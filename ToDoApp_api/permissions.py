from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnTask(permissions.BasePermission):
    """allow user to edit their own tasks """

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own task"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id
