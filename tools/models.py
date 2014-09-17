from django.db import models

# Create your models here.

class ToolListItem(models.Model):
    name = models.CharField(max_length=200)
    position = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name

class Tool(models.Model):
    tool_list_item = models.ForeignKey(ToolListItem)
    tool_name = models.CharField(max_length=200)
    tool_image = models.ImageField(upload_to='upload')
    tool_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return u'%s' % self.tool_name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    dest = models.CharField(max_length=200, default="/")
    position = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name

class Container(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload')
    dest = models.CharField(max_length=200, default="/")
    position = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name

class NewsItem(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s' % self.name

class IndexContent(models.Model):
    content = models.TextField()

class ScissorsParam(models.Model):
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    length = models.IntegerField()
    feature = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s' % self.name

class Contact(models.Model):
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    metro = models.CharField(max_length=200)
