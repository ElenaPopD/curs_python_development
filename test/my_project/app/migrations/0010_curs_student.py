# Generated by Django 5.0.1 on 2024-01-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_userprofile_cnp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('descriere', models.CharField(blank=True, default='No description provided', help_text='Intoduceti o descriere', max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('prenume', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cursuri', models.ManyToManyField(to='app.curs')),
            ],
        ),
    ]
