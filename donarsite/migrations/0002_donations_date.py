# Generated by Django 2.1.7 on 2019-03-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donarsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
