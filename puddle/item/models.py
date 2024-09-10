from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    # Options for configurations of the model
    class Meta:
        ordering = ('name' ,)
        verbose_name_plural='Categories'

    # Change the name of categories to their real name that has been entered 
    def __str__(self) :
        return self.name
    
    # When you use "CASCADE" in a Django model, it means that if the object that a foreign key points to is deleted, 
    # all the objects that reference it will also be deleted.

class Item(models.Model):
    category = models. ForeignKey (Category, related_name='items', on_delete= models. CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images' ,  blank=True , null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User , related_name = 'items' ,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name