from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"
        # fields = ("customer_email", "customer_name", "message")

        widgets ={
            "customer_email" : forms.TextInput(attrs={'style': 'width: 95%;'}),
            "customer_name" : forms.TextInput(attrs={'style': 'width: 95%;'}),
            "message" : forms.Textarea(attrs = {'style': 'width: 95%; height: 150px;'})
        }
        labels = {
            'customer_email' : 'Correo',
            'customer_name' : 'Nombre',
            'message' : 'Mensaje' 
        }
