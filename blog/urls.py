from django.urls import path, include
from blog import views
urlpatterns = [
    path('', views.blogdisplay, name='blogdisplay'),
    path('details/<str:pk>', views.details, name='details'),

]
