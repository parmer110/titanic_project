# Generated by Django 5.1 on 2024-08-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TitanicPassenger',
            fields=[
                ('passenger_id', models.IntegerField(primary_key=True, serialize=False)),
                ('survived', models.BooleanField()),
                ('pclass', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.FloatField(blank=True, null=True)),
                ('sibsp', models.IntegerField()),
                ('parch', models.IntegerField()),
                ('ticket', models.CharField(max_length=20)),
                ('fare', models.FloatField()),
                ('cabin', models.CharField(blank=True, max_length=20, null=True)),
                ('embarked', models.CharField(max_length=1)),
            ],
        ),
    ]
