from rest_framework.permissions import BasePermission
from .models import Application

class IsCandidateOrEvaluator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Evaulator':
            return True
        if request.user.role == 'Candidate':
            return obj.user == request.user
        return False