# Generated by Django 4.1.1 on 2022-11-21 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("groups", "0025_delete_invitation"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Invitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pub_id",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=255,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, db_index=True, null=True),
                ),
                (
                    "from_who",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitation_from",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "to_a_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="groups.group"
                    ),
                ),
                (
                    "to_who",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitation_to",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
