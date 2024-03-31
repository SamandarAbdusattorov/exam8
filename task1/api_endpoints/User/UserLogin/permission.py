from rest_framework.permissions import BasePermission


class IsDeletedPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_deleted == False)

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
