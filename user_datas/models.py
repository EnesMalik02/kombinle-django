# myapp/models.py
from django.db import models

class ClothingSearch(models.Model):
    country = models.CharField(max_length=100, verbose_name='Ülke')
    gender = models.CharField(max_length=10, verbose_name='Cinsiyet')
    age = models.PositiveIntegerField(verbose_name='Yaş')
    search_term = models.CharField(max_length=100, verbose_name='Arama Kelimesi')
    main_word = models.CharField(max_length=100, verbose_name='Ana Kelime')
    color = models.CharField(max_length=50, verbose_name='Renk')
    height = models.PositiveIntegerField(verbose_name='Boy (cm)')
    weight = models.PositiveIntegerField(verbose_name='Kilo (kg)')
    waist = models.PositiveIntegerField(verbose_name='Bel (cm)')
    chest = models.PositiveIntegerField(verbose_name='Göğüs (cm)')
    hip = models.PositiveIntegerField(verbose_name='Kalça Çevresi (cm)')

    def __str__(self):
        return f"{self.search_term} - {self.gender}, {self.age} Yaş"
