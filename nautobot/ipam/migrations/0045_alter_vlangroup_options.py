# Generated by Django 3.2.24 on 2024-02-14 14:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0044_ip_version_nonnullable"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vlangroup",
            options={"ordering": ("name",), "verbose_name": "VLAN group", "verbose_name_plural": "VLAN groups"},
        ),
    ]
