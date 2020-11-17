from django import forms
from .models import Project
from .models import Transcript,SealedAddress,Gradesheet,SealedAddressGradesheet, GradesheetCopies
from django.forms.widgets import *
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime
from django.core.validators import MinValueValidator

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


YEAR = (
    ('2019-2020','2019-2020'),
    ('2018-2019','2018-2019'),
    ('2017-2018','2017-2018'),
    ('2016-2017','2016-2017'),
    ('2015-2016','2015-2016')
) 

SEMESTER = (
    ('sem1','Sem - I'),
    ('sem2','Sem - II')
) 


class ProjectForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        return cleaned_data
    # courseCode = forms.ChoiceField(choices=COURSE_CODES,required = True, help_text="F266/F366/F367/F376/F377/F491")

    class Meta:
        model = Project
        fields = ['studentname','studentId','title','department','courseCode']
        exclude = ['faculty','approved', 'disapproved', 'inprocess', ]
        widgets = {
            'department': forms.TextInput(attrs={'class': 'validate'}),
            'courseCode': forms.TextInput(attrs={'class': 'validate'}),
            'title': forms.Textarea(attrs={'class': 'materialize-textarea'}),

        }
        labels = {
            'studentname': _('Student Name'),
            'studentId': _('Student ID'),
            'department': _('Department code'),
            'courseCode': _('Course Code'),
            'title': _('Project Title'),

        }

class TranscriptForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(TranscriptForm, self).clean()
        
        if ((cleaned_data['origTranscript'] != 0) and (cleaned_data['gradStatus']=='graduated')):
            self._errors["origTranscript"] = ["Graduated Students cannot appply for original transcripts"] # Will raise a error message
            del cleaned_data['origTranscript']
        elif ((cleaned_data['origTranscript'] == 0) and (cleaned_data['gradStatus']=='continuing')):
            self._errors["origTranscript"] = ["Continuing students must apply for atleast one original transcript"] # Will raise a error message
            del cleaned_data['origTranscript']
        elif ((cleaned_data['origTranscript'] == 0) and (cleaned_data['dupTranscripts']==0)):
            self._errors["dupTranscripts"] = ["Kindly apply for atleast one transcript"] # Will raise a error message
            del cleaned_data['dupTranscripts']

        if ( (cleaned_data['postalAddressLocation'] != 'None') and ( (cleaned_data['postalAddress']=='') or (cleaned_data['postalAddress']==None) ) ):
            self._errors["postalAddress"] = ["Please specify the address"] # Will raise a error message
            del cleaned_data['postalAddress']
        elif ( (cleaned_data['postalAddressLocation'] == 'None') and ( (cleaned_data['postalAddress']!='') and (cleaned_data['postalAddress']!=None) ) ):
            self._errors["postalAddressLocation"] = ["Please specify the address location"] # Will raise a error message
            del cleaned_data['postalAddressLocation']
        elif ( (cleaned_data['postalAddressLocation'] == 'None') and (cleaned_data['gradStatus']=='graduated') ):
            self._errors["postalAddressLocation"] = ["Please specify the address location"] # Will raise a error message
            del cleaned_data['postalAddressLocation']
            
        
        
        return cleaned_data

    class Meta:
        model = Transcript
        exclude = ['disapproved', 'inprocess', 'approved', 'paymentApproved', 'paymentDisapproved', 'paymentInprocess', 'paidAmount', 'refNo', 'amtcal','form_no','posted','printed','remarks']
        labels = {
            'dupTranscripts': _('Number of Duplicate transcripts'),
            'bitsID': _('Student ID'),
            'corrEmail': _('E-mail address'),
            'gradStatus': _('Graduation Status'),
            'hostel': _('Hostel (Leave blank if not applicable)'),
            'roomNo': _('Room No. (Leave blank if not applicable)'),
            'ps2Station': _('PS-2 Station (Leave blank if not applicable)'),
            'forwardingLetters': _('Number of Forwarding Letters'),
            'sealedCopies': _('Number of Sealed Copies'),
            'origTranscript': _('Number of original transcripts'),
            'phone_number': _('Phone Number'),
            'name': _('Name'),
            'postalAddress': _('Postal Address'),
            'postalAddressLocation': _('Postal Address Location'),
            'soft_hard_copy': _('Want a soft copy or hard copy'),
        }

class TranscriptForm2(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(TranscriptForm2, self).clean()

    class Meta:
        model = Transcript
        fields = ['refNo','remarks']
        labels = {
            'remarks': _('Remarks (Optional)'),
            'refNo': _('SBI Payment Reference Number')
        }

    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        extra = int(extra)
        super(TranscriptForm2, self).__init__(*args, **kwargs)

        for i in range(extra):
            self.fields['Sealed address %s' % i] = forms.CharField(max_length=80)

        self.fields.move_to_end('remarks', last=True)



class AddressForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(AddressForm, self).clean()

    class Meta:
        model = SealedAddress
        fields = ['addr','transcript']

class GradesheetCopiesForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(GradesheetCopiesForm, self).clean()

    class Meta:
        model = GradesheetCopies
        fields = ['year','semester','copies','gradesheet']



class GradesheetForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(GradesheetForm, self).clean()

        if ( (cleaned_data['postalAddressLocation'] != 'None') and ( (cleaned_data['postalAddress']=='') or (cleaned_data['postalAddress']==None) ) ):
            self._errors["postalAddress"] = ["Please specify the address"] # Will raise a error message
            del cleaned_data['postalAddress']
        elif ( (cleaned_data['postalAddressLocation'] == 'None') and ( (cleaned_data['postalAddress']!='') and (cleaned_data['postalAddress']!=None) ) ):
            self._errors["postalAddressLocation"] = ["Please specify the address location"] # Will raise a error message
            del cleaned_data['postalAddressLocation']

    class Meta:
        model = Gradesheet
        exclude = ['disapproved', 'inprocess', 'approved', 'paymentApproved', 'paymentDisapproved', 'paymentInprocess', 'paidAmount', 'refNo', 'amtcal','form_no','posted','printed','remarks']
        labels = {
            'bitsID': _('Student ID'),
            'corrEmail': _('E-mail address'),
            'hostel': _('Hostel (Leave blank if not applicable)'),
            'roomNo': _('Room No. (Leave blank if not applicable)'),
            'ps2Station': _('PS-2 Station (Leave blank if not applicable)'),
            'forwardingLetters': _('Number of Forwarding Letters'),
            'sealedCopies': _('Number of Sealed Copies'),
            'phone_number': _('Phone Number'),
            'name': _('Name'),
            'postalAddress': _('Postal Address'),
            'postalAddressLocation': _('Postal Address Location'),
            'noOfSemesters': _('No of Semesters'),
        }

class GradesheetAddressForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(GradesheetAddressForm, self).clean()

    class Meta:
        model = SealedAddressGradesheet
        fields = ['addr','gradesheet']

class GradesheetForm2(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(GradesheetForm2, self).clean()

    class Meta:
        model = Gradesheet
        fields = []
        
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        sems = kwargs.pop('sems')
        sems = int(sems)
        extra = int(extra)
        super(GradesheetForm2, self).__init__(*args, **kwargs)
    
        for i in range(sems):
            self.fields['Year %s' % i] = forms.ChoiceField(choices = YEAR, label="", initial='', widget=forms.Select(), required=True)
            self.fields['Semester %s' % i] = forms.ChoiceField(choices = SEMESTER, label="", initial='', widget=forms.Select(), required=True)
            self.fields['Copies %s' % i] = forms.IntegerField(initial=1, validators = [MinValueValidator(1)])

        for i in range(extra):
            self.fields['Sealed address %s' % i] = forms.CharField(max_length=80)

class GradesheetForm3(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super(GradesheetForm3, self).clean()

    class Meta:
        model = Gradesheet
        fields = ['refNo','remarks']
        labels = {
            'refNo': _('SBI Payment Reference Number'),
            'remarks': _('Remarks (Optional)')
        }



# class ProjsectForm(forms.ModelForm):
#     studentID = forms.CharField(label='Student ID Number', widget=forms.Textarea)
#     studentName = forms.CharField(label='Student Name', widget=forms.Textarea)
#     projectTitle = forms.CharField(label='Proect Title', widget=forms.Textarea)



# class printBonafideForm(forms.Form):
#     text = forms.CharField(required=True, label='Body Text', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

# class DayPassForm(forms.ModelForm):
#     date = forms.CharField(label='Date', widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     time = forms.CharField(label='Out Time', widget=forms.TextInput(attrs={'class': 'timepicker'}))
#     intime = forms.CharField(label='In Time', widget=forms.TextInput(attrs={'class': 'timepicker'}))
#     def clean(self):
#         cleaned_data = super(DayPassForm, self).clean()
#         date = datetime.strptime(cleaned_data['date'], '%d %B, %Y').date()
#         time = datetime.strptime(cleaned_data['time'], '%H:%M').time()
#         intime = datetime.strptime(cleaned_data['intime'], '%H:%M').time()
#         date_time_start = datetime.combine(date, time)
#         if datetime.now() >= date_time_start:
#             self.add_error('date', "Daypass cannot be issued before the present date and time")
#         if (date_time_start-datetime.now()).days>2:
#             self.add_error('date', "Can apply for daypass within 2 days")
#         return cleaned_data

#     class Meta:
#         model = DayPass
#         exclude = ['student', 'approvedBy',
#                     'approved', 'comment', 'disapproved', 'inprocess', 'dateTime','inTime']
#         widgets = {
#             'reason': forms.Textarea(attrs={'class': 'materialize-textarea'}),
#             'corrAddress': forms.Textarea(attrs={'class': 'materialize-textarea validate'}),
#         }
#         labels = {
#             'corrAddress': _(" Location you're visiting "),
            
#         }
        
