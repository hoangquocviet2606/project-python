# Generated by Django 3.2.1 on 2021-05-28 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0002_employee_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(default=1000, primary_key=True, serialize=False),
        ),
    ]
