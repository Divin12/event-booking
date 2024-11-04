from django.urls import path
from . import views
app_name = 'user_Authentification'

urlpatterns = [
    path('signup/', views.register_view, name='signup'),
    path('signin/', views.login_view, name='login_view'),
    path('signout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('password/', views.password_reset, name='password_reset'),
    path('profile/create-profile/', views.create_or_update_profile, name='create_or_update_profile'),

    # Other URL patterns if present
]





