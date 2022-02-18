# Generated by Django 4.0.1 on 2022-02-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apk_file', models.FileField(upload_to='apk/')),
                ('downloads', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'apk',
                'verbose_name_plural': 'apk',
            },
        ),
    ]
