from django.urls import path, re_path
from .views import HomeView, ProjectView, ContactView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('projects/', ProjectView.as_view(), name='project_list'),
    path('contact/', ContactView.as_view(), name='contact'),
]
