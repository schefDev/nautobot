# Generated by Django 3.2.24 on 2024-02-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tenancy", "0008_tagsfield"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tenant",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="tenant",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="tenantgroup",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="tenantgroup",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
