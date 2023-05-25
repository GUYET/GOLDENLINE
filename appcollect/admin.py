from django.contrib import admin
from .models import (
    RequeteCollecte,
    RequeteAnonymisees,
    DataDepenseCsp,
    DataPanierCsp,
)


class RequeteCollecteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nb_collect_id",
        "purchase_amount",
        "product_category_name_id",
    )
    list_filter = (
        "id",
        "nb_collect_id",
        "purchase_amount",
        "product_category_name_id",
    )
    search_fields = (
        "id",
        "nb_collect_id",
        "purchase_amount",
        "product_category_name_id",
    )


class RequeteAnonymiseesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "id_customer",
        "child_number",
        "csp_name_id",
        "purchase_amount",
        "purchase_date",
        "nb_collect_id",
    )
    list_filter = (
        "id",
        "id_customer",
        "child_number",
        "csp_name_id",
        "purchase_amount",
        "purchase_date",
        "nb_collect_id",
    )
    search_fields = (
        "id",
        "id_customer",
        "child_number",
        "csp_name_id",
        "purchase_amount",
        "purchase_date",
        "nb_collect_id",
    )


class DataDepenseCspAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "csp_name_id",
        "purchase_amount",
    )
    list_filter = (
        "id",
        "csp_name_id",
        "purchase_amount",
    )
    search_fields = (
        "id",
        "csp_name_id",
        "purchase_amount",
    )


class DataPanierCspAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "csp_name_id",
        "panier_csp",
    )
    list_filter = (
        "id",
        "csp_name_id",
        "panier_csp",
    )
    search_fields = (
        "id",
        "csp_name_id",
        "panier_csp",
    )


admin.site.register(RequeteCollecte, RequeteCollecteAdmin)
admin.site.register(RequeteAnonymisees, RequeteAnonymiseesAdmin)
admin.site.register(DataDepenseCsp, DataDepenseCspAdmin)
admin.site.register(DataPanierCsp, DataPanierCspAdmin)
