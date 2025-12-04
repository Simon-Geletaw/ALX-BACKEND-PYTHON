from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication if needed for extension.
    Currently identical to JWTAuthentication.
    """
    pass
