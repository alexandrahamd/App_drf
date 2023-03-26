# Generated by Django 4.1.7 on 2023-03-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_of_change',
            field=models.DateField(blank=True, null=True, verbose_name='дата изменения'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_of_creation',
            field=models.DateField(auto_created=True, blank=True, null=True, verbose_name='дата создания'),
        ),
    ]
