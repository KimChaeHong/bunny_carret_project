from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# 유저 관련 모델
class Manner(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manner_seller') # 판매자 
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manner_buyer') # 구매자
    score = models.IntegerField() # 판매자 매너 점수
    created_at = models.DateTimeField(auto_now_add=True) # 매너 점수 등록일

    def __str__(self):
        return f'{self.seller.username}'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile') # 유저이름
    manner = models.ForeignKey(Manner, on_delete = models.SET_NULL, null=True, related_name='profile_manner') # 유저매너
    nickname = models.CharField(max_length=30, blank=True, null=True) # 유저 닉네임
    profile_img = models.ImageField(upload_to='post_images/', blank=True, null=True) # 유저 프로필 사진
    region = models.CharField(max_length=100, null=True) # 유저의 지역
    region_certification = models.CharField(max_length=1, default='N') # 유저 지역 확인

    def __str__(self):
        return f'{self.user.username} Profile'
    

# 상품 관련 모델
class Categroy(models.Model):
    name = models.CharField(max_length=100) # 카테고리 이름

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_seller') # 판매자
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_buyer') # 구매자
    category = models.ForeignKey(Categroy, on_delete=models.CASCADE, related_name='product_category') # 카테고리명
    region = models.CharField(max_length=100, null=True) # 지역
    price = models.IntegerField() # 가격
    title = models.CharField(max_length=200) # 상품명
    content = models.TextField() # 상품 설명
    images = models.ImageField(upload_to='post_images/') # 상품이미지
    created_at = models.DateTimeField(auto_now_add=True, null=True) # 상품 등록일자
    updated_at = models.DateTimeField(auto_now=True, null=True)  # 상품 수정일자
    product_reserved = models.CharField(max_length=1, default='N')  # 예약 여부
    product_sold = models.CharField(max_length=1, default='N')  # 판매 여부
    view_cnt = models.PositiveIntegerField(default=0)  # 조회 수
    chat_cnt = models.PositiveIntegerField(default=0)  # 채팅 수

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']



