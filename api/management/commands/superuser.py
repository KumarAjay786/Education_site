from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a superuser for the custom user model.'

    def handle(self, *args, **options):
        User = get_user_model()
        # Hardcoded credentials
        email = 'info@pragathiedu.com'
        password = 'Pragathi@2020'
        name = 'Admin User'
        username = email  # Ensure username is set for default Django user model

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR(
                f"Superuser with email {email} already exists."))
            return

        # Try to create superuser with username, email, password, and name
        try:
            user = User.objects.create_superuser(
                username=username, email=email, password=password, name=name)
        except TypeError:
            # Fallback for user models that don't have 'name' field
            user = User.objects.create_superuser(
                username=username, email=email, password=password)
        user.is_active = True
        user.save()
        self.stdout.write(self.style.SUCCESS(
            f"Superuser created with email: {email} and username: {username}"))
