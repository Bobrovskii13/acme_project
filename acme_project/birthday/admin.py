from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = '<i><b>Не задано</b></i>'


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'
    )


admin.site.register(Birthday, BirthdayAdmin)

admin.site.register(Tag)
