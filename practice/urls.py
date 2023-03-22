from django.urls import path
from practice import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('people/',views.people, name='people' ),
    path('detailPerson/<int:id>',views.detailPeople, name='detailPeople' ),
]