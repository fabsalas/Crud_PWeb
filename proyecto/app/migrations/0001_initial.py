# Generated by Django 3.2.3 on 2021-07-08 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=99)),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sistema')),
            ],
        ),
    ]
