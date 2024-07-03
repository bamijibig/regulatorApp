from django.db import models

class Regulator(models.Model):
    JURISDICTION_CHOICES = (
        ('National', 'National'),
        ('Scotland', 'Scotland'),
        ('England', 'England'),
      
    )
    
    name = models.CharField(max_length=255)
    jurisdiction = models.CharField(
        max_length=50,
        choices=JURISDICTION_CHOICES,
        default='NATIONAL',  # Default should match one of the choices' values
    )
    contact_information = models.TextField()
    regulatory_scope = models.TextField()
    legal_documents = models.TextField()

    def __str__(self):
        return self.name

class IndustrySector(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RegulationType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Regulation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    regulator = models.ForeignKey(Regulator, on_delete=models.CASCADE)
    industry_sector = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    regulation_type = models.ForeignKey(RegulationType, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    regulatorydetails = models.TextField()

    def __str__(self):
        return self.title
