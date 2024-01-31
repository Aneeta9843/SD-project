from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Category

# Create your models here.
class Place(models.Model):
    MY_CHOICES=(
        ('Private and Luxury','Private and Luxury'),
        ('Full day Tours','Full day tours'),
        ('Day trips','Day Trips'),
        ('Forest','Forest'),
        ('Favourites','Favourites'),
    ) 
    class Meta(object):
        db_table = 'place'

    #name,description, image,category, place_type, time to travel,google map link,created_at,updated_at
    name = models.CharField(
        'Name',max_length= 60, null=False,blank=False, db_index=True
    )
    descriptions= models.CharField(
        'Description', max_length= 750, null=False,blank=False, db_index=True
    )
    image = CloudinaryField(
        "Images", null=False, blank=False
    )
    category = models.ForeignKey(
        Category, on_delete =models.CASCADE
    )
    place_type = models.CharField(
        'Place Type', max_length=50, null=False, blank=False,choices= MY_CHOICES
    )
    time_to_travel = models.CharField(
        'Time To Travel', max_length=10, null=False, blank=False
    )
    google_map_link =models.CharField(
        'Google Map', max_length=500, null=False,blank=False)
    
    created_at = models.DateTimeField(
        'Created At', null=False, blank=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', null=False, blank=False, auto_now=True
    )

    def __str__(self):
        return self.name

