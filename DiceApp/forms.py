# Login Authentication
from django import forms
from .models import UserProfile
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
)
from django.contrib.auth.models import User


# For Login page
class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": "True", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"autocomplete": "Current-password", "class": "form-control"}
        )
    )


class UserregistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": "True", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"autofocus": "True", "class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"autofocus": "True", "class": "form-control"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"autofocus": "True", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class MyPasswordResetForm(PasswordChangeForm):
    pass


# class UserProfileForm:


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "full_name",
            "username",
            "email",
            "profile_picture",
            "gender",
            "game_history",
            "add_cash",
            "balance",
            "inbox_notification",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileSettingsForm, self).__init__(*args, **kwargs)

        # Add customizations to other fields
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["profile_picture"].widget.attrs.update({"class": "form-control"})
        self.fields["gender"].widget.attrs.update({"class": "form-control"})
        self.fields["game_history"].widget.attrs.update({"class": "form-control"})
        self.fields["add_cash"].widget.attrs.update({"class": "form-control"})
        self.fields["balance"].widget.attrs.update({"class": "form-control"})
        self.fields["inbox_notification"].widget.attrs.update({"class": "form-control"})


from django import forms


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "New Password"}), label=""
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}), label=""
    )


from django import forms
from .models import WithdrawalRequest


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = WithdrawalRequest
        fields = [
            "amount",
            "payment_method",
            "bank_name",
            "account_number",
            "ifsc_code",
            "upi_id",
        ]

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get("payment_method")
        bank_name = cleaned_data.get("bank_name")
        account_number = cleaned_data.get("account_number")
        ifsc_code = cleaned_data.get("ifsc_code")
        upi_id = cleaned_data.get("upi_id")

        if payment_method == "bank_transfer":
            if not bank_name or not account_number or not ifsc_code:
                raise forms.ValidationError("All bank details must be provided.")
        elif payment_method == "upi":
            if not upi_id:
                raise forms.ValidationError("UPI ID must be provided.")
