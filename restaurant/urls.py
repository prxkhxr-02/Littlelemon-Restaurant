from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/',views.menu,name="menu"),
    path('contact_us/',views.contact_us, name="contact_us"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
    path('feedback/',views.feedback, name="feedback"),

]