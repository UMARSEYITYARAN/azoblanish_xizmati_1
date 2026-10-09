from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from app.views import LogoutView, MeView, RegisterView, ForgotPasswordView, ConfirmPasswordView, ResetPasswordView
from app.views import VerifyEmailView, ResendCodeView

schema_view = get_schema_view(
    openapi.Info(
        title="Radifus API",
        default_version='v1',
        description="0 dan boshlab",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("user/register/", RegisterView.as_view()),
    path("user/verify-email/", VerifyEmailView.as_view()),
    path("user/resend-code/", ResendCodeView.as_view()),
    path("user/login/", TokenObtainPairView.as_view()),
    path("user/refresh/", TokenRefreshView.as_view()),
    path("user/logout/", LogoutView.as_view()),
    path("user/me/", MeView.as_view()),
    path("forget/forgot-password/", ForgotPasswordView.as_view()),
    path("forget/confirm-password/", ConfirmPasswordView.as_view()),
    path("forget/reset-password/", ResetPasswordView.as_view()),

]