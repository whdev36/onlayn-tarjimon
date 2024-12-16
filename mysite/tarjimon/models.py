from django.db import models

# Lu'gat modelini yaratish

class Lugat(models.Model):
    class Meta:
        verbose_name = 'Lug\'at'
        verbose_name_plural = 'Lug\'atlar'
    ing = models.CharField('Inglizcha', max_length=255) # Inglizcha so'zlar
    uzb = models.CharField('O\'zbekcha', max_length=255) # O'zbekcha so'zlar

    def __str__(self):
        return f'{self.ing} - {self.uzb}'
