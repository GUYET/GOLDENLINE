# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


# Création de la table RequeteAnonymisees
class RequeteAnonymisees(models.Model):
    id = models.AutoField(primary_key=True)
    id_customer = models.BigIntegerField()
    child_number = models.IntegerField(blank=True, null=True)
    csp_name_id = models.TextField(
        max_length="250", db_collation="C", blank=True, null=True
    )
    purchase_amount = models.DecimalField(decimal_places=2, max_digits=8)
    purchase_date = models.DateField(blank=True, null=True)
    nb_collect_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "requete_anonymisees"


# Création de la table RequeteCollecte
class RequeteCollecte(models.Model):
    id = models.AutoField(primary_key=True)
    nb_collect_id = models.BigIntegerField(blank=True, null=True)
    purchase_amount = models.DecimalField(decimal_places=2, max_digits=8)
    product_category_name_id = models.TextField(
        max_length="250", db_collation="C", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "requete_collecte"


# Création de la table DataDepenseCsp
class DataDepenseCsp(models.Model):
    id = models.AutoField(primary_key=True)
    csp_name_id = models.TextField(
        max_length="250", db_collation="C", blank=True, null=True
    )
    purchase_amount = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        managed = False
        db_table = "depense_detail_csp"


# Création de la table DataDepenseTotalCsp
class DataDepenseTotalCsp(models.Model):
    id = models.AutoField(primary_key=True)
    csp_name_id = models.TextField(
        max_length="250", db_collation="C", blank=True, null=True
    )
    depense_csp = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        managed = False
        db_table = "depense_total_par_csp"


# Création de la table DataPanierMoyenCsp
class DataPanierMoyenCsp(models.Model):
    id = models.AutoField(primary_key=True)
    csp_name_id = models.TextField(
        max_length="250", db_collation="C", blank=True, null=True
    )
    moyenne_arrondie = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        managed = False
        db_table = "depense_moyen_par_csp"
