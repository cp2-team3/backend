# Generated by Django 4.1.5 on 2023-01-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(null=True, verbose_name='Birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', '남성'), ('Female', '여성')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
