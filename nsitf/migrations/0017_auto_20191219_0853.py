# Generated by Django 2.0.13 on 2019-12-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsitf', '0016_employees_employer_numb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_tasks',
            name='code',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
