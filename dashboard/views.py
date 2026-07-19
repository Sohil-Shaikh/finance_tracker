from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from income.models import Income
from expense.models import Expense


@login_required
def dashboard(request):

    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total_income = incomes.aggregate(total=Sum("amount"))["total"] or 0
    total_expense = expenses.aggregate(total=Sum("amount"))["total"] or 0

    balance = total_income - total_expense

    if total_income > 0:
        savings_percentage = round((balance / total_income) * 100, 2)
    else:
        savings_percentage = 0

    context = {
    "total_income": total_income,
    "total_expense": total_expense,
    "balance": balance,
    "savings_percentage": savings_percentage,

    "income_chart": float(total_income),
    "expense_chart": float(total_expense),
}

    return render(request, "dashboard/dashboard.html", context)