from rest_framework.permissions import BasePermission, SAFE_METHODS





# Here 'obj' is the particular model object. Example: 'IsAllowedToEditTaskListElseNone' is for TaskListViewset the object is Tasklist model as an object

class IsAllowedToEditTaskListElseNone(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by
    
class IsAllowedToEditTaskElseNone(BasePermission):
    
    def has_permission(self, request, view):

        if not request.user.is_anonymous:
            return request.user.profile.house != None
        
        return False
    
    def has_object_permission(self, request, view, obj):
        print(obj)
        return request.user.profile.house == obj.task_list.house
    
class IsAllowedToEditAttachmentElseNone(BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house != None
        
    def has_object_permission(self, request, view, obj):
        
        return request.user.profile.house == obj.task.task_list.house