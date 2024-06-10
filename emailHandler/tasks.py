# emailHandler/tasks.py

import logging
from celery import shared_task
from jobhunter.celery import app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

logger = logging.getLogger(__name__)

@app.task()
def send_mail_to_company(company_name, company_email):
    try:
        
        subject = f"Application for Python Developer Position at {company_name}"
        from_email = 'ajithajayan222aa@gmail.com'
        to_email = [company_email]

        context = {
            'hiring_manager': 'Hiring_manager',
            'company_name': company_name
        }

        html_content = render_to_string('personal/email_coverletter.html', context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")

        resume_path = 'C:/Users/ajith/OneDrive/Desktop/jobhunter/assets/Email/PDF/Ajith_Ajayan_Fullstack_Developer__Resume.pdf'

        if os.path.exists(resume_path):
            email.attach_file(resume_path)
        else:
            logger.warning("Resume file not found at the specified path.")

        email.send(fail_silently=False)
        logger.info("Email sent successfully")

    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        raise
