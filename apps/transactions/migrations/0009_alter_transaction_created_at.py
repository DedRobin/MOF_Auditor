# Generated by Django 4.1.1 on 2023-01-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0008_alter_transaction_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="created_at",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
