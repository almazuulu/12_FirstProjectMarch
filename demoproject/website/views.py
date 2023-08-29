from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = "Askar"
    
    html_code = f"<h1> Hello World! {name}</h1>"\
        "<p> Some code in HTML!! </p>" \
        "<b> New changes </b>"
    
    return HttpResponse(html_code)
    
def about_us(index):
    html_code = "<h1> About us</h1>"\
        "<p> We are wonderful team! </p>" 
    
    return HttpResponse(html_code)


def contact_us(index):
    html_code = "<h1> Contact us</h1>"\
        "<p> We are wonderful team! </p>" 
    
    return HttpResponse(html_code)
