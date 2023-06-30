from django.contrib import admin

from main.models import IHA, Category, RentalRecord


# Register your models here.
@admin.register(IHA)
class IhaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)
admin.site.register(RentalRecord)
