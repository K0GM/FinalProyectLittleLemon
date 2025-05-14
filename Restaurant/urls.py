from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'reserva', views.ReservasViewSet)


urlpatterns = [
        path('home', views.index, name='home'),
        path('', include(router.urls)),
]
