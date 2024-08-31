from django.db import models
from django.urls import reverse, path

# Create your models here.
class CorruptionStory(models.Model):
    class Meta:
        ordering = ["-date_created"]

    amount = models.IntegerField(help_text="Enter amount")
    banner = models.ImageField(help_text="Upload the banner image")
    content = models.TextField(help_text="Enter article body")
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(help_text="Enter the article headline", max_length=300)
    is_published = models.BooleanField(default=False, help_text="Is published?")

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("corruption_detail", args=[str(self.id)])
