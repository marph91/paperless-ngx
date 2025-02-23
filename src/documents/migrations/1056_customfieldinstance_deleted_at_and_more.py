# Generated by Django 5.1.2 on 2024-10-28 01:55

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1055_alter_storagepath_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="customfieldinstance",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customfieldinstance",
            name="restored_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customfieldinstance",
            name="transaction_id",
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="restored_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="transaction_id",
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sharelink",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sharelink",
            name="restored_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sharelink",
            name="transaction_id",
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
