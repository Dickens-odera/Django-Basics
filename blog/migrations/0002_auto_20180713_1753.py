# Generated by Django 2.0.7 on 2018-07-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogposts',
            options={'verbose_name_plural': 'BlogPosts'},
        ),
        migrations.AlterField(
            model_name='blogposts',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
