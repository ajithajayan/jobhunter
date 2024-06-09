from django.shortcuts import render
from emailHandler.models import companyDetails
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os


# Create your views here.

def index(request):

    return render(request,'personal/index.html')


def send_mail_to_company():
    subject = "For the project application"
    from_email = 'ajithajayan222aa@gmail.com'
    to_email = ['ajithakhil333aa@gmail.com']

    # Define the context for the template
    context = {
        'hiring_manager': 'John Doe',
        'company_name': 'LSQARED'
    }

    # Render the HTML template with context
    html_content = render_to_string('personal/email_coverletter.html', context)
    text_content = strip_tags(html_content)  # Convert HTML to plain text

    # Create the email with both plain text and HTML alternatives
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")

    # Path to your resume PDF file
    resume_path = 'C:/Users/ajith/OneDrive/Desktop/jobhunter/assets/Email/PDF/Ajith_Ajayan_Fullstack_Developer__Resume.pdf'

    
    # Attach the PDF file
    if os.path.exists(resume_path):
        email.attach_file(resume_path)
    else:
        print("Resume file not found at the specified path.")

 
    # Send the email
    email.send(fail_silently=False)

    


def update_company(request):
    # with open('jobs.txt','r') as jobs:
    #     for job in jobs:
    #         details = job.split()
    #         email = details[-1]
    #         company_name = " ".join(details[:-1])
    #         print( f"the company name is {company_name} and email is {email}")
    #         companyDetails.objects.create(company_name=company_name, email=email)


    send_mail_to_company()

    company_jobs = companyDetails.objects.all() 
    context = { 'company' :company_jobs}


    return render(request,'personal/email_template.html',context)


