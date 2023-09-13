from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField()
    # link to ToDoList
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    """
    ToDoList
      > Item
      > Item
      ....
    """
