from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse
from .params import URL,USER_NAME,PASSWORD

#The main function to render the homepage, i.e- tickets page
def view_tickets(request):
    #Retrieved URL from params.py
    url = URL
    try:
        #Initial get API request for json data with authentication check
        response = requests.get(url,auth = HTTPBasicAuth(USER_NAME,PASSWORD))
    except Exception as e:
        #If authentication fails, this is the error message displayed
        return HttpResponse(" Sorry, there was an error with authentication. Please try again")
    #if get is successful, the json is converted to dictionary in a list.
    data = response.json()
    #Returns a message that there are no tickets in case there is no data
    if len(data)==0:
        return HttpResponse(" Sorry, currently there are no tickets assigned")
    context = {
        "subject": data["requests"],
    }
    #This displays all the values in the html page
    return render(request, "tickets.html", context)

def ticket(request):
    # Same process as in view_tickets function
    url = URL
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER_NAME, PASSWORD))
    except Exception as e:
        return HttpResponse(" Sorry, there was an error. Please go back and try again")
    #The posted data from tickets.html page is retrieved here
    subject = request.POST.get('subj')
    ticketid = request.POST.get('id')
    description = request.POST.get('description')

    context = {
        'subject':subject,
        'ticketid':ticketid,
        'description':description
    }
    #Withthehelp of this retrieved data, we are able to print details of ticket clicked on in
    #previous page in viewticket.html page
    return render(request,'viewticket.html',context)