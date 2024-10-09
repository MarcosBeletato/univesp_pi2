from django.shortcuts import render
from django.http import HttpResponse
import gspread

gc = gspread.service_account(filename='service_account.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1UNkoZviCvDlZnoCtyKgTW3OZWtI2BTbqtHcyeuQhGdc/edit?gid=0#gid=0')
wks = sh.worksheet('pedidos')

# Create your views here.
def home(request):
    wks = sh.worksheet('pedidos')
    return HttpResponse(wks.acell('B2').value)