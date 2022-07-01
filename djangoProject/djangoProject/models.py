from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    socialID = models.CharField(max_length=255, unique=True)
    creditScore = models.IntegerField()


class Loan(models.Model):

    class PaymentStatus(models.TextChoices):
        Paying = "Paying"
        Paid = "Paid"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    paymentStatus = models.CharField(max_length=255, choices=PaymentStatus.choices)


class Bank(models.Model):
    name = models.CharField(max_length=255)
    minimumCreditScore = models.IntegerField()


class Task(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)


class Result(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    canLend = models.BooleanField()
    maxAmount = models.IntegerField()
