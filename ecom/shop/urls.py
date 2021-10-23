from django.urls import path
from .views import index, about, contact, tracker, search, productView, checkout
urlpatterns = [
    path('', index, name ="home"),
    path('about/', about, name ="AboutUs"),
    path('contact/', contact, name ="Contact"),
    path('tracker/', tracker, name ="TrackingStatus"),
    path('search/', search, name ="Search"),
    path('productview/', productView, name ="ProductView"),
    path('checkout/', checkout, name ="CheckOut"),

]