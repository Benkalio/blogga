from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Publish'))

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(max_length=200, unique=True)
  # author = models.ForeignKey(to=User, on_delete=models.CASCADE)
  status = models.IntegerField(choices=STATUS,default=0)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)
  
  # CHANGING THE NAME OF THE MODEL FROM POST
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('blog_view', kwargs={'slug': self.slug})
  

# class User(models.Model):
#   name: mode
