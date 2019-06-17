from django.db import models
from datetime import datetime
# Create your models here.

class TodoItem(models.Model):
	Book_title = models.TextField()
	Author_name = models.TextField()
	Published_year = models.DateField(default=datetime.now)