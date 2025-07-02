from rest_framework import serializers
from .models import AdmissionForm, ContactMessage, CareerApplication, TuitionAdmission
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class AdmissionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionForm
        fields = '__all__'
        read_only_fields = ['id', 'created_at',
                            'updated_at']  # if your model has these


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        read_only_fields = ['id', 'submitted_at']  # adjust as per your model


class CareerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerApplication
        fields = '__all__'
        read_only_fields = ['id', 'submitted_at']  # adjust based on your model


class TuitionAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionAdmission
        fields = '__all__'
        read_only_fields = ['id', 'submitted_at']  # adjust as needed


# ✅ Login Serializer for Admin Authentication

# Login Serializer for Admin Authentication
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user and user.is_active and user.is_superuser:
            data['user'] = user
            return data
        raise serializers.ValidationError("Invalid email or password.")


# Forgot Password Serializer
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value, is_superuser=True).exists():
            raise serializers.ValidationError("No superuser with this email.")
        return value


# Reset Password Serializer
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=6)

    def validate(self, data):
        # Token validation will be handled in the view
        return data
