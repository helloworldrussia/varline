# Generated by Django 4.0.1 on 2022-02-13 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0004_modalpage_alter_referral_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='token',
            field=models.UUIDField(default=uuid.UUID('4b107ec5-38fa-428a-b804-7a622f9956b0')),
        ),
    ]
