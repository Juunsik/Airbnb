from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TrustMeBroAuthentication(BaseAuthentication):
    def authenticate(self, request):  # API request 가 있을 때마다 자동으로 호출
        username = request.headers.get("Trust-Me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # user 만 리턴이 아닌 (user, None)으로 리턴해야 한다.
        except User.DoesNotExist:
            raise AuthenticationFailed
