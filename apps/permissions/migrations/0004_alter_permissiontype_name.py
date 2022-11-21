# Generated by Django 4.1.1 on 2022-11-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0003_alter_permission_group_alter_permission_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permissiontype",
            name="name",
            field=models.CharField(
                choices=[
                    ("read", "Read"),
                    ("create", "Create"),
                    ("update", "Update"),
                    ("delete", "Delete"),
                ],
                db_index=True,
                max_length=255,
                unique=True,
            ),
        ),
    ]
