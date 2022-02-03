from django import forms
from hostel.models import Hostel ,Reviews

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields =  ("date","customername","customer_id","price","hostel_name")

class HostelupdateForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields =  ("date",)
 
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=("__all__")