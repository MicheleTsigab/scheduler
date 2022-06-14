from django.urls import path,include
from rest_framework_nested import routers
from .views import *
router = routers.SimpleRouter()
router.register(r'doctor', doctorViewset)
router.register(r'patient',patientViewset)
availablity = routers.NestedSimpleRouter(router, r'doctor', lookup='doctor')
availablity.register(r'availablity', availablityViewset,basename='doctor-availablity')
doc_appointment=routers.NestedSimpleRouter(router,r'doctor',lookup='doctor')
doc_appointment.register(r'appt',docapptViewset,basename='doctor-appointment')
pat_appointment=routers.NestedSimpleRouter(router,r'patient',lookup='patient')
pat_appointment.register(r'appt',patapptViewset,basename='patient-appointment')
#home_appointment=
doc_homeappointment=routers.NestedSimpleRouter(router,r'doctor',lookup='doctor')
doc_homeappointment.register(r'homeappt',dochomeapptViewset,basename='doctor-homeappointment')
pat_homeappointment=routers.NestedSimpleRouter(router,r'patient',lookup='patient')
pat_homeappointment.register(r'homeappt',pathomeapptViewset,basename='patient-homeappointment')
docr= routers.DefaultRouter()
docr.register(r'doctor', doctorsWithinR,basename='doctorwithin')
#home_appointment=
urlpatterns = [
    path(r'',index),
    path(r'', include(router.urls)),
    path(r'', include(availablity.urls)),
    path(r'',include(doc_appointment.urls)),
    path(r'',include(pat_appointment.urls)),
    path(r'',include(doc_homeappointment.urls)),
    path(r'',include(pat_homeappointment.urls)),
    #path(r'',include(docr.urls))
    path('doctors/',doctorsWithinR.as_view({'get':'list'}))
]
#urlpatterns += router.urls
#urlpatte
