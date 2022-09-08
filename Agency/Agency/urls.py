from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Path to access django admin
    path('admin/', admin.site.urls),
    
  # ============================ FRONTEND SECTION ========================== |
    #Path to render homepage
    path('', views.home, name="home"),
     #Path to render opportunities page
    path('opportunities', views.opportunities, name="opportunities"),
    # PAth to Login/Logout
    path('login/', include('django.contrib.auth.urls')),
  # PAth to Support
    path('support', views.support, name="support"),
    
    # ============================ SEND EMAIL ========================== |
    # PAth to send frontend form
    path('email_frontend', views.email_frontend, name="email_frontend"),
     # PAth to send backend form
    path('email_backend', views.email_backend, name="email_backend"),
     # PAth to send fullstack form
    path('email_fullstack', views.email_fullstack, name="email_fullstack"),
    
    # ============================ BACKEND SECTION =================
     path('backend/', views.backend, name="backend"),   
  
]
