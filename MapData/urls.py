from django.contrib import admin
from django.urls import path, include
from MapData_app import views  # Import views from MapData_app

urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),

    # Include routes from the app's urls.py (for API or app-specific URLs)
    path('api/', include('MapData_app.urls')),

    # Homepage route (mapped to home view function)
    path('', views.home, name='home'),  # Root URL
]
