from django.db import models
from django.db.models.deletion import PROTECT
import datetime as dt

# Create your models here.
class Editor(models.Model):#Editor model
    fname=models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return self.fname
    class Meta:
        ordering=['fname']
    def save_editor(self):
        self.save()
    def delete_editor(self):
        self.delete()
  
class tags(models.Model):#tags model
    name=models.CharField(max_length=30)
    
    def ____(self):
        return self.tagname
  
class Article(models.Model):#article model  
    title=models.CharField(max_length=50)
    post=models.TextField()
    editor=models.ForeignKey('Editor',on_delete=models.CASCADE)
    tags =models.ManyToManyField(tags)
    postdate= models.DateTimeField(auto_now=True)
    article_image = models.ImageField(upload_to = 'articles/')
    def __str__(self):
        return self.title
    @classmethod
    def news_today(cls):
        date= dt.date.today()
        news=cls.objects.filter(postdate=date)
        return news
    @classmethod
    def pastdays_news(cls,date):
        news= cls.objects.filter(postdate=date)
        return news
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
