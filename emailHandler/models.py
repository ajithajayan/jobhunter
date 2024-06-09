from django.db import models

# Create your models here.

status = [('applied','applied'),
          ('rejected','rejected'), 
          ('Hr round', 'Hr round'), 
          ('TechnicalRound', 'TechnicalRound'), 
          ('offerletter', 'offerletter'),
        ]


class companyDetails(models.Model):
    company_name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    applied_date = models.DateField(auto_now=True)
    application_status = models.CharField(max_length=100, choices=status, default='applied' )

    def __str__(self):
        return self.company_name
    
