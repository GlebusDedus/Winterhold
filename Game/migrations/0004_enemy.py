# Generated by Django 4.0 on 2021-12-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0003_place_enemy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('damage', models.TextField()),
                ('hp', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
