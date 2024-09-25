from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Transaction(models.Model):
    transaction_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.description} - {self.amount}"
    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    transaction = models.ForeignKey(Transaction,
                                on_delete=models.PROTECT,
                                default = 1)
    

    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default = timezone.now)
    
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='transaction_posts')
    
    status = models.CharField (
        max_length=10,
        choices = options,
        default='published')

    objects = models.Manager() # The default manager.
    postobjects = PostObjects() # The custom manager.

    class Meta:
        ordering = ('-published',)



    def __str__(self):
        return self.title
