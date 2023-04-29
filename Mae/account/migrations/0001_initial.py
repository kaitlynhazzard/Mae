# Generated by Django 4.1.7 on 2023-04-29 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(choices=[('0', 'ALL'), ('1', 'CRIMINAL'), ('2', 'CIVIL')], default='0', max_length=1)),
                ('residence_state', models.CharField(max_length=2)),
                ('incident_state', models.CharField(max_length=2)),
                ('incident_description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
