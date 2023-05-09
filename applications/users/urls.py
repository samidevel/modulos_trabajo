from django.urls import path, reverse_lazy, reverse
from . import views
from django.contrib.auth import views as auth_views


#app_name = 'users_app'

urlpatterns = [
    path('', views.LoginUser.as_view(), name='login_user'),
    path('logout-user', views.Logout_View.as_view(), name='logout'),
    path('create-users', views.UserCreateView.as_view(), name='create_users'),
    path('user-update/<pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('change-password', views.UserPasswordChange.as_view(), name='change_password'),
    path('password-user', views.UserUpdatePassword.as_view(), name='password_user'),
    path('turnos-view', views.TurnosView.as_view(), name='turnos_view'),        
    path('list-users', views.ListUserRegister.as_view(), name='list_users'),


    path('reset_password',
          auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="reset_password"),

    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
),

    #path('reset/<uidb64>/<token>/', 
         #auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_confirm_email',
         #success_url=reverse_lazy('users:app:password_reset_complete')), name="password_reset_confirm"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('password_reset_complete', 
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    
]
