from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='insjack_app.index'),  # Set root to login page
    path('register/', views.register, name='insjack_app.register'),
    # path('login/', views.login_view, name='login'),  # Custom login view
    # # path('logout/', views.logout_view, name='logout'),  # Custom logout view
    # path('upload/', views.upload_image, name='upload_image'),
    path('leaf/detection/', views.leaf, name='insjack_app.leaf'), 
    path('dashboard/', views.dashboard, name='insjack_app.home'),
]