# Generated by Django 3.2.6 on 2021-08-13 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu_payment', '0005_alter_logpurchase_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logpurchase',
            name='administrative_fee_base',
            field=models.FloatField(blank=True, null=True),
        ),
    ]