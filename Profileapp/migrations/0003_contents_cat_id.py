# Generated by Django 4.1.2 on 2023-02-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profileapp', '0002_categories_contents_cont_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='cat_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Profileapp.categories'),
        ),
    ]
