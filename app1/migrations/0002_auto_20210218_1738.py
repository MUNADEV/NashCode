# Generated by Django 3.0.11 on 2021-02-18 20:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
