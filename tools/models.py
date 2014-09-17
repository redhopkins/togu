#encoding: utf-8

from django.db import models

# Create your models here.

class ToolListItem(models.Model):
    name = models.CharField(max_length=200)
    position = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name

class ScissorTool(models.Model):
    list_item = models.ForeignKey(ToolListItem)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Параметры специфичные для ножниц
    material = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    length = models.IntegerField()
    feature = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s' % self.name

class ClipperTool(models.Model):
    list_item = models.ForeignKey(ToolListItem)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Параметры специфичные для кусачек
    material = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    length = models.IntegerField()
    feature = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s' % self.name

class PusherTool(models.Model):
    list_item = models.ForeignKey(ToolListItem)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Параметры специфичные для пушеров
    material = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    length = models.IntegerField()
    feature = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s' % self.name

class TweezersTool(models.Model):
    list_item = models.ForeignKey(ToolListItem)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Параметры специфичные для пинцетов
    material = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    length = models.IntegerField()
    feature = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s' % self.name

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

class Contact(models.Model):
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    metro = models.CharField(max_length=200)
