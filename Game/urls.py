from django.urls import path
from .views import travel, greet, fight
app_name='Game'
urlpatterns=[
    path('', greet, name='greetings'),
    path('travel/', travel, name='travel'),
    path('fight/', fight, name='fight'),
]