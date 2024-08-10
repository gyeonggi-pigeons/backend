from django.db import models
from django.contrib.auth import get_user_model


class Nutrient(models.Model):
    food_code = models.CharField(max_length=255)  # 식품코드
    food_name = models.CharField(max_length=255)  # 식품명
    data_type_code = models.CharField(max_length=10)  # 데이터구분코드
    data_type_name = models.CharField(max_length=255)  # 데이터구분명
    food_origin_code = models.CharField(max_length=10)  # 식품기원코드
    food_origin_name = models.CharField(max_length=255)  # 식품기원명
    food_category_large_code = models.CharField(max_length=10)  # 식품대분류코드
    food_category_large_name = models.CharField(max_length=255)  # 식품대분류명
    representative_food_code = models.CharField(max_length=10)  # 대표식품코드
    representative_food_name = models.CharField(max_length=255)  # 대표식품명
    food_category_medium_code = models.CharField(max_length=10)  # 식품중분류코드
    food_category_medium_name = models.CharField(max_length=255)  # 식품중분류명
    food_category_small_code = models.CharField(max_length=10)  # 식품소분류코드
    food_category_small_name = models.CharField(max_length=255)  # 식품소분류명
    food_category_detail_code = models.CharField(max_length=10)  # 식품세분류코드
    food_category_detail_name = models.CharField(max_length=255)  # 식품세분류명
    nutrition_content_standard = models.FloatField()  # 영양성분함량기준량
    nutrition_content_standard_type = models.CharField(
        max_length=50, null=True)  # 영양성분함량기준량구분
    energy = models.FloatField(null=True)  # 에너지(kcal)
    moisture = models.FloatField(null=True)  # 수분(g)
    protein = models.FloatField(null=True)  # 단백질(g)
    fat = models.FloatField(null=True)  # 지방(g)
    ash = models.FloatField(null=True)  # 회분(g)
    carbohydrate = models.FloatField(null=True)  # 탄수화물(g)
    sugars = models.FloatField(null=True)  # 당류(g)
    dietary_fiber = models.FloatField(null=True)  # 식이섬유(g)
    calcium = models.FloatField(null=True)  # 칼슘(mg)
    iron = models.FloatField(null=True)  # 철(mg)
    phosphorus = models.FloatField(null=True)  # 인(mg)
    potassium = models.FloatField(null=True)  # 칼륨(mg)
    sodium = models.FloatField(null=True)  # 나트륨(mg)
    vitamin_a = models.FloatField(null=True)  # 비타민 A(μg RAE)
    retinol = models.FloatField(null=True)  # 레티놀(μg)
    beta_carotene = models.FloatField(null=True)  # 베타카로틴(μg)
    thiamin = models.FloatField(null=True)  # 티아민(mg)
    riboflavin = models.FloatField(null=True)  # 리보플라빈(mg)
    niacin = models.FloatField(null=True)  # 니아신(mg)
    vitamin_c = models.FloatField(null=True)  # 비타민 C(mg)
    vitamin_d = models.FloatField(null=True)  # 비타민 D(μg)
    cholesterol = models.FloatField(null=True)  # 콜레스테롤(mg)
    saturated_fatty_acids = models.FloatField(null=True)  # 포화지방산(g)
    trans_fatty_acids = models.FloatField(null=True)  # 트랜스지방산(g)
    sucrose = models.FloatField(null=True)  # 자당(g)
    glucose = models.FloatField(null=True)  # 포도당(g)
    fructose = models.FloatField(null=True)  # 과당(g)
    lactose = models.FloatField(null=True)  # 유당(g)
    maltose = models.FloatField(null=True)  # 맥아당(g)
    magnesium = models.FloatField(null=True)  # 마그네슘(mg)
    zinc = models.FloatField(null=True)  # 아연(mg)
    copper = models.FloatField(null=True)  # 구리(μg)
    manganese = models.FloatField(null=True)  # 망간(mg)
    selenium = models.FloatField(null=True)  # 셀레늄(μg)
    tocopherol = models.FloatField(null=True)  # 토코페롤(mg)
    tocotrienol = models.FloatField(null=True)  # 토코트리에놀(mg)
    folate = models.FloatField(null=True)  # 엽산(μg DFE)
    vitamin_b12 = models.FloatField(null=True)  # 비타민 B12(μg)
    amino_acids = models.FloatField(null=True)  # 아미노산(mg)
    isoleucine = models.FloatField(null=True)  # 이소류신 / 이소루신(mg)
    leucine = models.FloatField(null=True)  # 류신 / 루신(mg)
    lysine = models.FloatField(null=True)  # 라이신(mg)
    methionine = models.FloatField(null=True)  # 메티오닌(mg)
    phenylalanine = models.FloatField(null=True)  # 페닐알라닌(mg)
    threonine = models.FloatField(null=True)  # 트레오닌(mg)
    valine = models.FloatField(null=True)  # 발린(mg)
    histidine = models.FloatField(null=True)  # 히스티딘(mg)
    arginine = models.FloatField(null=True)  # 아르기닌(mg)
    tyrosine = models.FloatField(null=True)  # 티로신(mg)
    cysteine = models.FloatField(null=True)  # 시스테인(mg)
    alanine = models.FloatField(null=True)  # 알라닌(mg)
    aspartic_acid = models.FloatField(null=True)  # 아스파르트산(mg)
    glutamic_acid = models.FloatField(null=True)  # 글루탐산(mg)
    glycine = models.FloatField(null=True)  # 글리신(mg)
    proline = models.FloatField(null=True)  # 프롤린(mg)
    serine = models.FloatField(null=True)  # 세린(mg)
    butyric_acid = models.FloatField(null=True)  # 부티르산(4:0)(mg)
    caproic_acid = models.FloatField(null=True)  # 카프로산(6:0)(mg)
    caprylic_acid = models.FloatField(null=True)  # 카프릴산(8:0)(mg)
    capric_acid = models.FloatField(null=True)  # 카프르산(10:0)(mg)
    lauric_acid = models.FloatField(null=True)  # 라우르산(12:0)(mg)
    myristic_acid = models.FloatField(null=True)  # 미리스트산(14:0)(mg)
    palmitic_acid = models.FloatField(null=True)  # 팔미트산(16:0)(mg)
    stearic_acid = models.FloatField(null=True)  # 스테아르산(18:0)(mg)
    arachidic_acid = models.FloatField(null=True)  # 아라키드산(20:0)(mg)
    myristoleic_acid = models.FloatField(null=True)  # 미리스톨레산(14:1)(mg)
    palmitoleic_acid = models.FloatField(null=True)  # 팔미톨레산(16:1)(mg)
    oleic_acid = models.FloatField(null=True)  # 올레산(18:1 n-9)(mg)
    vaccenic_acid = models.FloatField(null=True)  # 박센산(18:1 n-7)(mg)
    # 가돌레산(20:1 n-11) / 에이코센산(20:1 n-9)(mg)
    gadoleic_acid = models.FloatField(null=True)
    linoleic_acid = models.FloatField(null=True)  # 리놀레산(18:2 n-6)(g)
    alpha_linolenic_acid = models.FloatField(null=True)  # 알파리놀렌산(18:3 n-3)(g)
    gamma_linolenic_acid = models.FloatField(
        null=True)  # 감마 리놀렌산(18:3 n-6)(mg)
    eicosadienoic_acid = models.FloatField(null=True)  # 에이코사디에노산(20:2 n-6)(mg)
    arachidonic_acid = models.FloatField(null=True)  # 아라키돈산(20:4 n-6)(mg)
    eicosatrienoic_acid = models.FloatField(
        null=True)  # 에이코사트리에노산(20:3 n-6)(mg)
    epa = models.FloatField(null=True)  # 에이코사펜타에노산(EPA, 20:5 n-3)(mg)
    dpa = models.FloatField(null=True)  # 도코사펜타에노산(DPA, 22:5 n-3)(mg)
    dha = models.FloatField(null=True)  # 도코사헥사에노산(DHA, 22:6 n-3)(mg)
    trans_oleic_acid = models.FloatField(
        null=True)  # 트랜스 올레산(18:1 trans n-9)(mg)
    trans_linoleic_acid = models.FloatField(null=True)  # 트랜스 리놀레산(18:2t)(mg)
    trans_linolenic_acid = models.FloatField(null=True)  # 트랜스 리놀렌산(18:3t)(mg)
    caffeine = models.FloatField(null=True)  # 카페인(mg)
    source_code = models.CharField(max_length=10)  # 출처코드
    source_name = models.CharField(max_length=255)  # 출처명
    food_weight = models.FloatField(null=True)  # 식품중량
    food_weight_type = models.CharField(max_length=50, null=True)  # 식품중량구분
    company_name = models.CharField(max_length=255)  # 업체명
    data_creation_method_code = models.CharField(max_length=10)  # 데이터생성방법코드
    data_creation_method_name = models.CharField(max_length=255)  # 데이터생성방법명
    data_creation_date = models.DateField(null=True)  # 데이터생성일자
    data_reference_date = models.DateField(null=True)  # 데이터기준일자

    def __str__(self):
        return f"{self.food_code} - {self.food_name}"


class ImageResponseCache(models.Model):
    photo_hash = models.CharField(max_length=255)
    response = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.response} - {self.photo_hash}"


class UserProfile(models.Model):
    ACTIVITY_LEVEL_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )
    STATUS_CHOICES = (
        ('A', 'Preparing for Pregnancy'),
        ('B', 'Pregnant'),
        ('C', 'After Having a Baby'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    activity_level = models.CharField(
        max_length=1, choices=ACTIVITY_LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True)
    birth_count = models.PositiveSmallIntegerField(null=True)
    gestational_diabetes = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.nickname}"


class UserFood(models.Model):
    TIME_CHOICES = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('S', 'Snack'),
    )
    user = models.ForeignKey(
        get_user_model(), related_name="consumed_foods", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        UserProfile, related_name="consumed_foods", on_delete=models.CASCADE, null=True)
    food = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    serving = models.FloatField(default=1)
    time = models.CharField(max_length=1, choices=TIME_CHOICES)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.user_profile = UserProfile.objects.get(user=self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.food.food_name}"

    class Meta:
        ordering = ['-created_at']


class UserWeight(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="weights", on_delete=models.CASCADE)
    weight = models.FloatField()
    created_at = models.DateField(auto_now_add=True, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.weight}"

    class Meta:
        ordering = ['created_at']
