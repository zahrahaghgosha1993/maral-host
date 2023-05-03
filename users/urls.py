from django.urls import path, include
import users.panel.views as panel

urlpatterns = [
    path('api/', include('users.api.urls')),
    path('panel/', include('users.panel.urls')),
]
