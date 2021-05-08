from django.urls import path

from api.views import product_list, product_detail, category_list


urlpatterns = [
    path('api/product', product_list),
    path('api/product/<int:product_id>/', product_detail),
    path('api/category', category_list)
]
