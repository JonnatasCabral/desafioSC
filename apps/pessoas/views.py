from rest_framework import generics
from .models import Endereco, Pessoa, Divida
from .serializers import (EnderecoSerializer, PessoaSerializer,
DividaSerializer)

class PessoaRetrieveAPIView(generics.RetrieveAPIView):

    lookup_field = 'cpf'

    def get(self, request, cpf):
        pessoa = Pessoa.objects.get(cpf=cpf)
        endereco = Endereco.objects.filter(pessoa_endereco__cpf=cpf)
        dividas = Divida.objects.filter(pessoa=pessoa)
        dados_pessoa = {
            'nome': pessoa.nome,
            'cpf': pessoa.cpf,
            'endereco': EnderecoSerializer(endereco, many=True).data,
            'dividas': DividaSerializer(dividas, many=True).data,
        }
        return Response(dados_pessoa)