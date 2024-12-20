from django.db import models # type: ignore

# Create your models here.
class URLstore(models.Model):
    id = models.AutoField(primary_key=True)
    short_url = models.CharField(max_length=255, unique=True)
    original_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return self.original_url