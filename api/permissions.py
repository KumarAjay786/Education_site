from rest_framework.permissions import BasePermission


class IsAdminEmail(BasePermission):
    """
    Allows access only to the specified admin email.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.email == 'info@pragathiedu.com')
