from django.contrib import admin
from tools import models

# Register your models here.

#class ToolAdmin(admin.ModelAdmin):
#    fields = ['tool_list_item', 'tool_name', 'tool_image', 'tool_price']

class ToolListItemAdmin(admin.ModelAdmin):
    fields = ['name', 'position']
    list_display = ('name', 'position')

admin.site.register(models.ToolListItem, ToolListItemAdmin)
admin.site.register(models.ScissorTool)
admin.site.register(models.PusherTool)
admin.site.register(models.TweezersTool)
admin.site.register(models.ClipperTool)
admin.site.register(models.MenuItem)
admin.site.register(models.Container)
admin.site.register(models.NewsItem)
admin.site.register(models.IndexContent)
admin.site.register(models.Contact)
