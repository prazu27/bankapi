from django.db import models

# Create your models here.

class Bank(models.Model):
	name = models.CharField(max_length=255)
	branch_code = models.CharField(max_length=20)
	ifsc_code = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Customer(models.Model):
	username = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	bank_account_number = models.CharField(max_length=20, unique=True)
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
	balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

	def __str__(self):
		return self.username