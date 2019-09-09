# Generated by Django 2.1.7 on 2019-04-11 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ngo', '0003_auto_20190316_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='needs1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntype', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=10)),
                ('status', models.CharField(max_length=1)),
                ('nname', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]