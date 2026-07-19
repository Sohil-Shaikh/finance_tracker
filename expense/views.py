from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Expense
from .forms import ExpenseForm


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)

    return render(request, 'expense/expense_list.html', {
        'expenses': expenses
    })


@login_required
def add_expense(request):

    if request.method == "POST":

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()

            messages.success(request, "Expense added successfully.")

            return redirect("expense_list")

    else:

        form = ExpenseForm()

    return render(request, "expense/add_expense.html", {
        "form": form
    })


@login_required
def edit_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():

            form.save()

            messages.success(request, "Expense updated successfully.")

            return redirect("expense_list")

    else:

        form = ExpenseForm(instance=expense)

    return render(request, "expense/add_expense.html", {
        "form": form
    })


@login_required
def delete_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )

    expense.delete()

    messages.success(request, "Expense deleted successfully.")

    return redirect("expense_list")