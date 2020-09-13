# Generated by Django 3.1.1 on 2020-09-12 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20200911_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='amount_of_upvotes',
        ),
        migrations.RemoveField(
            model_name='news',
            name='upvoated',
        ),
        migrations.AddField(
            model_name='news',
            name='upvoted',
            field=models.ManyToManyField(related_name='news_upvoted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='creation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
