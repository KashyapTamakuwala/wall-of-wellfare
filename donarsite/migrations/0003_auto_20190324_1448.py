# Generated by Django 2.1.7 on 2019-03-24 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donarsite', '0002_donations_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='pendingdonations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(max_length=20)),
                ('nmame', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('dname', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='donations',
            new_name='accepteddonations',
        ),
    ]