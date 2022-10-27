
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste (models.Model):
    first_name = models.CharField(max_length = 40)
    last_name  = models.CharField(max_length = 40)
    age = models.IntegerField()
    

    def __str__(self):
        return(self.first_name)

class Song (models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    Title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)   
    likes = models.IntegerField()
    artisteId=models.IntegerField()


    def __str__(self):
         return(self.Title)


class Lyrics (models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    song_id = models.IntegerField
   

    def __str__(self):
         return (self.content)
