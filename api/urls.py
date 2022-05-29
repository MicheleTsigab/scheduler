from django.urls import path
from rest_framework import routers
router = routers.SimpleRouter()
urlpatterns = [
    #path('',first_api_view)

]
urlpatterns += router.urls