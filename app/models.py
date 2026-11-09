from django.db import models
from django.utils.text import slugify
from unidecode import unidecode 

def make_unique_slug(model, instance, source):
    base = slugify(unidecode(source)) or "item"
    slug = base
    n = 2
    while model.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
        slug = f"{base}-{n}"
        n += 1
    return slug

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(Category, self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    place = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(Event, self, self.name)
        super().save(*args, **kwargs)
                
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('date_time',)
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"