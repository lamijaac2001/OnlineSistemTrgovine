from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# urls.py

urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('search/', views.search, name="search"),
    path('orders/',views.orders,name="orders"),
    path('ordersmake',views.ordersmake,name="ordersmake"),
    path('orderconfirm',views.orderconfirm,name="orderconfirm"),
    path('ordershistory',views.ordershistory,name="ordershistory"),
    path('products',views.products,name="products"),
    path('cart/',views.cart,name="cart"),
    path('dodaj_u_korpu/<int:proizvod_id>/', views.dodaj_u_korpu, name='dodaj_u_korpu'),
    path('ukloni_iz_korpe/<int:proizvod_id>/', views.ukloni_iz_korpe, name='ukloni_iz_korpe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # za slike