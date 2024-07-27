from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet,show_db_settings

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'settings', show_db_settings)


urlpatterns = [
    path('', include(router.urls)),
]