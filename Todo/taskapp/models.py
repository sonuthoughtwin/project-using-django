from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_content = models.TextField(blank=True)
    created_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        ordering =['-created_date']




    def __str__(self):
        return str(self.id)+" "+self.task_title+" "+self.task_content
        

