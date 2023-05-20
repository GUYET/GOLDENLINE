from django.contrib import admin
from .models import RequeteCollecte


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


admin.site.register(RequeteCollecte, RequeteCollecteAdmin)
