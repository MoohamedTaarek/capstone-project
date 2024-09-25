from django.shortcuts import render, redirect, get_object_or_404
from .models import transaction
from .forms import TransactionForm
from rest_framework import generics
from .serializers import postSerializer

# List the products - Read
def transaction_list(request):
    transactions = transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

# Create a product - Create
def transactionCreate(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listCreate')
    else:
        form = TransactionForm()
    return render(request, 'transactions/transaction_form.html', {'form': form, 'form_title': 'Create transaction'})

# Update a product - Update
def transaction_update(request, pk):
    transaction = get_object_or_404(transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('listCreate')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/transaction_form.html', {'form': form, 'form_title': 'Update transaction'})

# Delete a product - Delete
def transaction_delete(request, pk):
    transaction = get_object_or_404(transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('listCreate')
    return render(request, 'transactions/transaction_delete.html', {'transaction': transaction})


# API views
class postListAPIView(generics.ListCreateAPIView):
    queryset = transaction.objects.all()
    serializer_class = postSerializer

class postDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = transaction.objects.all()
    serializer_class = postSerializer


