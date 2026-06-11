import jwt
import time
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from config import chatapp_secrets

class RealtimeTokenView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        now = int(time.time())
        
        payload = {
            "sub": str(request.user.id),
            "role": "authenticated",
            "iat": now,
            "exp": now + 3600,
            "aud": "authenticated",
        }
        
        token = jwt.encode(payload, chatapp_secrets.DB_JWT, algorithm="HS256")
        
        return Response({"token": token})