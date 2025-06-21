from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class WithdrawalRequest(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("bank_transfer", "Bank Transfer"),
        ("upi", "UPI"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default="pending")  # Example status field
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this field exists

    def __str__(self):
        return f"Withdrawal Request by {self.user.username} - Amount: {self.amount}"


# userprofileview model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        blank=True,
        null=True,
    )
    game_history = models.TextField(blank=True, null=True)
    add_cash = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inbox_notification = models.BooleanField(default=True)


from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_request_id = models.CharField(max_length=255, blank=True, null=True)


from django.db import models
from django.contrib.auth.models import User


class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    selected_dice = models.CharField(max_length=50, blank=True, null=True)
    selected_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"


class GameResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_images = models.JSONField()
    bet_amount = models.DecimalField(max_digits=10, decimal_places=2)
    won_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp} - Bet: {self.bet_amount} - Won: {self.won_amount}"


# models.py


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_image = models.CharField(max_length=20)
    bet_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Bet: {self.bet_amount} - image: {self.selected_image}"


# Deposit Message


class DepositMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=False)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now().replace(microsecond=0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.message} - {self.date}"


# practicegamewallet

from django.contrib.auth.models import User
from django.db import models


class VirtualWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet"


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
