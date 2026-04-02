from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    completed = models.BooleanField(default=False)

    # ✅ NEW FIELDS
    due_date = models.DateTimeField(null=True, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low')
        ],
        default='Medium'
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title