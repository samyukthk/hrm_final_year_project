from .models import Product
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myenvapp.serializers import  ProductSerializer
from myenvapp.serializers import  CategorySerializer
from rest_framework import status
from myenvapp.models import Product
from myenvapp.models import Category
from myenvapp.serializers import *
from myenvapp.models import *
from rest_framework.decorators import api_view, APIView
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view()
def index(request):
    return Response({"message": "index!"})


@api_view(['GET'])
def Product_list(request):
    if request.method == 'GET':
        account = Product.objects.all()
        serializers = ProductSerializer(account, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def Category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def Product_add(request):
    if request.method == 'GET':
        account = Product.objects.all()
        serializers = ProductSerializer(account, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#######################################################################################################   
    
@api_view(['GET'])
def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'DELETE'])
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    ####################################################################################################
    
    
@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializers = UserSerializer(user, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    
@api_view(['GET','POST'])
def user_add(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializers = UserSerializer(user, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE'])
def user_delete(request, category_id):
    user = User.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    ##################################################
    
    
    
    
@api_view(['GET', 'PATCH'])
def user_edit(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except user.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    ##########################################################################
    
    
    
@api_view(['GET', 'PUT'])
def category_edit2(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#######################################student##############################################


@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializers = StudentSerializer(student, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)  
 
 
 
    
@api_view(['GET','POST'])
def student_add(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializers = StudentSerializer(student, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'DELETE'])
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method ==  'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'PATCH'])
def student_edit(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except student.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
@api_view(['GET', 'PUT'])
def student_edit2(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    ###########################################image###################################################
    
    
@api_view(['GET'])
def image_list(request):
    if request.method == 'GET':
        image = ImageTest.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    #######################################order using class api calling#########################################


class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderAdd(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all() 
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDelete(APIView):
    def get(self, request, order_id, format=None):
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, order_id, format=None):
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderEdit(APIView):
    def get(self, request, order_id, format=None):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, order_id, format=None):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class OrderEdit2(APIView):
    def get(self, request, order_id, format=None):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id, format=None):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Oreder not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
        
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)