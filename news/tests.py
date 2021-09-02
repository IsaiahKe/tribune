from django.db.models import query
from django.db.models.fields import EmailField
from django.test import TestCase
from .models import Editor,tag,Article
# Create your tests here.
class TestEditorClass(TestCase):
    
    def setUp(self):
        self.james=Editor(fname="James",sname='James',email="james.james@gmail.com")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
        
    def test_save_method(self):
       self.james.save_editor()
       query=Editor.objects.all()
       self.assertTrue(len(query)>0)
       
    def test_delete(self):
        self.james.save_editor()
        self.james.delete_editor()
        query= Editor.objects.all()
        self.assertTrue(len(query)<1)
    # def test_update(self):
    #      self.james.save_editor()
    #      self.james.update_editor('','james@gmail.com')
    #     self.assertEquals(,'james@gmail.com'
        
        
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tag(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tag.objects.all().delete()
        Article.objects.all().delete()  
   