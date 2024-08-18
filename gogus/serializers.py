from rest_framework import serializers
from .models import PessoaFisica, PessoaJuridica, Endereco, Telefone
from django.contrib.contenttypes.models import ContentType

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class BaseDadosPessoaisSecundariosSerializer(serializers.ModelSerializer):
    #endereco = serializers.PrimaryKeyRelatedField(queryset = Endereco.objects.all())
    #telefone = serializers.PrimaryKeyRelatedField(queryset = Telefone.objects.all())
    #pessoa
    telefone = TelefoneSerializer()
    endereco = EnderecoSerializer()

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        telefone_data = validated_data.pop('telefone')

        endereco = Endereco.objects.create(**endereco_data)

        dados = self.Meta.model.objects.create(endereco=endereco **validated_data)

        telefone = Telefone.objects.create(
            nr_tel = telefone_data['nr_tel'],
            tipo_tel = telefone_data['tipo_tel'],
            content_type = ContentType.objects.get_for_model(self.Meta.model),
            object_id = dados.id
        )

        return dados

class PessoaFisicaSerializer(serializers.ModelSerializer):
    class Meta(BaseDadosPessoaisSecundariosSerializer.Meta):
        model = PessoaFisica
        fields = '__all__'

class PessoaJuridicaSerializer(serializers.ModelSerializer):
    class Meta(BaseDadosPessoaisSecundariosSerializer.Meta):
        model = PessoaJuridica
        fields = '__all__'




