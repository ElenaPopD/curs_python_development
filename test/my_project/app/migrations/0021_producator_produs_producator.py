# Generated by Django 5.0.1 on 2024-01-30 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='produs',
            name='producator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.producator'),
        ),
    ]