from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def doctor(request):
    return render(request,'doctor.html')
def electronic(request):
    return render(request,'electronic.html')
def fashion(request):
    return render(request,'fashion.html')
def jewellery(request):
    return render(request,'jewellery.html')
