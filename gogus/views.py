from rest_framework import viewsets
from .serializers import PessoaFisicaSerializer, PessoaJuridicaSerializer, EnderecoSerializer, TelefoneSerializer
from .models import PessoaFisica, PessoaJuridica, Endereco, Telefone

# comentários adicionados em teste

class PessoaFisicaViewSet(viewsets.ModelViewSet):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer

class PessoaJuridicaViewSet(viewsets.ModelViewSet):
    queryset = PessoaJuridica.objects.all()
    serializer_class = PessoaJuridicaSerializer

class TelefoneSerializer(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Telefone.objects.filter(object_id = self.kwargs['pk'])
        return queryset
    serializer_class = TelefoneSerializer

class EnderecoSerializer(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Endereco.objects.filter(id = self.kwargs['pk'])
        return queryset
    serializer_class = EnderecoSerializer
