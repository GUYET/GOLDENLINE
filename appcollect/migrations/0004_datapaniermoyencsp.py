# Generated by Django 4.2.1 on 2023-05-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appcollect", "0003_datadepensecsp_delete_datacategorieprodcsp"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataPanierMoyenCsp",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "csp_name_id",
                    models.TextField(blank=True, db_collation="C", null=True),
                ),
                (
                    "panier_moyen",
                    models.TextField(blank=True, db_collation="C", null=True),
                ),
            ],
            options={
                "db_table": "depense_panier_moyen_csp",
                "managed": False,
            },
        ),
    ]
