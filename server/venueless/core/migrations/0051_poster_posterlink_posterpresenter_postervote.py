# Generated by Django 3.2.4 on 2021-10-16 14:00

import uuid

import django.db.models.deletion
from django.db import migrations, models

import venueless.core.models.poster


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0050_auto_20210826_1050"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poster",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255, null=True)),
                (
                    "abstract",
                    models.JSONField(default=venueless.core.models.poster.default_text),
                ),
                (
                    "authors",
                    models.JSONField(default=venueless.core.models.poster.default_text),
                ),
                (
                    "tags",
                    models.JSONField(default=venueless.core.models.poster.default_text),
                ),
                ("category", models.CharField(blank=True, max_length=50, null=True)),
                ("poster_url", models.URLField(blank=True, null=True)),
                ("poster_preview", models.URLField(blank=True, null=True)),
                (
                    "schedule_session",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "chat_room",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="chat_posters",
                        to="core.room",
                    ),
                ),
                (
                    "parent_room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_posters",
                        to="core.room",
                    ),
                ),
                (
                    "presentation_room",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="presentation_posters",
                        to="core.room",
                    ),
                ),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posters",
                        to="core.world",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PosterLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("display_text", models.CharField(max_length=300)),
                ("url", models.URLField()),
                ("sorting_priority", models.IntegerField(default=0)),
                (
                    "poster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="core.poster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PosterVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "poster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="core.poster",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="poster_votes",
                        to="core.user",
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "poster")},
            },
        ),
        migrations.CreateModel(
            name="PosterPresenter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "poster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="presenters",
                        to="core.poster",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="poster_presenter",
                        to="core.user",
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "poster")},
            },
        ),
    ]
