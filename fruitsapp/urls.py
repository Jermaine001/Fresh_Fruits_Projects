from django.urls import path
from .views import (
    index,
    contact,
    about,
    shop
)

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
]
