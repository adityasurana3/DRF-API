from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAllowedToEditTaskListElseNone(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by