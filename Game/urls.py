from django.urls import path
from .views import travel, greet
app_name='Game'
urlpatterns=[
    path('', greet, name='greetings'),
    path('travel/', travel, name='travel'),
]