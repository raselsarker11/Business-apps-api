from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # authenticated rai parbay.
        if request.user and request.user.is_authenticated:
            return obj.user == request.user or request.user.is_admin
        
        return False

