from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='Home'),
    path("doctors/<str:type>",views.doctors_view,name='Doctors'),
    path('create_profile/<str:name>',views.create_profile, name='Create_profile'),
    path('P_details/<str:p_name>',views.p_details, name='P_details'),
    path('p_details',views.doc_profile, name='p_details'),
    path('prescription/<str:id>',views.prescription1, name='prescription'),
    path('all_patient',views.all_patient, name='all_patient'),
    path('msg',views.msg, name='msg'),
]