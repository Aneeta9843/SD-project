from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', max_length=50, null=False, blank=False, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', max_length=150, null=False, blank=False, db_index=True
    )
    image = CloudinaryField(
        'Image', null=True,blank=True 
    )
    created_at = models.DateTimeField(
        'Created At', null=False, blank=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Updated At", null=False, blank=False,auto_now=True
    )

    def __str__(self):
        return self.name


