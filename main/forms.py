from django import forms


class RequestForm(forms.Form):
    keyword = forms.CharField(max_length=50, label='Слово для поиска')
