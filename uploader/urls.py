from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api', views.GeneralViewSet, basename='general')

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('', include(router.urls)),
]
