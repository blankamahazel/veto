from django.shortcuts import render
# New imports
from django.http import HttpResponseRedirect # Redirect the page after submit
from django.contrib import messages # Return messages
from django.core.mail import EmailMultiAlternatives # Request to send emails
from django.template import loader # Render templates on email body
from App.models import Registered_email, Support # Informations in models.py
from django.contrib.auth.decorators import login_required # Login required to acces private pages
from django.views.decorators.cache import cache_control # Destroy the section after logout

# =================FRONTEND SECTION ==================|
# Funtion to render homepage
def home(request):
    return render(request, "home.html")

    # Funtion to render opportunities page
def opportunities(request):
    return render(request, "opportunities.html") 

    # Support
def support(request):
    if request.method == "POST":
            
        # check if email exist in DB
        email = request.POST['email']
        
        if Support.objects.filter(email = email).exists():   
           messages.info(request, ".") # Arguement inside the message cannot be empty (because i put a dot(.))
           return HttpResponseRedirect('/support')
        else: 
            support = Support()

            message = request.POST.get('message')
            terms = request.POST.get('terms')
            person = request.POST.get('person')
            option = request.POST.get('option')
            email = request.POST.get('email')

            support.message = message
            support.message = terms
            support.message = person
            support.message = option
            support.message = email

            support.save()
            messages.success(request, "We will review your request !")
            return HttpResponseRedirect('/')
    else:
            return render(request, "support.html")
 
 

# =========================== RESUMES ===============|
# Function to send frontend form
def email_frontend(request):
    if request.method == "POST":
        
        # check if email exist in DB
        email = request.POST['email']
        
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your CV resume in our DataBase")
            return HttpResponseRedirect('/opportunities')
        # ================    
        else:
             name = request.POST.get('name')
             age = request.POST.get('age')
             email = request.POST.get('email')
             phone = request.POST.get('phone')
             Address = request.POST.get('address')
             experience = request.POST.get('experience') 
             skills = request.POST.get('skills')
        
             #Register inside DB
             contact = Registered_email()
             contact.email = email
             contact.save()
        # ================
        
        template = loader.get_template('resume_form.txt')      
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : Address,
            'experience' : experience,
            'skills' : skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Frontend - Candidate", message,
            "Frontend Opportunity",
            ['vertisev@gmail.com']
        
        )
        email.content_subtype = 'html' 
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send() 
        messages.success(request, 'Frontend resume sent successfully !') 
        return HttpResponseRedirect('/')     
        
        
# Function to send backend form
# Function to send frontend form
def email_backend(request):
    if request.method == "POST":
        
        # check if email exist in DB
        email = request.POST['email']
        
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your CV resume in our DataBase")
            return HttpResponseRedirect('/opportunities')
        # ================    
        else:
             name = request.POST.get('name')
             age = request.POST.get('age')
             email = request.POST.get('email')
             phone = request.POST.get('phone')
             Address = request.POST.get('address')
             experience = request.POST.get('experience') 
             skills = request.POST.get('skills')
        
             #Register inside DB
             contact = Registered_email()
             contact.email = email
             contact.save()
        # ================
        
        template = loader.get_template('resume_form.txt')      
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : Address,
            'experience' : experience,
            'skills' : skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Backend - Candidate", message,
            "Backend Opportunity",
            ['vertisev@gmail.com']
        
        )
        email.content_subtype = 'html' 
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send() 
        messages.success(request, 'Backend resume sent successfully !') 
        return HttpResponseRedirect('/')     
        
# Function to send fullstack form
# Function to send frontend form
def email_fullstack(request):
    if request.method == "POST":
        
        # check if email exist in DB
        email = request.POST['email']
        
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your CV resume in our DataBase")
            return HttpResponseRedirect('/opportunities')
        # ================    
        else:
             name = request.POST.get('name')
             age = request.POST.get('age')
             email = request.POST.get('email')
             phone = request.POST.get('phone')
             Address = request.POST.get('address')
             experience = request.POST.get('experience') 
             skills = request.POST.get('skills')
        
             #Register inside DB
             contact = Registered_email()
             contact.email = email
             contact.save()
        # ================
        
        template = loader.get_template('resume_form.txt')      
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : Address,
            'experience' : experience,
            'skills' : skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Fullstack - Candidate", message,
            "Fullstack Opportunity",
            ['vertisev@gmail.com']
        
        )
        email.content_subtype = 'html' 
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send() 
        messages.success(request, 'Fullstack resume sent successfully !') 
        return HttpResponseRedirect('/')     
        
        # =================BACKEND SECTION ==================|
@cache_control(no_cache=True, must_revalidate=True, no_store=True)     
@login_required(login_url="login")        
def backend(request):
    return render(request,"backend.html")