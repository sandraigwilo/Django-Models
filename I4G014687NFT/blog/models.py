from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.text

    def __str__(self):
        return self.author

    def __str__(self):
        return self.created_date

    def __str__(self):
        return self.published_date