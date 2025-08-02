from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    name=models.CharField(max_length=64)
    content=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey('Category', related_name='categories', on_delete=models.PROTECT, null= True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=2, )
    slug=models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts', kwargs={'slug': self.slug})
class Category(models.Model):
    category_name=models.CharField(max_length=32)
    def __str__(self):
        return self.category_name


class Comment(models.Model):
    comment_content=models.TextField(max_length=500)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    comment_post = models.ForeignKey("Post", related_name="com_of_post", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment_content

