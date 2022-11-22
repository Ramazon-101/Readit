from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=70)

    def __str__(self):
        return self.tag


class Article(Timestamp):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    # views = models.IntegerField(defult=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("readit:article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(Timestamp):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='article/comment_author', null=True, blank=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.author.username

    @property
    def get_image_url(self):
        if settings.DEBUG:
            return f'http://127.0.0.1:8000{self.image.url}'
        return f'https://smth.uz/{self.image.url}'
