from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorForm(forms.Form):
    CHOICES = (("Erkaka", "Erkak"), ("Ayol", "Ayol"))
    name = forms.CharField(label='Ismi')
    gender = forms.ChoiceField(choices=CHOICES, label="Jinsi")
    date_of_birth = forms.DateField(label="Tug'ilgan sanasi ")
    number_of_book = forms.IntegerField(label="Kitoblar soni")
    alive = forms.BooleanField(label="Tirikmi", required=False)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"


class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = "__all__"

