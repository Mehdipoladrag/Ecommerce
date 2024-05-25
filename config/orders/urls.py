from django.urls import path
from .views import CartView
app_name = 'orders'

urlpatterns = [
    path('cart', CartView.as_view(), name='cart')
]