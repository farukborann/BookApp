from rest_framework import permissions

class HasSaleAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if(not super().has_permission()):
            return False
        
        if(request.user and request.user.is_staff):
            return True
        
        if request.method in permissions.SAFE_METHODS and obj.author == request.user.author:
            return True
        
        if obj.publisher == request.user.publisher:
            return True
        
        return False
    
class HasBookAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if(not super().has_permission(request, view)):
            return False
        
        if(request.user and request.user.is_staff):
            return True
        
        if hasattr(request.user, 'publisher') and obj.publisher == request.user.publisher:
            return True
        
        if hasattr(request.user, 'author') and obj.authors.filter(id=request.user.author.id).exists():
            return True
        
        return False
    
class HasAuthorAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if(not super().has_permission()):
            return False
        
        if(request.user and request.user.is_staff):
            return True
        
        if obj == request.user:
            return True
        
        return False
    