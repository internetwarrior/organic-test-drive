from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError




class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    # Ensure max_tags is defined if needed
    # max_tags = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    STATES = [
        ('new', 'L1_7'),
        ('active', 'L2_30'),
        ('completed', 'L3_30'),
    ]
    
    
    name = models.CharField('Название',max_length=50,blank=False, default='')
    description = models.TextField('Описание',max_length =250, blank =False,default ='')
    
    progress_bar = models.IntegerField('Прогресс',default=0,validators=[
            MaxValueValidator(100),
            MinValueValidator(0),]
 )
    state = models.CharField('Сдадия',max_length=10, choices=STATES, default='new')
    
    dao_project = models.BooleanField(default=False)
    xp = models.IntegerField(default=0)
    flag = CountryField('Флаг страны',blank_label='(select country)', null=True, blank=True)
    
    kyc_verified = models.BooleanField('Верификация',default=False)
    
    
    tags = models.ManyToManyField(Tag)
    
    

    def __str__(self):
        return f"Проект {self.name}"

