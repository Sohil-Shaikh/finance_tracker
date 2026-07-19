from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    CATEGORY_CHOICES = [
        ('Salary', 'Salary'),
        ('Business', 'Business'),
        ('Freelance', 'Freelance'),
        ('Investment', 'Investment'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='incomes'
    )

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Salary'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"