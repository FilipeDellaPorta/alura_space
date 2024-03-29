# Generated by Django 5.0.2 on 2024-02-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[(' ', ' '), ('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('PLANETA', 'Planeta'), ('GALÁXIA', 'Galáxia')], max_length=50),
        ),
    ]
