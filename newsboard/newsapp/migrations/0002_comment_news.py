# Generated by Django 3.1.1 on 2020-09-11 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newsapp.news'),
            preserve_default=False,
        ),
    ]
