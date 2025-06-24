from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet


# Create a router and register the SongViewSet.
router = DefaultRouter()
router.register(r'songs', SongViewSet) #the router will handle the URL routing for the SongViewSet

urlpatterns = [
    path('', include(router.urls)),
]
