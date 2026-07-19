from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from income.models import Income
from expense.models import Expense
import json


@login_required
def report_dashboard(request):

    # Get logged-in user's data
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    # Summary
    total_income = incomes.aggregate(total=Sum("amount"))["total"] or 0
    total_expense = expenses.aggregate(total=Sum("amount"))["total"] or 0

    balance = total_income - total_expense

    # Expense Category Wise Total
    category_data = (
        expenses.values("category")
        .annotate(total=Sum("amount"))
        .order_by("category")
    )

    labels = []
    data = []

    for item in category_data:
        labels.append(item["category"])
        data.append(float(item["total"]))

    context = {
        "income": total_income,
        "expense": total_expense,
        "balance": balance,
        "labels": json.dumps(labels),
        "data": json.dumps(data),
    }

    return render(request, "reports/dashboard.html", context)