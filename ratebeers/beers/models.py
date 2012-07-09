from __future__ import division
from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    num_likes = models.IntegerField(default=0)
    num_dislikes = models.IntegerField(default=0)
    pic = models.CharField(max_length=500)

    @property
    def score(self):
        return round(100 * (self.num_likes / max(5, self.num_likes + self.num_dislikes)))
