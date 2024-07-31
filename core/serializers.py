# core/serializers.py
from rest_framework import serializers
from .models import User, Expense, ExpenseUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ExpenseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseUser
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    users = ExpenseUserSerializer(many=True)

    class Meta:
        model = Expense
        fields = '__all__'
