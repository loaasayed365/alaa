# Generated by Django 5.0.3 on 2024-03-20 18:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField(max_length=11)),
                ('billing_address', models.CharField(max_length=250)),
                ('is_closed', models.BooleanField(default=False)),
                ('open', models.DateField(auto_now_add=True)),
                ('closed', models.DateField(auto_now=True)),
                ('new', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('blocked', models.BooleanField(default=False)),
                ('banned', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
