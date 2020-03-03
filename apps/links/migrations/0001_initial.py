# Generated by Django 3.0.3 on 2020-03-03 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=200, verbose_name='link')),
                ('status', models.IntegerField(verbose_name='status')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
        ),
    ]
