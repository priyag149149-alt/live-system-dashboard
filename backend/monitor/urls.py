
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('me/', me_view),
    path('system/stats/', stats_view),
]