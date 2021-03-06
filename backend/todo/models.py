from django.db import models


# Represents a To-Do task
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
