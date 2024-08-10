from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class TokenAuthentication(BaseAuthentication):
    """
    Requires a Authorization header with either formats: "Bearer <token>" / "Token <token>"
    Using Cookies also works: "token: <token>"
    You can also send the token in the query string (NOT RECOMMENDED): "?token=<token>"
    Token is handled on this order: Authorization header > Cookie > QueryString
    """

    def authenticate(self, request):
        if (token := request.COOKIES.get("token")) is None:
            if (token := request.GET.get("token")) is None:
                return None
        elif (auth_header := request.META.get("HTTP_AUTHORIZATION")):
            auth_type, _, token = auth_header.partition(' ')
            if auth_type not in ["Token", "Bearer"]:
                return None
        try:
            user = USER_MODEL.objects.get(id=token)
            return (user, user.id)
        except Exception:
            return None
