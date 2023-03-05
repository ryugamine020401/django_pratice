from django import forms
from .models import Expense
class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        # fields = ('name', 'price')
        # fields = '__all__' 可以顯示所有
        fields = '__all__'
        widgets = {  # 客製化表單的顯示外觀 套用Bootstrap的表單CSS類別
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {  # 讓表單顯示中文
            'name': '花費項目',
            'price': '金額'
        }
