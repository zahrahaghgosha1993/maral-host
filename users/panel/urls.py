from django.urls import path
import users.panel.views as panel

urlpatterns = [
    path('login/', panel.LoginView.as_view(), name='user_login'),
    path('', panel.PanelView, name='user_panel'),
]
