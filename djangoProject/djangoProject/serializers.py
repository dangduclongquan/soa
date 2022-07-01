from rest_framework import serializers

from .models import *


class BankSerializer(serializers.ModelSerializer):
    def create(self):
        return Bank(**self.validated_data)
    class Meta:
        model = Bank
        fields = [
            'name',
            'minimumCreditScore'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    def create(self):
        return Customer(**self.validated_data)
    class Meta:
        model = Customer
        fields = [
            'name',
            'dob',
            'socialID',
            'creditScore'
        ]


class LoanSerializer(serializers.ModelSerializer):
    def create(self):
        return Loan(**self.validated_data)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Loan
        fields = [
            'customer_id',
            'amount',
            'paymentStatus'
        ]


class TaskSerializer(serializers.ModelSerializer):
    def create(self):
        return Task(**self.validated_data)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    bank_id = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = Task
        fields = [
            'customer_id',
            'bank_id'
        ]


class ResultSerializer(serializers.ModelSerializer):
    def create(self):
        return Result(**self.validated_data)
    task_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = Result
        fields = [
            'task_id',
            'canLend',
            'maximumAmount'
        ]
