from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('posted', 'Posted'),
)


# -------------------------------------------------------------------------
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique_for_date='posted')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    dp = models.ImageField(upload_to='publisher_dp',
                           blank=True, null=True)
    email = models.EmailField(null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    createdBy = models.ForeignKey(User,
                                  related_name='PublisherUser',
                                  on_delete=models.CASCADE, )
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('BAP:PublisherDetail',
                       args=[self.pk])

# -------------------------------------------------------------------------
class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=30, unique_for_date='posted')

    email = models.EmailField()
    dp = models.ImageField(upload_to='author_dp',
                           blank=True, null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    createdBy = models.ForeignKey(User,
                                  related_name='AuthorUser',
                                  on_delete=models.CASCADE, )
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('BAP:AuthorDetail',
                       args=[self.pk])

# -------------------------------------------------------------------------
class Book(models.Model):
    GENRE_CHOICES = (
        ('fiction', 'Fiction'),
        ('pureScience', 'PureScience'),
        ('education', 'Education'),
        ('childrens', 'Childrens')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique_for_date='posted')
    genre = models.CharField(max_length=15,
                             choices=GENRE_CHOICES,
                             default='fiction')
    authors = models.ManyToManyField('Author',
                                   related_name='BookAuthors')
    publisher = models.ForeignKey(Publisher,
                                  related_name='PublisherBook',
                                  on_delete=models.CASCADE)
    publication_date = models.DateField()
    cover_pic = models.ImageField(upload_to='book_cover_pic',
                                  blank=True, null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    createdBy = models.ForeignKey(User,
                                  related_name='BookUser',
                                  on_delete=models.CASCADE, )
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-genre"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('BAP:BookDetail',
                       args=[self.pk])



# -------------------------------------------------------------------------
