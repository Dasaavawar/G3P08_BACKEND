from django.db import reset_queries
from rest_framework     import serializers, status, views
from rest_framework.response     import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from AuthAppEmpleados.serializers.usuarioSerializer import UsuarioSerilizer


class UsuarioCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializers = UsuarioSerilizer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        tokenData = {
            "username": request.data["username"],
            "password":request.data["password"]
        }
    
        try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
