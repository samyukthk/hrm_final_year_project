
from .models import Category, Product, Student, User, ImageTest ,Order
from rest_framework  import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageTest
        fields = '__all__'
        
        
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'