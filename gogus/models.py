from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Endereco(models.Model):
    ESTADO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso Do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio De Janeiro'),
        ('RN', 'Rio Grande Do Norte'),
        ('RS', 'Rio Grande Do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    logradouro = models.CharField(max_length = 60)
    numero = models.CharField(max_length = 6)
    bairro = models.CharField(max_length = 60)
    municipio = models.CharField(max_length = 60)
    estado = models.CharField(max_length = 2, choices = ESTADO)
    cep = models.CharField(max_length = 8)
    complemento = models.CharField(max_length = 100)

class PessoaFisica(models.Model):
    GENERO = (
        ('HC', 'Homem cis'),
        ('HT', 'Homem Trans'),
        ('MC', 'Mulher cis'),
        ('MT', 'Mulher trans'),
        ('AS', 'Assexual'),
        ('IS', 'Intersex'),
    )
    SEXO = (
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
    )
    nome = models.CharField(max_length = 100, null = False, blank = False)
    email = models.EmailField(max_length = 100)
    cpf = models.CharField(max_length = 11, null = False, blank = False)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length = 2, choices = GENERO, blank = False, null = False)
    sexo = models.CharField(max_length = 2, choices = SEXO, blank = False, null = False)
    endereco = models.OneToOneField(Endereco, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nome}'

class PessoaJuridica(models.Model):
    STATUS = (
        ('A', 'ATIVO'),
        ('I', 'INATIVO'),
    )
    CONTRIBUINTE = (
        ('S', 'SIM'),
        ('N', 'NAO'),
    )
    razao_social = models.CharField(max_length = 120, null = False, blank = False)
    nome_fantasia = models.EmailField(max_length = 100)
    cnpj = models.CharField(max_length = 11, null = False, blank = False)
    inscricao_estadual = models.CharField(max_length = 9)
    inscricao_municipal = models.CharField(max_length = 11)
    contribuinte = models.CharField(choices = CONTRIBUINTE, max_length = 1)
    status = models.CharField(choices = STATUS, max_length = 1)
    contato = models.CharField(max_length = 100)
    endereco = models.OneToOneField(Endereco, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nome_fantasia}'


class Telefone(models.Model):
    TIPO = (
        ('MOVEL', 'MOVEL'),
        ('FIXO', 'FIXO'),
    )
    nr_tel = models.CharField(max_length = 14, null = False, blank = False, default = '+5527999999999')
    tipo_tel = models.CharField(max_length = 5, choices = TIPO, blank = False, null = False, default = 'MOVEL')

    # início da solução que implementa chave estrangeira genérica a fim
    # de compatibilizar a receber telefone de pessoa física e pessoa jurídica
    #pessoa_fisica = apps.get_model('gogus', 'PessoaFisica')
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, null = True, blank = True)
    object_id = models.PositiveIntegerField(null = True, blank = True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.nr_tel ({self.tipo_tel})}'


