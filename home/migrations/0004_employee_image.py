# Generated by Django 2.2.3 on 2019-07-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=None, upload_to='pics'),
        ),
    ]