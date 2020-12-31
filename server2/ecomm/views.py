from django.shortcuts import render
from .models import Category, User, Product, Review, Order, LineItem
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Case, When, Value, CharField, IntegerField, F
from .serializers import CategorySerializer, UserSerializer, ProductSerializer,\
    ReviewSerializer, OrderSerializer, LineItemSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def category_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Product.objects.annotate(categoryId=Case(
            When(category__pk=pk, then=Value(pk)),
            # default=Value('categoryId'),
            output_field=IntegerField(),
        )).filter(category__pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        for i in snippet:
            print(i.category.id)
        serializer = ProductSerializer(snippet, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Product.objects.annotate(categoryId=F('category')).all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserView(APIView): 
#     serializer_class = UserSerializer 
#     def get(self, request): 
#         detail = [ {
#             "email": detail.email,"password": detail.password,"role":detail.role,
#             "salt": detail.salt,"googleId": detail.googleId,"facebookId":detail.facebookId
#             }  
#         for detail in User.objects.all()] 
#         return Response(detail) 
#     def post(self, request): 
#         serializer = UserSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save() 
#             return  Response(serializer.data)



# class ReviewView(APIView): 
#     serializer_class = ReviewSerializer 
#     def get(self, request): 
#         detail = [ {
#             "title": detail.title,"content": detail.content,"rating":detail.rating,
#             "product": detail.product,"user": detail.user
#             }  
#         for detail in Review.objects.all()] 
#         return Response(detail) 
#     def post(self, request): 
#         serializer = ReviewSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save() 
#             return  Response(serializer.data)

# class OrderView(APIView): 
#     serializer_class = OrderSerializer 
#     def get(self, request): 
#         detail = [ {
#             "status": detail.status,"firstname": detail.firstname,"lastname":detail.lastname,
#             "street": detail.street,"street2": detail.street2,
#             "state": detail.state,"zip_code": detail.zip_code,"phone":detail.phone,
#             "email": detail.email,"user": detail.user}  
#         for detail in Order.objects.all()] 
#         return Response(detail) 
#     def post(self, request): 
#         serializer = OrderSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save() 
#             return  Response(serializer.data)

# class LineItemView(APIView): 
#     serializer_class = LineItemSerializer 
#     def get(self, request): 
#         detail = [ {"quantity": detail.quantity,"product": detail.product}  
#         for detail in Line.objects.all()] 
#         return Response(detail) 
#     def post(self, request): 
#         serializer = LineItemSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save() 
#             return  Response(serializer.data)

