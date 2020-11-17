from django.db import models
from django.contrib.auth.models import User
import os
import re
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator 
from uuid import uuid4

def generateUUID():
    return str(uuid4())

DEPARTMENTS = (
    ('CHE', 'CHE'),
    ('EEE', 'EEE'),
    ('ECE', 'EEE'),
    ('CS', 'CS'),
    ('MECH', 'MECH'),
    ('INSTR', 'INSTR'),
    ('MATH','MATH'),
    ('PHY','PHY'),
    ('CHEM','CHEM'),
    ('ECON','ECON'),
    ('BIO','BIO'),
    ('HSS','HSS'),
    ('BITS','BITS')
)
COURSE_CODES=(
    ('F266','F266'),
    ('F366','F366'), 
    ('F367','F367'),
    ('F376','F376'), 
    ('F377','F377'), 
    ('F491','F491'),
    ('F382','F382'),  
)

postalAddressChoices=(
    ('Within India','Within India'),
    ('Outside India','Outside India'),  
)

SoftHardChoices=(
    ('Soft Copy','Soft Copy'),
    ('Hard Copy','Hard Copy'),  
)

YEAR = (
    ('2026-2027','2026-2027'),
    ('2025-2026','2025-2026'),
    ('2024-2025','2024-2025'),
    ('2023-2024','2023-2024'),
    ('2022-2023','2022-2023'),
    ('2021-2022','2021-2022'),
    ('2020-2021','2020-2021'),
    ('2019-2020','2019-2020'),
    ('2018-2019','2018-2019'),
    ('2017-2018','2017-2018'),
    ('2016-2017','2016-2017'),
    ('2015-2016','2015-2016'),
    ('2014-2015','2014-2015'),
    ('2013-2014','2013-2014'),
    ('2012-2013','2012-2013'),
    ('2011-2012','2011-2012'),
    ('2010-2011','2010-2011'),
    ('2009-2010','2009-2010'),
    ('2008-2009','2008-2009'),
    ('2007-2008','2007-2008'),
    ('2006-2007','2006-2007'),
    ('2005-2006','2005-2006'),
    ('2004-2005','2004-2005'),
    ('2003-2004','2003-2004'),
) 

SEMESTER = (
    ('sem1','Sem - I'),
    ('sem2','Sem - II')
) 

GRADUATION_STATUS = (
    ('continuing','Continuing Student'),
    ('graduated','Graduated Student')
) 



class Arc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Transcript(models.Model):
    name = models.CharField(max_length=20, blank = False)
    bitsID = models.CharField(max_length=13, blank=False, null = False)
    corrEmail = models.EmailField(max_length=50, blank = False, null = False)
    phone_number = models.CharField(max_length=10, blank = False, validators=[MinLengthValidator(10)], null=False)
    refNo = models.CharField(max_length=20, blank = False)
    approved = models.BooleanField(default=0, blank=True)
    disapproved = models.BooleanField(default=0, blank=True)
    inprocess = models.BooleanField(default=1, blank=True)
    posted = models.BooleanField(default=0, blank=True)
    printed = models.BooleanField(default=0, blank=True)
    hostel = models.CharField(max_length=4, blank = True)
    roomNo = models.CharField(max_length=3, blank = True)
    gradStatus = models.CharField(max_length=20, choices=GRADUATION_STATUS, default='continuing')
    ps2Station = models.CharField(max_length=50, blank = True)
    origTranscript = models.IntegerField(default=1, blank=True, validators=[MinValueValidator(0)])
    dupTranscripts = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])
    forwardingLetters = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])
    sealedCopies = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])
    amtcal = models.IntegerField(default=200, blank=True)
    paidAmount = models.IntegerField(default=0, blank=True)
    paymentApproved = models.BooleanField(default=0, blank=True)
    paymentDisapproved = models.BooleanField(default=0, blank=True)
    paymentInprocess = models.BooleanField(default=1, blank=True)
    form_no=models.CharField(default=generateUUID, max_length=36, unique=True, editable=False)
    postalAddressLocation = models.CharField(max_length=20, choices = postalAddressChoices  , default='Within India')
    postalAddress = models.CharField(max_length=100, blank = True)
    remarks = models.CharField(max_length=100, blank = True)
    soft_hard_copy = models.CharField(max_length=20, choices = SoftHardChoices , default='Soft Copy')


    def __str__(self):
        return self.bitsID + ' '+ self.refNo

class Gradesheet (models.Model):
    name = models.CharField(max_length=20, blank = False)
    bitsID = models.CharField(max_length=13, blank=False, null = False)
    corrEmail = models.EmailField(max_length=50, blank = False, null = False)
    phone_number = models.CharField(max_length=10, blank = False, validators=[MinLengthValidator(10)], null=False)
    refNo = models.CharField(max_length=20, blank = False)
    approved = models.BooleanField(default=0, blank=True)
    disapproved = models.BooleanField(default=0, blank=True)
    inprocess = models.BooleanField(default=1, blank=True)
    posted = models.BooleanField(default=0, blank=True)
    printed = models.BooleanField(default=0, blank=True)
    hostel = models.CharField(max_length=4, blank = True)
    roomNo = models.CharField(max_length=3, blank = True)
    ps2Station = models.CharField(max_length=50, blank = True)
    sealedCopies = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])
    amtcal = models.IntegerField(default=200, blank=True)
    paidAmount = models.IntegerField(default=0, blank=True)
    paymentApproved = models.BooleanField(default=0, blank=True)
    paymentDisapproved = models.BooleanField(default=0, blank=True)
    paymentInprocess = models.BooleanField(default=1, blank=True)
    form_no=models.CharField(default=generateUUID, max_length=36, unique=True, editable=False)
    postalAddressLocation = models.CharField(max_length=20, choices=postalAddressChoices, default='Within India')
    postalAddress = models.CharField(max_length=50, blank = True)
    noOfSemesters = models.IntegerField(default=1, blank = False, validators = [MinValueValidator(1)])
    remarks = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return self.bitsID + ' '+ self.refNo


class Project(models.Model):
    studentname = models.CharField(max_length = 100, null= True, blank = False,verbose_name = 'Student Name')
    studentId = models.CharField(max_length = 13, null= True, blank = False,verbose_name = 'Student ID')
    title = models.CharField(max_length = 200, null=True,blank =False, verbose_name = 'Project Title')
    department = models.CharField(max_length=5, choices=DEPARTMENTS, null=True, blank=False,verbose_name = 'Department Code')
    courseCode = models.CharField(max_length=30, choices=COURSE_CODES, null=True, blank=False,verbose_name = 'Course Code')
    faculty = models.ForeignKey('Faculty', on_delete = models.CASCADE,verbose_name = 'Faculty')
    approved = models.BooleanField(default=0, blank=True,verbose_name = 'Approved')
    disapproved = models.BooleanField(default=0, blank=True)
    inprocess = models.BooleanField(default=1, blank=True)
    def __str__(self):
        return self.faculty.name + ' '+ self.studentname + ' ' + str(self.id)

class SealedAddress(models.Model):
    addr = models.CharField(max_length=80)
    transcript = models.ForeignKey(Transcript, related_name='sealed_addresses', on_delete=models.CASCADE)

class SealedAddressGradesheet(models.Model):
    addr = models.CharField(max_length=80)
    gradesheet = models.ForeignKey(Gradesheet, related_name='sealed_addresses_gradesheet', on_delete=models.CASCADE)

class GradesheetCopies(models.Model):
    year = models.CharField(max_length=4, choices=YEAR, default='2015-2016')
    semester = models.CharField(max_length=8, choices=SEMESTER, default='sem1')
    copies = models.IntegerField(default=1, blank=False, validators = [MinValueValidator(1)])
    gradesheet = models.ForeignKey(Gradesheet, related_name='gradesheet_copies', on_delete=models.CASCADE)


