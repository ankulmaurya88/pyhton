from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for home page
    path('about/', views.about, name='about'),  # Route for about page
    path('scrape/', views.scrape_flipkart_mobiles, name='scrape_flipkart_mobiles'),
]