from django.contrib import admin
from main.models import Services

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["utility_type",]

    fields = [
        "account_number",
        "tariff",
        "meter_reading",
        "date",
        "total_cost",
        'user_id',
    ]
