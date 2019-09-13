# Generated by Django 2.1.7 on 2019-03-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50, unique=True)),
                ('contact_email', models.CharField(max_length=50)),
                ('contact_telephone', models.CharField(max_length=50)),
                ('contact_address', models.CharField(max_length=38)),
                ('profession', models.CharField(max_length=50)),
                ('office_hours', models.CharField(max_length=200)),
                ('short_bio', models.TextField()),
                ('creation', models.DateTimeField(verbose_name="date d'ajout")),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('publication', models.DateTimeField(verbose_name="date d'ajout")),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=64, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('telephone', models.CharField(max_length=10, unique=True)),
                ('last_login', models.DateTimeField(verbose_name='dernière connexion')),
                ('creation', models.DateTimeField(verbose_name="date d'ajout")),
            ],
        ),
    ]