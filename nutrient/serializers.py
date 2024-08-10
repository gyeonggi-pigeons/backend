from rest_framework import serializers
from .models import Nutrient, UserProfile, UserFood
from django.db.models import F, Sum
from django.utils import timezone


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    today_total_calories = serializers.SerializerMethodField()
    breakfast_calories = serializers.SerializerMethodField()
    lunch_calories = serializers.SerializerMethodField()
    dinner_calories = serializers.SerializerMethodField()
    snack_calories = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_today_total_calories(self, obj):
        return obj.consumed_foods.filter(created_at=timezone.now().date()).aggregate(
            total_calories=Sum(F('food__energy') * F('serving') * (F('food__food_weight') / F('food__nutrition_content_standard')))).get('total_calories')

    def get_breakfast_calories(self, obj):
        return obj.consumed_foods.filter(created_at=timezone.now().date(), time='B').aggregate(
            total_calories=Sum(F('food__energy') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_calories')

    def get_lunch_calories(self, obj):
        return obj.consumed_foods.filter(created_at=timezone.now().date(), time='L').aggregate(
            total_calories=Sum(F('food__energy') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_calories')

    def get_dinner_calories(self, obj):
        return obj.consumed_foods.filter(created_at=timezone.now().date(), time='D').aggregate(
            total_calories=Sum(F('food__energy') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_calories')

    def get_snack_calories(self, obj):
        return obj.consumed_foods.filter(created_at=timezone.now().date(), time='S').aggregate(
            total_calories=Sum(F('food__energy') * F('serving') * F('food__food_weight') / F('food__nutrition_content_standard'))).get('total_calories')


class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFood
        fields = '__all__'
