from django import forms
from .models import OrderForm
class OrderInfo(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = {'customer_name','address1','address2','city','mobile_no','dilevery_mode','product','status'}
        