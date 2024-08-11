import hashlib
import json
import re
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
from django.conf import settings
from .models import Nutrient, ImageResponseCache, UserProfile, UserFood
from .serializers import NutrientSerializer, UserProfileSerializer, UserFoodSerializer
from django.db.models import F, Sum
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.utils import timezone
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def handle_uploaded_file(uploaded_file):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(uploaded_file)
    sha256_checksum = sha256_hash.hexdigest()
    return sha256_checksum


def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


def extract_json_list(text):
    # Regular expression to match a JSON list, including empty and multiline lists
    json_list_pattern = r'\[\s*(?:[^\[\]]|\n)*?\s*\]'

    # Search for the JSON list in the text
    match = re.search(json_list_pattern, text, re.DOTALL)

    if match:
        json_list_str = match.group(0)
        try:
            # Convert the matched string to an actual Python list
            json_list = json.loads(json_list_str)
            return json_list
        except json.JSONDecodeError:
            return []
    return []


class GetNeutrientInfo(APIView):
    def post(self, request, *args, **kwargs):
        image = request.data.get("image")
        image_hash = handle_uploaded_file(image.read())
        cache, created = ImageResponseCache.objects.get_or_create(
            photo_hash=image_hash)
        if not created:
            foods = cache.response
        else:
            image.seek(0)
            uploaded_image = client.files.create(
                file=(image.name, image.read(), image.content_type),
                purpose="vision"
            )
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=[
                    {
                        "type": "image_file",
                        "image_file": {"file_id": uploaded_image.id}
                    }
                ],
            )
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=settings.OPENAI_ASSISTANT_ID,
            )
            print(f"thread_id: {thread.id}")
            wait_on_run(run, thread)
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            try:
                resp_value = messages.data[0].content[0].text.value
                print(f"resp_value: {resp_value}")
                resp_value = extract_json_list(resp_value)
                print(f"resp_value: {resp_value}")
            except Exception as e:
                resp_value = []
            cache.response = resp_value
            cache.save()
            foods = resp_value
        foods_object = Nutrient.objects.filter(food_name__in=foods)
        serializer = NutrientSerializer(foods_object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileMainPage(APIView):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.filter(
            user=request.user).first()
        if not user_profile:
            return Response({"message": "User Profile Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserFoodPerTime(APIView):
    def get(self, request, *args, **kwargs):
        time = request.query_params.get('time')
        date = timezone.now().date()
        # user_profile = UserProfile.objects.filter(
        #     user=request.user).first()
        # if not user_profile:
        #     return Response({"message": "User Profile Not Found"}, status=status.HTTP_404_NOT_FOUND)
        consumed_foods = request.user.consumed_foods.filter(
            time=time, created_at=date)
        print(consumed_foods)
        # nutrients = [food.food for food in consumed_foods]
        serializer = UserFoodSerializer(consumed_foods, many=True)
        total_carbohydrates = consumed_foods.aggregate(
            total_carbohydrates=Sum(F('food__carbohydrate') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_carbohydrates')
        total_protein = consumed_foods.aggregate(
            total_protein=Sum(F('food__protein') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_protein')
        total_fat = consumed_foods.aggregate(
            total_fat=Sum(F('food__fat') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_fat')
        total_energy = consumed_foods.aggregate(
            total_energy=Sum(F('food__energy') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_energy')
        return Response({"food_items": serializer.data, "total_carbohydrates": total_carbohydrates, "total_protein": total_protein, "total_fat": total_fat, 'total_energy': total_energy}, status=status.HTTP_200_OK)


class UserFoodImageUpload(APIView):
    def post(self, request, *args, **kwargs):
        image = request.data.get("image")
        time = request.data.get("time")
        image_hash = handle_uploaded_file(image.read())
        cache, created = ImageResponseCache.objects.get_or_create(
            photo_hash=image_hash)
        if not created:
            foods = cache.response
        else:
            image.seek(0)
            uploaded_image = client.files.create(
                file=(image.name, image.read(), image.content_type),
                purpose="vision"
            )
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=[
                    {
                        "type": "image_file",
                        "image_file": {"file_id": uploaded_image.id}
                    }
                ],
            )
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=settings.OPENAI_ASSISTANT_ID,
            )

            wait_on_run(run, thread)
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            try:
                resp_value = messages.data[0].content[0].text.value
                resp_value = extract_json_list(resp_value)
            except Exception as e:
                resp_value = []
            cache.response = resp_value

            cache.save()
            foods = resp_value
        foods_object = Nutrient.objects.filter(food_name__in=foods).order_by(
            'food_name', 'id')
        # Use a dictionary to keep only the first occurrence of each food_name
        unique_nutrients = {}
        for nutrient in foods_object:
            if nutrient.food_name not in unique_nutrients:
                unique_nutrients[nutrient.food_name] = nutrient

        # Convert the dictionary values back to a list of Nutrient objects
        nutrients = list(unique_nutrients.values())

        [UserFood(
            user=request.user, food=food, serving=1, time=time).save() for food in nutrients]
        return Response({"message": "Food Items Added Successfully"}, status=status.HTTP_200_OK)


class UserFoodRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = UserFood.objects.all()
    serializer_class = UserFoodSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'food_id'
