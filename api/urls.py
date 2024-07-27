from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet,show_db_settings

router = DefaultRouter()
router.register(r'persons', PersonViewSet)


urlpatterns = [
    path('', include(router.urls)),
        path('settings/', show_db_settings, name='show_db_settings'),

]