# Generated by Django 4.0.3 on 2022-04-14 15:07

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
            name='FileObject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('content_type', models.TextField(choices=[('pdf', 'pdf'), ('video', 'Video'), ('img', 'Bild'), ('file', 'Andere Datei')], default='file', max_length=5)),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmbededObject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.TextField()),
                ('content_type', models.TextField(choices=[('xlsx', 'Excel'), ('pptx', 'Powerpoint'), ('else', 'Sonstiges')], default='file', max_length=5)),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
