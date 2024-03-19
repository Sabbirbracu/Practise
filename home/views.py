from django.shortcuts import render
from home.models import Contact
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def index(requests):
    return render(requests,'index.html')

def contact(requests):
    if requests.method == "POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        contact_info = Contact(name=name,email=email,subject=subject,message=message)
        contact_info.save()
        messages.success(requests,"Your sms have sent successfully")
        return redirect('/contact')
    
    return render(requests,'contact.html')