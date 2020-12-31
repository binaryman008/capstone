from rest_framework import serializers
from .models import Category, User, Product, Review, Order, LineItem

# class CategorySerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = Category 
#         fields = ['name', 'description', 'photo']

class CategorySerializer(serializers.Serializer):
    """
    It will create serialized data for the problem 2
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CompanyTable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password', 'role', 'salt', 'googleId', 'facebookId']

    
class ProductSerializer(serializers.Serializer):
    """
    It will create serialized data for the problem 2
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.CharField()
    rating = serializers.IntegerField()
    price = serializers.IntegerField()
    categoryId = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CompanyTable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.price = validated_data.get('price', instance.price)
        instance.categoryId = validated_data.get('categoryId', instance.categoryId)
        instance.save()
        return instance


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'photo', 'rating', 'price', 'category']


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