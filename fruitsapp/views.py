from django.shortcuts import render

# Create your views here.
#Home View
def index(request):
    return render(request, 'fruitsapp/index.html')

#About View
def about(request):
    return render(request, 'fruitsapp/about.html')

#shop View
def shop(request):
    return render(request, 'fruitsapp/shop.html')

#contact View
def contact(request):
    return render(request, 'fruitsapp/contact.html')