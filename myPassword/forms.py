from django import forms


class PasswordForm(forms.Form):
    your_password = forms.CharField(label="your password", max_length=100)