# Generated by Django 2.0 on 2019-09-20 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fristname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('qualifiction', models.CharField(blank=True, max_length=20)),
                ('speciality', models.CharField(max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('clinic', models.CharField(blank=True, max_length=20)),
                ('adress', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=20)),
                ('birthdate', models.DateField()),
                ('about_doc', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fristname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('clinic', models.CharField(blank=True, max_length=20)),
                ('adress', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=20)),
                ('birthdate', models.DateField()),
                ('blood_group', models.CharField(blank=True, max_length=20)),
                ('blood_pressure', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('roal', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]
