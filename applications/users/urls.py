from django.urls import path
from . import views


app_name = 'users_app'

urlpatterns = [
    path('', views.LoginUser.as_view(), name='login_user'),
    path('logout-user', views.Logout_View.as_view(), name='logout'),
    path('create-users', views.UserCreateView.as_view(), name='create_users'),
    path('user-update/<pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('change-password', views.UserPasswordChange.as_view(), name='change_password'),
    path('password-user', views.UserUpdatePassword.as_view(), name='password_user'),
    path('turnos-view', views.TurnosView.as_view(), name='turnos_view'),        
    path('list-users', views.ListUserRegister.as_view(), name='list_users'),

    path('reset_password', views.UserPasswordReset.as_view(template_name='users/password_reset.html'), name="reset_password"),

    path('password-reset-done', views.UserPasswordResetDone.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirm.as_view(), name="password_reset_confirm"),

    

    
]