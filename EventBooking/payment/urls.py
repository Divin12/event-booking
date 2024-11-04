from django.urls import path
from . import views

urlpatterns = [
    path('make_payment/<int:order_id>/', views.make_payment, name='make_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),

]