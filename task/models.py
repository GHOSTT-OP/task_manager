from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    deadline = models.DateTimeField()
    private = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    percentage = models.IntegerField(default=0 ,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def save(self, *args, **kwargs):
        if self.to_user == self.from_user:
            self.private = True
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

