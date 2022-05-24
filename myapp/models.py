from django.db import models
from .utils import get_ihreb_data,get_niceone_data,get_amazon_price,get_xcite_price
# dell01 in the code


class Link(models.Model):
    title = models.CharField(max_length=250,blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']    # Order By .....

    def save(self, *args, **kwargs):
        title,price = get_ihreb_data(self.url)


        old_price = self.current_price               # the price we get now
        if self.current_price:                       # if update is successful    # change this
            if price != old_price:                   # chek if this condition is true
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price          # if we have a change if the price  its be came the old_price tha we has the current_price
            else:                                   # if not be update       
                self.old_price = 0    
                self.price_difference = 0

        
        self.title = title 
        self.current_price = price

        super().save(*args, **kwargs)


class Niceone(models.Model):
    title = models.CharField(max_length=250,blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']    # Order By .....

    def save(self, *args, **kwargs):
        title,price = get_niceone_data(self.url)
        old_price = self.current_price               # the price we get now
        if self.current_price:                       # if update is successful    # change this
            if price != old_price:                   # chek if this condition is true
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price          # if we have a change if the price  its be came the old_price tha we has the current_price
            else:                                   # if not be update       
                self.old_price = 0    
                self.price_difference = 0

        
        self.title = title 
        self.current_price = price

        super().save(*args, **kwargs)


class Amazon(models.Model):
    title = models.CharField(max_length=250,blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']    # Order By .....

    def save(self, *args, **kwargs):
        title,price = get_amazon_price(self.url)
        old_price = self.current_price               # the price we get now
        if self.current_price:                       # if update is successful    # change this
            if price != old_price:                   # chek if this condition is true
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price          # if we have a change if the price  its be came the old_price tha we has the current_price
            else:                                   # if not be update       
                self.old_price = 0    
                self.price_difference = 0

        
        self.title = title 
        self.current_price = price

        super().save(*args, **kwargs)



class Xcite(models.Model):
    title = models.CharField(max_length=250,blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']    # Order By .....

    def save(self, *args, **kwargs):
        title,price = get_xcite_price(self.url)
        old_price = self.current_price               # the price we get now
        if self.current_price:                       # if update is successful    # change this
            if price != old_price:                   # chek if this condition is true
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price          # if we have a change if the price  its be came the old_price tha we has the current_price
            else:                                   # if not be update       
                self.old_price = 0    
                self.price_difference = 0

        
        self.title = title 
        self.current_price = price

        super().save(*args, **kwargs)