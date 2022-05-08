from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRate = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRate = self.post_set.aggregate(postRate = Sum('rating'))
        defRate = 0
        defRate += postRate.get('commentRate')
        commentRate = self.authorUser.comment_set.aggregate(commentRate = Sum('commentRate'))
        self.authorRate = postRate *3 + commentRate
        self.save()


class Category(models.Model):
    CategoryName = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.CategoryName.title()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICED = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    typePost = models.CharField(max_length=2, choices=CATEGORY_CHOICED)
    daterimePost = models.DateTimeField(auto_now=True)
    categoryPost = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return  f'{self.title}: {self.text[:4]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])




class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True)
    commentRate = models.SmallIntegerField(default=0)

    def like(self):
        self.commentRate += 1
        self.save()

    def dislike(self):
        self.commentRate -= 1
        self.save()
