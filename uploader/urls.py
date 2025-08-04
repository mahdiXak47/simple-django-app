from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'healthz', views.GeneralViewSet, basename='general')

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('healthz/', views.GeneralViewSet.as_view({'get': 'healthz'}), name='healthz'),
    path('', include(router.urls)),
]
