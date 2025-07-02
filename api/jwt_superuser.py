from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed



class SuperuserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove username from required fields, add email
        self.fields.pop('username', None)
        self.fields['email'] = self.fields['email'] if 'email' in self.fields else self.fields['password'].__class__(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if not email or not password:
            raise AuthenticationFailed('Email and password are required.')
        # Authenticate using email as username
        attrs['username'] = email
        data = super().validate(attrs)
        if not self.user.is_superuser:
            raise AuthenticationFailed('Only superusers can obtain a token.')
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser
        return token


class SuperuserTokenObtainPairView(TokenObtainPairView):
    serializer_class = SuperuserTokenObtainPairSerializer
