from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://t3.ftcdn.net/jpg/00/92/66/20/240_F_92662026_9fiMh5jgCBIo9il3sQgMQCXdZ0W5afBa.jpg")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"item_id": self.pk})