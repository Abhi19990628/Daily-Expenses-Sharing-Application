from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from .models import User, Expense, ExpenseUser
from .serializers import UserSerializer, ExpenseSerializer
import csv

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def create(self, request, *args, **kwargs):
        users = request.data.get('users', None)  # Use get() with a default value
        if users is None:
            return Response({'error': 'users field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Your existing code to create an expense
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def balance_sheet(self, request):
        users = User.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'

        writer = csv.writer(response)
        writer.writerow(['User', 'Total Owed'])

        for user in users:
            total_owed = ExpenseUser.objects.filter(user=user).aggregate(sum('amount_owed'))['amount_owed__sum']
            writer.writerow([user.name, total_owed])

        return response
