from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Income
from .forms import IncomeForm


@login_required
def income_list(request):

    incomes = Income.objects.filter(user=request.user)

    # Search
    search = request.GET.get("search","")

    if search:
        incomes = incomes.filter(title__icontains=search)

    # Category Filter
    category = request.GET.get("category")

    if category:
        incomes = incomes.filter(category=category)

    paginator = Paginator(incomes, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "search": search,
        "category": category,
    }

    return render(request, "income/income_list.html", context)

@login_required
def add_income(request):

    if request.method == "POST":

        form = IncomeForm(request.POST)

        if form.is_valid():

            income = form.save(commit=False)
            income.user = request.user
            income.save()

            messages.success(request, "Income added successfully.")

            return redirect('income_list')

    else:

        form = IncomeForm()

    return render(request, 'income/add_income.html', {
        'form': form
    })


@login_required
def edit_income(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = IncomeForm(request.POST, instance=income)

        if form.is_valid():

            form.save()

            messages.success(request, "Income updated successfully.")

            return redirect("income_list")

    else:

        form = IncomeForm(instance=income)

    return render(request, "income/add_income.html", {
        "form": form
    })


@login_required
def delete_income(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    income.delete()

    messages.success(request, "Income deleted successfully.")

    return redirect("income_list")