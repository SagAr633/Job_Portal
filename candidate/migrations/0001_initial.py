# Generated by Django 4.0.3 on 2022-05-19 06:59

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
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_pic', models.ImageField(upload_to='pro_p')),
                ('qualification', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(default=18)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('cv', models.FileField(null=True, upload_to='cvs')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
