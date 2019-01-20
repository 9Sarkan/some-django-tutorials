from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 40)
    content = models.TextField()
    img = models.ImageField(upload_to = 'PostImages/', default = 'photo.png', verbose_name = 'Post Image')

    def __str__(self):
        return self.title
