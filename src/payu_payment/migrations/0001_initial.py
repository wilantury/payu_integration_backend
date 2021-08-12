# Generated by Django 3.2.6 on 2021-08-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_code_pol', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('additional_value', models.FloatField(default=0.0)),
                ('test', models.SmallIntegerField(default=1)),
                ('transaction_date', models.DateTimeField()),
                ('cc_number', models.CharField(max_length=255)),
                ('cc_holder', models.CharField(max_length=100)),
                ('error_code_bank', models.CharField(max_length=255)),
                ('billing_country', models.CharField(max_length=4)),
                ('bank_referenced_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('value', models.FloatField(default=0.0)),
                ('payment_method_type', models.SmallIntegerField()),
                ('email_buyer', models.CharField(max_length=100)),
                ('response_message_pol', models.CharField(max_length=255)),
                ('error_message_bank', models.CharField(max_length=255)),
                ('shipping_city', models.CharField(max_length=55)),
                ('transaction_id', models.CharField(max_length=40)),
                ('sign', models.CharField(max_length=255)),
                ('tax', models.FloatField(default=0.0)),
                ('payment_method', models.SmallIntegerField()),
                ('billing_address', models.CharField(max_length=255)),
                ('payment_method_name', models.CharField(max_length=255)),
                ('pse_bank', models.CharField(max_length=255)),
                ('state_pol', models.SmallIntegerField()),
                ('date', models.DateTimeField()),
                ('nickname_buyer', models.CharField(max_length=255)),
                ('reference_pol', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=10)),
                ('risk', models.FloatField(default=0.0)),
                ('shipping_address', models.CharField(max_length=255)),
                ('bank_id', models.SmallIntegerField()),
                ('payment_request_state', models.CharField(max_length=32)),
                ('customer_number', models.IntegerField()),
                ('administrative_fee_base', models.FloatField()),
                ('attempts', models.IntegerField()),
                ('merchant_id', models.IntegerField()),
                ('exchange_rate', models.FloatField()),
                ('shipping_country', models.CharField(max_length=5)),
                ('installments_number', models.IntegerField()),
                ('franchise', models.CharField(max_length=50)),
                ('payment_method_id', models.SmallIntegerField()),
                ('nickname_seller', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=40)),
                ('billing_city', models.CharField(max_length=40)),
                ('reference_sale', models.DateTimeField()),
            ],
        ),
    ]
