# Generated by Django 3.2 on 2022-12-23 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoryname',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='categoryname',
            new_name='category',
        ),
    ]
