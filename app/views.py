from django.shortcuts import render, redirect
from django.http import HttpResponse
import gspread
import datetime

gc = gspread.service_account(filename='service_account.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1UNkoZviCvDlZnoCtyKgTW3OZWtI2BTbqtHcyeuQhGdc/edit?gid=0#gid=0')

# Create your views here.
def home(request):
    wks = sh.worksheet('pedidos')
    data = {}

    data['values'] = wks.get_all_records()
    return render(request, 'index.html', data)

def create(request):
    return render(request, 'create.html')

def store(request):
    sh.values_append(
            'pedidos!A2',
            params={
                'valueInputOption':'RAW'
            },
            body={
                'values':[[request.POST['name'], request.POST['address'], request.POST['order'], request.POST['ordertime']]]
            }
    )

    return redirect('/')

def delete(request):
    if request.method == 'POST':
        row_number = int(request.POST['row_number']) + 1  # Ajustando índice (contagem começa em 1)
        wks = sh.worksheet('pedidos')
        wks.delete_rows(row_number)
    return redirect('/')