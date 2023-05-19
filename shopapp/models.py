from django.db import models

# Create your models here.
class Catigory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    image = models.ImageField()
    ish_vaqti = models.CharField(max_length=30)
    tel = models.CharField(max_length=300)
    telegrma = models.CharField(max_length=300)
    ish_kunlari = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Catigory,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name


class Snakers(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(unique=True,blank=True)
    type=models.ForeignKey(Catigory,on_delete=models.CASCADE)
    more=models.TextField()
    uz = "so`m"
    en = "$"
    ru = "rubl"
    the_price=(
        (uz,"so`m"),
        (en,"$"),
        (ru,"rubl"),
    )
    price_type = models.CharField(max_length=10,choices=the_price,default="so`m")
    price = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name

class Buy(models.Model):
    name = models.CharField(max_length=156)
    pthone = models.CharField(max_length=30)
    produck = models.ForeignKey(Snakers,on_delete=models.CASCADE,null=True)
    ALL_VALUES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    how = models.CharField(max_length=100,choices=ALL_VALUES)
    map = models.TextField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    message = models.TextField()
