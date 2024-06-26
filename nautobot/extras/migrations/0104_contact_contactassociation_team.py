# Generated by Django 3.2.23 on 2024-01-04 20:35

import uuid

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion

import nautobot.core.models.fields
import nautobot.extras.models.mixins
import nautobot.extras.models.roles
import nautobot.extras.models.statuses


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0103_add_db_indexes_to_object_change"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(db_index=True, max_length=100)),
                ("phone", models.CharField(blank=True, db_index=True, max_length=100)),
                ("email", models.EmailField(blank=True, db_index=True, max_length=254)),
                ("address", models.TextField(blank=True)),
                ("comments", models.TextField(blank=True)),
                ("tags", nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("name", "phone", "email")},
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(db_index=True, max_length=100)),
                ("phone", models.CharField(blank=True, db_index=True, max_length=100)),
                ("email", models.EmailField(blank=True, db_index=True, max_length=254)),
                ("address", models.TextField(blank=True)),
                ("comments", models.TextField(blank=True)),
                ("contacts", models.ManyToManyField(related_name="teams", to="extras.Contact")),
                ("tags", nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("name", "phone", "email")},
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="ContactAssociation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("associated_object_id", models.UUIDField(db_index=True)),
                (
                    "associated_object_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_associations",
                        to="extras.contact",
                    ),
                ),
                (
                    "role",
                    nautobot.extras.models.roles.RoleField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contact_associations",
                        to="extras.role",
                    ),
                ),
                (
                    "status",
                    nautobot.extras.models.statuses.StatusField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contact_associations",
                        to="extras.status",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_associations",
                        to="extras.team",
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("team", "associated_object_type", "associated_object_id", "role"),
                    ("contact", "associated_object_type", "associated_object_id", "role"),
                },
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
    ]
