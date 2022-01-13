from django.db import models
from markdownx.models import MarkdownxField

class TagModel(models.Model):
    name = models.CharField('tag', max_length=50)
    color = models.CharField('background', max_length=7, default='#000000')

    def __str__(self):
        return self.name


class ArticleModel(models.Model):
    title = models.CharField('title', max_length=100)
    thumbnail = models.ImageField(
        'thumbnail',
        null=True,
        blank=True,
        upload_to='image/'
    )
    tag = models.ManyToManyField(TagModel, verbose_name='tag')
    slug = models.SlugField('slug', unique=True)
    lead_text = models.TextField('lead_text', max_length=120)
    main_text = MarkdownxField('main_text')
    is_public = models.BooleanField('public', default=False)
    created_at = models.DateField('created')

    class ColorModel(models.TextChoices):
        WHITE = '#ffffff', 'white'
        BLACK = '#000000', 'black'
    
    color = models.CharField(
        'text_color',
        max_length=7,
        choices=ColorModel.choices,
        default='#ffffff'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title