from rest_framework import serializers
from .models import Endereco, Pessoa, Divida


class EnderecoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Endereco
        fields = '__all__'


class PessoaSerializer(serializers.ModelSerializer):

    endereco = serializers.StringRelatedField()
    
    class Meta:
        model = Pessoa
        fields = '__all__'

class DividaSerializer(serializers.ModelSerializer):

    pessoa = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Divida
        fields = '__all__'
