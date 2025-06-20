from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='البريد الإلكتروني',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        required=True,
        label='رقم الجوال',
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '05xxxxxxxx'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مستخدم بالفعل.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.startswith("05") or not phone.isdigit():
            raise forms.ValidationError("رقم الجوال غير صالح. يجب أن يبدأ بـ 05 ويتكوّن من أرقام فقط.")
        return phone
