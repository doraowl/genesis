# Generated by Django 3.0.7 on 2020-06-17 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200614_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_text', models.TextField(default='')),
                ('lemma', models.TextField(default='')),
                ('pos', models.TextField(default='')),
                ('position', models.IntegerField(default=-1)),
                ('sentence', models.IntegerField(default=-1)),
                ('text', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Text')),
            ],
        ),
    ]
