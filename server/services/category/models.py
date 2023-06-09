from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'Category'

    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.name
