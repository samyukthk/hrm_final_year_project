from django.urls import path
from myenvapp.views import *

urlpatterns = [
    path('Product', Product_list, name='product'),
    path('Productadd/', Product_add, name='product'),
    path('categorylist/',Category_list,name='category'),
    path('category/<int:category_id>/view/', category_view, name='category-view'),
    path('category/<int:category_id>/delete/', category_delete, name='category-delete'),
    path('Userlist/',user_list,name='user_list'),
    path('Useradd/', user_add, name='user_add'),
    path('User/<int:category_id>/delete/', user_delete, name='user-delete'),
    path('Useredit/<int:user_id>/edit/', user_edit, name='user-edit'),
    path('categoryedit/<int:category_id>/edit2/', category_edit2, name='category-delete'),
    path('studentlist/',student_list,name='student_list'),
    path('studentadd/', student_add, name='student_add'),
    path('student/<int:student_id>/delete/', student_delete, name='student-delete'),
    path('studentedit/<int:student_id>/edit/', student_edit, name='student-edit'),
    path('studentedit2/<int:student_id>/edit2/', student_edit2, name='student-edit2'),
    path('image/list', image_list, name='image-list'),
    
    path('order/list', OrderList.as_view(), name='order-list'),
    path('order/add/', OrderAdd.as_view(), name='order-add'),
    path('order/<int:order_id>/delete/', OrderDelete.as_view(), name='order-delete'),
    path('order/<int:order_id>/edit/', OrderEdit.as_view(), name='order-edit'),
    path('order/<int:order_id>/edit2/', OrderEdit2.as_view(), name='order-edit'),
]