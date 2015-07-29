from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self')

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=10)
    category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.name

class Code(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' - ' + self.code


