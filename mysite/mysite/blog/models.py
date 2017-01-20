from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=1, choices=(
        ('D', 'Draft'),
        ('P', 'Published'),
    ))

    author = models.ForeignKey('auth.User',
        related_name='posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
