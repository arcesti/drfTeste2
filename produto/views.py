from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer

class ProdutoView(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                produto = Produto.objects.get(id = pk)
                serializer = ProdutoSerializer(produto)
                return Response(serializer.data, status=200)
            
            except Produto.DoesNotExist:
                return Response({ "message": "Produto não encontrado" },status=404)
            
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = ProdutoSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.error_messages, status=400)
    
    def put(self, request, pk = None):
        if not pk:
            return Response({ "message": "Parametro inválido!" }, status=400)
        
        try:
            produto_existente = Produto.objects.get(id = pk)
            
        except Produto.DoesNotExist:
            return Response({ "message": "Produto não encontrado!" },status=404)
        
        produto = ProdutoSerializer(instance = produto_existente, data = request.data)
        
        if produto.is_valid():
            produto.save()
            return Response({ "message": "Produto atualizado com sucesso.", "produto": produto.data }, status=200)
        
        return Response({ "message": "erro ao atualizar produto" }, status=500)
    
    def delete(self, request, pk = None):
        if not pk:
            return Response({ "message": "Parametro inválido!" }, status=400)
        
        try:
            produto = Produto.objects.get(id = pk)
            produto.delete()
            return Response({ "message": "Produto deletado com sucesso!" }, status=200)
        
        except Produto.DoesNotExist:
            return Response({ "message":"Não foi possível concluir a exclusão, produto não encontrado" }, status=404)
        
        except Exception as e:
            return Response({ "message": "erro interno ao tentar excluir item", "erro": str(e) }, status=500)