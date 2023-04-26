from django.db import models


class Category(models.Model):
     name = models.CharField(max_length=255, verbose_name='Nazwa kategorii')
     slug = models.SlugField(max_length=255, unique=True,verbose_name='Odnośnik')
     icon = models.ImageField(upload_to='icons', verbose_name='Ikonka kategorii', blank=True)

     class Meta:
         verbose_name = "Kategoria"
         verbose_name_plural = "Kategorie"

     def __str__(self):
         return self.name

     def __unicode__(self):
         return self.name


class News(models.Model):
     category = models.ManyToManyField(Category,verbose_name='Kategorie')
     title = models.CharField(max_length=255,verbose_name='Tytuł')
     slug = models.SlugField(max_length=255, unique=True,verbose_name='Odnośnik')
     text = models.TextField(verbose_name='Treść')
     date = models.DateTimeField(verbose_name='Data dodania')
     wykop = models.CharField(max_length=255,verbose_name='Wykop', blank=True)

     class Meta:
         verbose_name = "Wiadomość"
         verbose_name_plural = "Wiadomości"

     def __str__(self):
         return self.title

     def __unicode__(self):
         return self.title

     def get_absolute_url(self):
         return '/news/' + self.slug + '/'