from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='blog_images')
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.pk, 'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)