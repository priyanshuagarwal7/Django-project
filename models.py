from django.db import models

# Create your models here.
class CreateBlogPost(models.Model):
    Author  = models.CharField(max_length=20)
    blogtitle = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.Author
    