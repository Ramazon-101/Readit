# Generated by Django 4.0.5 on 2022-06-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readit_app', '0006_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]