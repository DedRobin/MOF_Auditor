# Generated by Django 4.1.1 on 2022-12-14 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("balances", "0006_balancecurrency_rate_balancecurrency_updated_at"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BalanceCurrency",
            new_name="Currency",
        ),
    ]
