from django.urls import path, re_path
from .views import (
    frontend,
    frontend_page,
    admission_form_api,
    ContactMessageViewSet,
    CareerApplicationViewSet,
    TuitionAdmissionViewSet,
    AdmissionFormViewSet,  # <-- add this import
    LoginView,
    ForgotPasswordView,
    ResetPasswordView,
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenRefreshView
from .jwt_superuser import SuperuserTokenObtainPairView

urlpatterns = [
    # Auth
    path('api/login/', csrf_exempt(LoginView.as_view()), name='login'),
    path('api/forgot-password/',
         csrf_exempt(ForgotPasswordView.as_view()), name='forgot_password'),
    path('api/reset-password/', csrf_exempt(ResetPasswordView.as_view()),
         name='reset_password'),

    # JWT Auth
    path('api/token/', csrf_exempt(SuperuserTokenObtainPairView.as_view()),
         name='token_obtain_pair'),
    path('api/token/refresh/', csrf_exempt(TokenRefreshView.as_view()),
         name='token_refresh'),

    # API endpoints
    path('api/admissions/', csrf_exempt(AdmissionFormViewSet.as_view(
        {'get': 'list', 'post': 'create'})), name='admission_form_api'),
    path('api/contact/', csrf_exempt(ContactMessageViewSet.as_view(
        {'get': 'list', 'post': 'create'})), name='contact_message_api'),
    path('api/careers/', csrf_exempt(CareerApplicationViewSet.as_view(
        {'get': 'list', 'post': 'create'})), name='career_application_api'),
    path('api/tuition-admissions/', csrf_exempt(TuitionAdmissionViewSet.as_view(
        {'get': 'list', 'post': 'create'})), name='tuition_admission_api'),

    path('api/admissions/<int:pk>/', csrf_exempt(AdmissionFormViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})), name='admission_detail_api'),
    path('api/contact/<int:pk>/', csrf_exempt(ContactMessageViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})), name='contact_detail_api'),
    path('api/careers/<int:pk>/', csrf_exempt(CareerApplicationViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})), name='career_detail_api'),
    path('api/tuition-admissions/<int:pk>/', csrf_exempt(TuitionAdmissionViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})), name='tuition_detail_api'),

    # Frontend routing
    path('', frontend, name='frontend'),
    re_path(r'^(?P<page>[\w\-/]+?)(?:\.html)?/?$',
            frontend_page, name='frontend_page'),
]
