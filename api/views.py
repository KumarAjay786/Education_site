from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import (
    ContactMessageSerializer, CareerApplicationSerializer,
    AdmissionFormSerializer, TuitionAdmissionSerializer,
    LoginSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
)
from .models import ContactMessage, CareerApplication, AdmissionForm, TuitionAdmission
from django.shortcuts import render
import os
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminEmail
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
# Admission Form API (POST only)
# --- Superuser Login View ---
from rest_framework.views import APIView


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({"message": "Login successful", "user_id": user.id, "email": user.email})
        return Response(serializer.errors, status=400)


# --- Forgot Password View ---
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = get_user_model().objects.get(email=email, is_superuser=True)
            token = default_token_generator.make_token(user)
            reset_url = f"https://pragathiedu.com/reset-password?email={email}&token={token}"
            send_mail(
                subject="Password Reset Request",
                message=f"Reset your password using this link: {reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            return Response({"message": "Password reset link sent to your email."})
        return Response(serializer.errors, status=400)


# --- Reset Password View ---
class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']
            try:
                user = get_user_model().objects.get(email=email, is_superuser=True)
            except Exception:
                return Response({"error": "Invalid email."}, status=400)
            if not default_token_generator.check_token(user, token):
                return Response({"error": "Invalid or expired token."}, status=400)
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successful."})
        return Response(serializer.errors, status=400)


# Admission Form API (POST only)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsAdminEmail])
def admission_form_api(request):
    data = request.data.copy()
    files = request.FILES.getlist('marksheet[]')
    file_paths = []

    for file in files:
        save_path = f'admission_uploads/{file.name}'
        full_path = os.path.join('media', save_path)
        with default_storage.open(full_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        file_paths.append(save_path)

    data['marksheet'] = file_paths
    serializer = AdmissionFormSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAuthenticated, IsAdminEmail]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Message submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CareerApplicationViewSet(viewsets.ModelViewSet):
    queryset = CareerApplication.objects.all()
    serializer_class = CareerApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminEmail]


class TuitionAdmissionViewSet(viewsets.ModelViewSet):
    queryset = TuitionAdmission.objects.all()
    serializer_class = TuitionAdmissionSerializer
    permission_classes = [IsAuthenticated, IsAdminEmail]


class AdmissionFormViewSet(viewsets.ModelViewSet):
    queryset = AdmissionForm.objects.all()
    serializer_class = AdmissionFormSerializer
    permission_classes = [IsAuthenticated, IsAdminEmail]


# Frontend Views (static page rendering)
def frontend(request):
    return render(request, 'index.html')


def frontend_page(request, page):
    safe_page = os.path.basename(page)

    if not safe_page or not all(c.isalnum() or c in ('-', '_') for c in safe_page.replace('.html', '')):
        raise Http404()

    if safe_page.endswith('.html'):
        safe_page = safe_page[:-5]

    static_exts = ('.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg',
                   '.ico', '.map', '.woff', '.woff2', '.ttf', '.eot', '.json')

    if any(safe_page.endswith(ext) for ext in static_exts):
        raise Http404()

    template_name = f"{safe_page}.html"
    return render(request, template_name)
