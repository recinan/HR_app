from rest_framework.permissions import BasePermission
from .models import Application

class IsCandidateOrEvaluator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        role = str(request.user.user_role)
        if role == 'Evaluator':
            return True
        if role == 'Candidate':
            return obj.user == request.user
        return False