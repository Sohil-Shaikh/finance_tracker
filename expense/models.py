from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expenses'
    )

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Food'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(blank=True, null=True)

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"