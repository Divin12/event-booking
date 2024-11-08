from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'apartment'

urlpatterns = [
    path('apartment_list/', views.apartment_list, name='apartment_list'),
    path('apartment_detail/<str:apartment_name>/', views.apartment_detail_view, name='apartment_detail'),
    path('apartment_name/', views.apartment_name_list_view, name='apartment_name'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
