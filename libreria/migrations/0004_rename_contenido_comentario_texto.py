# Generated by Django 4.2 on 2023-04-05 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_remove_libro_description_libro_resena'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='contenido',
            new_name='texto',
        ),
    ]