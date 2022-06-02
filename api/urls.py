from django.urls import path,include
from rest_framework_nested import routers
from .views import *
router = routers.SimpleRouter()
router.register(r'doctor', doctorViewset)
router.register(r'patient',patientViewset)
availablity = routers.NestedSimpleRouter(router, r'doctor', lookup='doctor')
availablity.register(r'availablity', availablityViewset,basename='doctor-availablity')
doc_appointment=routers.NestedSimpleRouter(router,r'doctor',lookup='doctor')
doc_appointment.register(r'appointment',docapptViewset,basename='doctor-appointment')
#home_appointment=
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(availablity.urls)),
]
#urlpatterns += router.urls
#urlpatte
