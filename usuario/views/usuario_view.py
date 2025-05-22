from rest_framework.views import APIView
from rest_framework.response import Response
from usuario.models import Usuario
from usuario.serializers.usuario_serializer import UsuarioSerializer

class UsuarioView(APIView):
    def get(self, request, pk=None):
        if pk:
            usuario = Usuario.objects.get(id = pk)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.error_messages)