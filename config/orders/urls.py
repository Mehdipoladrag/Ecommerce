from django.urls import path
from .views import CartView, CartAddView, CartRemoveView, OrderCreateView, OrderDetailView
app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),

]