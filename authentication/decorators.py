from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def client_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login_client'):
    
    # Decorator for views that checks that the logged in user is a client,
    # redirects to the log-in page if necessary.
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_client,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def freelancer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login_freelancer'):
    
    # Decorator for views that checks that the logged in user is a teacher,
    # redirects to the log-in page if necessary.
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_freelancer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
