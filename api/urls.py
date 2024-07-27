from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet,show_db_settings,run_migrations

router = DefaultRouter()
router.register(r'persons', PersonViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('settings/', show_db_settings, name='show_db_settings'),
    path('run-migrations/', run_migrations,name='run migrations'),


]