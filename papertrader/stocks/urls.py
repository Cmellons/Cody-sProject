
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),  # Your existing index view
    path('add_stock/', views.add_stock, name='add_stock'),  # URL for adding stocks
    path('add_user_stock/', views.add_user_stock, name='add_user_stock'),  # URL for adding user stocks
    path('success/', views.success, name='success'),  # URL for success page
    path('buy_stock/', views.buy_stock, name='buy_stock'),  # Define URL for buying stocks
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)



