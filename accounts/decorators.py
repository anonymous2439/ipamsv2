from django.shortcuts import redirect, render


def authorized_roles(roles=None):
    if roles is None:
        roles = []

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                for role in roles:
                    if str.lower(request.user.role.name) == str.lower(role):
                        return view_func(request, *args, **kwargs)
                return render(request, 'accounts/unauthorized_user.html')
            return redirect('/')
        return wrapper_func
    return decorator
