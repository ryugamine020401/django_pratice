from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseModelForm


def form(request):

    expenses = Expense.objects.all()  # 查詢所有資料
    Form = ExpenseModelForm()
    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/money")

    context = {
        'expenses': expenses,
        'form': Form,
    }
    return render(request, 'moneyindex.html', context)

def update(request, pk):

    expense = Expense.objects.get(id=pk)
    form = ExpenseModelForm(instance=expense)
    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/money")
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

def delete(request, pk):

    expense = Expense.objects.get(id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("/money")

    context = {
        'expense': expense,
    }
    return render(request, 'delete.html', context)