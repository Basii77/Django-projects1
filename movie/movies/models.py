from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Movies(models.Model):
    title=models.CharField(max_length=50)
    director=models.CharField(max_length=20)
    year=models.IntegerField()
    poster=models.ImageField(upload_to="movies/poster",null=True,blank=True)
    def __str__(self):
        return self.title
