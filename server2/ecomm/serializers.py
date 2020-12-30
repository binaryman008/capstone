from rest_framework import serializers
from .models import Category, User, Product, Review, Order, LineItem

class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = ['name', 'description', 'photo']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password', 'role', 'salt', 'googleId', 'facebookId']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'rating', 'price', 'category']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating', 'product', 'user']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'status', 'firstname', 'lastname', 'street', 'street2',
            'state', 'zip_code', 'phone', 'email', 'user'
            ]


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ['quantity', 'product']