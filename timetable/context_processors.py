from timeline.models import User


def auth(request):
    """
    Returns context variables required by apps that use Django's authentication
    system.

    If there is no 'user' attribute in the request, uses AnonymousUser (from
    django.contrib.auth).
    """
    if hasattr(request, 'user'):
        try:
            user = User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            from django.contrib.auth.models import AnonymousUser
            user = AnonymousUser()
    return {
        'user': user,
    }
