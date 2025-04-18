from django.urls import path, re_path
from . import views

urlpatterns = [
    # API endpoints
    path('api/signup/', views.signup, name='signup'),
    path('api/signin/', views.signin, name='signin'),

    # Serve React App - catch all other URLs
    re_path(r'^.*', views.index, name='index'),
]