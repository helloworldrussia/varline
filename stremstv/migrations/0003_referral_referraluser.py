# Generated by Django 4.0.1 on 2022-02-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stremstv', '0002_news_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('referral_id', models.BigIntegerField(unique=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('unique_users', models.IntegerField(default=0)),
                ('total_requests', models.IntegerField(default=0)),
                ('downloads', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_id', models.BigIntegerField()),
                ('referral_name', models.CharField(max_length=250)),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(max_length=255)),
                ('requests', models.IntegerField(default=0)),
                ('downloads', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
