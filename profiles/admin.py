from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "first_name", "last_name", "created_at")
    fields = ("user", "gender", "first_name", "last_name")
    list_filter = ("gender",)
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "first_name", "last_name", "gender", "created_at")
