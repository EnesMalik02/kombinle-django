# Generated by Django 5.1.1 on 2024-10-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_datas', '0002_userprofile_delete_dummymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Ülke')),
                ('gender', models.CharField(max_length=10, verbose_name='Cinsiyet')),
                ('age', models.PositiveIntegerField(verbose_name='Yaş')),
                ('search_term', models.CharField(max_length=100, verbose_name='Arama Kelimesi')),
                ('main_word', models.CharField(max_length=100, verbose_name='Ana Kelime')),
                ('color', models.CharField(max_length=50, verbose_name='Renk')),
                ('height', models.PositiveIntegerField(verbose_name='Boy (cm)')),
                ('weight', models.PositiveIntegerField(verbose_name='Kilo (kg)')),
                ('waist', models.PositiveIntegerField(verbose_name='Bel (cm)')),
                ('chest', models.PositiveIntegerField(verbose_name='Göğüs (cm)')),
                ('hip', models.PositiveIntegerField(verbose_name='Kalça Çevresi (cm)')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
