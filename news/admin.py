from django.contrib import admin
from .models import tags,Article,Editor

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Editor)
admin.site.register(tags)

