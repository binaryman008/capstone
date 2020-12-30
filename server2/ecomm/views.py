from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Category, User, Product, Review, Order, LineItem
from rest_framework.response import Response
from .serializers import CategorySerializer, UserSerializer, ProductSerializer,\
    ReviewSerializer, OrderSerializer, LineItemSerializer

# Create your views here.

class CategoryView(APIView): 
    serializer_class = CategorySerializer 
    def get(self, request): 
        detail = [ {"name": detail.name,"description": detail.description,"photo":detail.photo}  
        for detail in Category.objects.all()] 
        return Response(detail) 
    def post(self, request): 
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)

class UserView(APIView): 
    serializer_class = UserSerializer 
    def get(self, request): 
        detail = [ {
            "email": detail.email,"password": detail.password,"role":detail.role,
            "salt": detail.salt,"googleId": detail.googleId,"facebookId":detail.facebookId
            }  
        for detail in User.objects.all()] 
        return Response(detail) 
    def post(self, request): 
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)

class ProductView(APIView): 
    serializer_class = ProductSerializer 
    def get(self, request): 
        detail = [ {
            "name": detail.name,"description": detail.description,"photo":detail.photo,
            "rating": detail.rating,"price": detail.price,"category":detail.category.id}  
        for detail in Product.objects.all()] 
        return Response(detail) 
    def post(self, request): 
        serializer = ProductSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)

class ReviewView(APIView): 
    serializer_class = ReviewSerializer 
    def get(self, request): 
        detail = [ {
            "title": detail.title,"content": detail.content,"rating":detail.rating,
            "product": detail.product,"user": detail.user
            }  
        for detail in Review.objects.all()] 
        return Response(detail) 
    def post(self, request): 
        serializer = ReviewSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)

class OrderView(APIView): 
    serializer_class = OrderSerializer 
    def get(self, request): 
        detail = [ {
            "status": detail.status,"firstname": detail.firstname,"lastname":detail.lastname,
            "street": detail.street,"street2": detail.street2,
            "state": detail.state,"zip_code": detail.zip_code,"phone":detail.phone,
            "email": detail.email,"user": detail.user}  
        for detail in Order.objects.all()] 
        return Response(detail) 
    def post(self, request): 
        serializer = OrderSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)

class LineItemView(APIView): 
    serializer_class = LineItemSerializer 
    def get(self, request): 
        detail = [ {"quantity": detail.quantity,"product": detail.product}  
        for detail in Line.objects.all()] 
        return Response(detail) 
    def post(self, request): 
        serializer = LineItemSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)

