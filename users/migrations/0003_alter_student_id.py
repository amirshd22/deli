# Generated by Django 3.2.3 on 2021-09-04 16:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_student_onlineclasses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
