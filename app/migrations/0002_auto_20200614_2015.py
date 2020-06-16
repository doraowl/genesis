# Generated by Django 3.0.7 on 2020-06-14 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('question', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='text',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='text',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('text', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Text')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField(default='')),
                ('test', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Test')),
                ('theme', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Theme')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='')),
                ('correctness', models.BooleanField(default=False)),
                ('task', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Task')),
            ],
        ),
    ]
