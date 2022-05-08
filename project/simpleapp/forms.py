from django import forms
from .models import Post, PostCategory, Category



class PostForm(forms.ModelForm):
   text = forms.CharField(min_length=20)

   class Meta:
       model = Post
       fields = [
           'author',
           'typePost',
           'categoryPost',
           'title',
           'text',
       ]

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       title = cleaned_data.get("title")

       if text == title:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )

       return cleaned_data

