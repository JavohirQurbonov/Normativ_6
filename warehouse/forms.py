from django.forms import ModelForm
from warehouse.models import Contact, Book

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','last_name','email','message']

class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','pages','price']

class UpdateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['pages','price']

