from django.contrib import admin
from tools import models

# Register your models here.

class ToolAdmin(admin.ModelAdmin):
    fields = ['tool_list_item', 'tool_name', 'tool_image', 'tool_price']

class ToolListItemAdmin(admin.ModelAdmin):
    fields = ['name', 'position']
    list_display = ('name', 'position')

admin.site.register(models.ToolListItem, ToolListItemAdmin)
admin.site.register(models.Tool, ToolAdmin)
admin.site.register(models.MenuItem)
admin.site.register(models.Container)