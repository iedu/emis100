from django.db import models

# Create your models here.
class test_paper(models.Model):
	qclass_id = models.IntegerField()
	qitem_id = models.IntegerField()
	question = models.CharField(max_length=200)
	answer   = models.CharField(max_length=200)
