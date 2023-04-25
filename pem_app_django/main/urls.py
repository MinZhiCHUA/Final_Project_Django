from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('multi', views.multi_func, name="multi"),
    path('product', views.tmp_product, name="product"),
]