# Generated by Django 5.0 on 2024-02-01 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("BookID", models.AutoField(primary_key=True, serialize=False)),
                ("Book_number", models.IntegerField()),
                ("Title", models.CharField(max_length=255)),
                ("ISBN", models.CharField(max_length=13, unique=True)),
                ("PublishedDate", models.DateField()),
                ("Genre", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Libary_user",
            fields=[
                ("UserID", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("MembershipDate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="BooksDetails",
            fields=[
                ("DetailsID", models.IntegerField(primary_key=True, serialize=False)),
                ("NumberOfPages", models.PositiveIntegerField()),
                ("Publisher", models.CharField(max_length=255)),
                ("Language", models.CharField(max_length=50)),
                (
                    "BookID",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="first_App.book"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BorrowedBooks",
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
                ("BorrowDate", models.DateField()),
                ("ReturnDate", models.DateField(blank=True, null=True)),
                (
                    "BookID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="first_App.book"
                    ),
                ),
                (
                    "UserID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="first_App.libary_user",
                    ),
                ),
            ],
        ),
    ]
