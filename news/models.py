from django.db import models

# Create your models here.


class News(models.Model):
    timestamp = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=0)
    touching = models.DecimalField(max_digits=10, decimal_places=0)
    empathy = models.DecimalField(max_digits=10, decimal_places=0)
    boredom = models.DecimalField(max_digits=10, decimal_places=0)
    anger = models.DecimalField(max_digits=10, decimal_places=0)
    amusement = models.DecimalField(max_digits=10, decimal_places=0)
    sadness = models.DecimalField(max_digits=10, decimal_places=0)
    surprise = models.DecimalField(max_digits=10, decimal_places=0)
    warmness = models.DecimalField(max_digits=10, decimal_places=0)
    words = models.TextField(blank=True, null=True)
    wordDict = {}

    def __str__(self):
        return self.timestamp

    class Meta:
        ordering = ['-timestamp']
        db_table = "news_test"