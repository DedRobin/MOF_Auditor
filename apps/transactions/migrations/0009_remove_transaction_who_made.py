# Generated by Django 4.1.1 on 2022-11-07 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0008_alter_transactioncategory_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="who_made",
        ),
    ]