# Generated by Django 3.2.3 on 2021-09-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0002_alter_onlineclass_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineclass',
            name='students',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]