from django.shortcuts import render
from tools import models

# Create your views here.
def index(request):
	all_menu_items = models.MenuItem.objects.order_by('position')
	all_containers = models.Container.objects.order_by('position')
	context = {'menuitems': all_menu_items, 'containers': all_containers}
	return render(request, 'tools/index.html', context)
    
def contacts(request):
    all_menu_items = models.MenuItem.objects.order_by('position')
    context = {'menuitems': all_menu_items}
    return render(request, 'tools/contacts.html', context)

def gallery(request):
	all_menu_items = models.MenuItem.objects.order_by('position')
	tool_list_item = models.ToolListItem.objects.order_by('position')
	all_tools = models.Tool.objects.all()
	context = {'menuitems': all_menu_items, 'toollistitems': tool_list_item, 'tools': all_tools}
	return render(request, 'tools/gallery.html', context)
