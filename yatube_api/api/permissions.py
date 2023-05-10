from rest_framework import permissions


class IsAuthorOrAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (request.method in permissions.SAFE_METHODS
                    or request.user.is_authenticated)
        return obj.author == request.user

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
