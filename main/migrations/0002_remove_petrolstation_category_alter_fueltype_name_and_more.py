# Generated by Django 5.0.6 on 2024-05-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petrolstation',
            name='category',
        ),
        migrations.AlterField(
            model_name='fueltype',
            name='name',
            field=models.CharField(choices=[('P', 'Petrol'), ('E', 'Electric'), ('G', 'Gas')], max_length=1, unique=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
