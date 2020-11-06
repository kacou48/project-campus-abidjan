"""enmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from users.views import UserProfileView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('qui_suis_je/', user_views.ma_page, name='qui_suis_je'),
    path('user_profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('profile_update/', user_views.profile_update, name='profile_update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/index.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('like/', views.LikeView, name='like_post'),
    path('', include('blog.urls')),
    path('social_login/', include('social_django.urls', namespace='social')),
    path('', include('send_mail_app.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
