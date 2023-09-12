from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsHouseManagerOrNone(BasePermission):
    
    def has_permission(self, request, view):
        print(view)
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        print("object")
        print(view)
        print(obj)
        print(request.user)
        print(request.user.profile)
        if request.method in SAFE_METHODS:
            return True
        
        return request.user.profile == obj.manager
