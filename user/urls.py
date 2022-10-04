from django.urls import path
from . import views

urlpatterns = [
    path('Join/', views.sign_up_view, name='Join'),
    path('Log_in/', views.sign_in_view, name='Log_in'),
    path('logout/', views.logout, name='logout'),
]