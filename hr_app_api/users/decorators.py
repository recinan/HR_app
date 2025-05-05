from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and request.user.user_role.role_name in role:
                return func(request, *args, **kwargs)
            return HttpResponseForbidden('Forbidden')
        return wrapper
    return decorator
