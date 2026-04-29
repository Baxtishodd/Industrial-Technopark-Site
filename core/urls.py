from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    # services
    path('electric_power', views.electric_power, name='electric_power'),
    path('security', views.security, name='security'),
    path('hot_water', views.hot_water, name='hot_water'),
    path('steam_supply', views.steam_supply, name='steam_supply'),
    path('gas_supply', views.gas_supply, name='gas_supply'),

    # projects
    path('dyeing_finishing', views.dyeing_finishing, name='dyeing_finishing'),
    path('flour_production', views.flour_production, name='flour_production'),
    path('power_generation', views.power_generation, name='power_generation'),
    path('garment_manufacturing', views.garment_manufacturing, name='garment_manufacturing'),
    path('oil_production', views.oil_production, name='oil_production'),

    # contact
    path('location', views.location, name='location'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('management/', views.management_list, name='management'),
    path('leadership/', views.leadership_list, name='leadership'),





]








