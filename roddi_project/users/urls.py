from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views

urlpatterns = [
    #localhost:8000/users/login/ -> login page
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"),
         name="loginpage"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),
         name="logoutpage"),
    path('profile/', users_views.profile, name="profile"),
    path('registation/', users_views.register, name="registration"),
    path('update-profile/', users_views.update_profile.as_view(), name='update-profile'),
    path('notify/', users_views.notify.as_view(), name='notify'),
    path('notify/<email>', users_views.notifyUser, name='notify-user'),
]