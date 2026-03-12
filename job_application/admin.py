from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','occupation')
    search_fields = ('first_name','last_name','email','occupation')
    list_filter = ('first_name','last_name','email','occupation')
    ordering = ("first_name",)
    readonly_fields = ("occupation",)



# Register your models here.
admin.site.register(Form, FormAdmin)
