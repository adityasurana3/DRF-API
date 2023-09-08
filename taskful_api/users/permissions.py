from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsUserOwnerOrGetAndPostOnly(BasePermission):

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        
        return False
    
class IsProfileOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user.profile == obj
        
        return False
                