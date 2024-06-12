from django.contrib import admin
from myprofile.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "surname",]
    search_fields = ["user", "name","surname",]
    fields = [
        "surname",
        "name",
        "patronymic",
        "email",
        "avatar",
        'birth_date',
        'phone',
        'city',
        ('street', 'house_number','apartment_number'),
    ]
    #inlines = [CartTabAdmin, OrderTabulareAdmin]