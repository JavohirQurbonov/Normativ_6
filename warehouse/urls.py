from django.urls import path
from warehouse.views import product_list, categories_list, category_products, contact, success_message, book_list, \
    detail_view, create_view, update_view, delete_view

urlpatterns = [
    path('',product_list,name='product_list'),
    path('categories/',categories_list,name='categories'),
    path('products/<int:pk>',category_products,name='category_products'),
    path('contact/',contact,name='contact'),
    path('success/',success_message,name='success_page'),

    path('books/',book_list,name='book_list'),
    path('detail/<int:pk>',detail_view,name='detail'),
    path('create/',create_view,name='create'),
    path('update/<int:pk>',update_view,name='update'),
    path('delete/<int:pk>',delete_view,name='delete')
]