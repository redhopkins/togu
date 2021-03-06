from django.shortcuts import render
from tools import models

# Create your views here.
def index(request):
    all_menu_items = models.MenuItem.objects.order_by('position')
    all_containers = models.Container.objects.order_by('position')
    content = models.IndexContent.objects.all()
    context = {'menuitems': all_menu_items, 'containers': all_containers, 'indexcontents': content}
    return render(request, 'tools/index.html', context)

def contacts(request):
    all_menu_items = models.MenuItem.objects.order_by('position')
    coordinates = models.Contact.objects.all()
    context = {'menuitems': all_menu_items, 'contacts': coordinates}
    return render(request, 'tools/contacts.html', context)

def gallery(request):
    all_menu_items = models.MenuItem.objects.order_by('position')
    tool_list_item = models.ToolListItem.objects.order_by('position')
    all_tools = models.ScissorTool.objects.all()
    #scissors_params = models.ScissorsParam.objects.all()
    context = {'menuitems': all_menu_items, 'toollistitems': tool_list_item, 'tools': all_tools} #, 'scissorsparams': scissors_params}
    return render(request, 'tools/gallery.html', context)

def about(request):
    return render(request, 'tools/contacts.html')

def services(request):
    return render(request, 'tools/contacts.html')

def news(request):
    all_menu_items = models.MenuItem.objects.order_by('position')
    all_news = models.NewsItem.objects.order_by('pub_date')
    context = {'menuitems': all_menu_items, 'news': all_news}
    return render(request, 'tools/news.html', context)

def page(request):
    all_menu_items = models.MenuItem.objects.order_by('position')
    context = {'menuitems': all_menu_items}
    return render(request, 'tools/page.html', context)
