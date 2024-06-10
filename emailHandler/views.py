from django.shortcuts import render
from emailHandler.models import companyDetails
from emailHandler.tasks import send_mail_to_company



# Create your views here.

def index(request):

    return render(request,'personal/index.html')



    


def update_company(request):
    with open('jobs.txt','r') as jobs:
        for job in jobs:
            details = job.split()
            email = details[-1]
            company_name = " ".join(details[:-1])
            print( f"the company name is {company_name} and email is {email}")
            companyDetails.objects.create(company_name=company_name, email=email)
             # Trigger the Celery task to send an email
            k = send_mail_to_company.delay(company_name, email)
            print(k.result)
            print(dir(k))

   

    # Fetch all company details from the database
    company_jobs = companyDetails.objects.all()
    context = {'company': company_jobs}

    return render(request, 'personal/email_template.html', context)


