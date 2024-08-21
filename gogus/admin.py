from django.contrib import admin
from .models import PessoaFisica, PessoaJuridica, Endereco, Telefone

# Register your models here.
class PessoaFis(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sexo', 'genero', 'cpf', 'data_nascimento', 'email')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = tuple('nome',)

admin.site.register(PessoaFisica, PessoaFis)

class PessoaJur(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'nome_fantasia', 'cnpj', 'status', 'contato')
    list_display_links = ('id', 'nome_fantasia')
    list_per_page = 20
    search_fields = tuple('nome_fantasia')

admin.site.register(PessoaJuridica, PessoaJur)

class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'logradouro', 'numero', 'bairro', 'municipio', 'estado', 'cep')
    list_display_links = ('id', 'logradouro')
    list_per_page = 20
    search_fields = tuple('logradouro')

admin.site.register(Endereco, Enderecos)

class Telefones(admin.ModelAdmin):
    list_display = ('id', 'nr_tel', 'tipo_tel')
    list_display_links = ('id', 'nr_tel')
    list_per_page = 20
    search_fields = tuple('nr_tel')

admin.site.register(Telefone, Telefones)
