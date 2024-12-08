# Generated by Django 5.1 on 2024-10-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_fooditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='category',
            field=models.CharField(choices=[('Fruit', 'Fruit'), ('Vegetable', 'Vegetable'), ('Meal', 'Meal'), ('Dairy', 'Dairy'), ('Other', 'Other')], default='Other', max_length=50),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]