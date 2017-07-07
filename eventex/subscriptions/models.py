from django.db import models
import uuid


class Subscription(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4().hex, editable=False)
    name = models.CharField(max_length=100, verbose_name='nome')
    cpf = models.CharField(max_length=11, verbose_name='cpf')
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name='telefone')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    paid = models.BooleanField(default=False, verbose_name="Pago")

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name