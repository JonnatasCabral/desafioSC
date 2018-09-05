from django.db import models


class Endereco(models.Model):

    rua = models.CharField('Rua', max_length=100)
    numero = models.IntegerField('Numero')
    cep = models.CharField('CEP', max_length=10)
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('UF', max_length=2)

    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"
    

class Pessoa(models.Model):

    nome = models.CharField('Nome', max_length=255)
    cpf = models.IntegerField('CPF', primary_key=True)
    endereco = models.ForeignKey(
            Endereco,
            on_delete=models.CASCADE,
            related_name="pessoa",
            verbose_name='Endereço'
        )
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome
    

class Divida(models.Model):
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    descricao = models.TextField('Descrição', max_length=100)
    empresa = models.CharField('Empresa', max_length=100)
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name="dividas",
        verbose_name='pessoa'
    )
    class Meta:
        verbose_name = "Divida"
        verbose_name_plural = "Dividas"

    def __str__(self):
        return '{0} - {1}'.format(self.empresa, self.valor)
