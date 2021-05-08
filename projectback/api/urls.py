from django.urls import path
from api import views

from api.views import product_list, product_detail, category_list, product2_list, category2_list


urlpatterns = [
    path('api/product', product_list),
    path('api/product/<int:product_id>/', product_detail),
    path('api/category', category_list),
    path('api/product2', product2_list),
    path('api/category2', category2_list),
    path('api/product-list', views.ProductViewSet.as_view(), name='product-list'),
    path('product-list/<str:pk>/', views.ProductDetailViewSet.as_view(), name='product-detail')
]
