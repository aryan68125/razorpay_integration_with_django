from django.urls import path
from payment_demo.views_bl import TestAPI
urlpatterns = [
    path('TestAPI/', TestAPI.as_view(),name="TestAPI"),
]
