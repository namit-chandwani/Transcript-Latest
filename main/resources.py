from .models import *
from import_export import resources, fields
from import_export.fields import Field

# class ProjectResource(resources.ModelResource):
#     class Meta:
#         model = Project
#         fields = ('faculty__name','studentId', 'studentname', 'department', 'courseCode','title','approved')
#         export_order = ('faculty__name','studentId', 'studentname', 'department', 'courseCode','title','approved')
#         verbose_name = True

class TranscriptResource(resources.ModelResource):
    class Meta:
        model = Transcript
        fields = ('bitsID', 'refNo','name','phone_number','corrEmail','gradStatus','hostel','roomNo','ps2Station','origTranscript','dupTranscripts','forwardingLetters','sealedCopies','amtcal','paidAmount','postalAddressLocation','postalAddress','remarks','soft_hard_copy','paymentApproved','paymentDisapproved','paymentInprocess','approved','disapproved','printed','posted','inprocess')
        export_order = ('bitsID', 'refNo','name','phone_number','corrEmail','gradStatus','hostel','roomNo','ps2Station','origTranscript','dupTranscripts','forwardingLetters','sealedCopies','amtcal','paidAmount','postalAddressLocation','postalAddress','remarks','soft_hard_copy','paymentApproved','paymentDisapproved','paymentInprocess','approved','disapproved','printed','posted','inprocess')
        

    addr1 = Field(column_name='Address 1')
    addr2 = Field(column_name='Address 2')
    addr3 = Field(column_name='Address 3')
    addr4 = Field(column_name='Address 4')
    addr5 = Field(column_name='Address 5')
    addr6 = Field(column_name='Address 6')
    addr7 = Field(column_name='Address 7')
    addr8 = Field(column_name='Address 8')
    addr9 = Field(column_name='Address 9')
    addr10 = Field(column_name='Address 10')
    

    def dehydrate_addr1(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 0):
    		return addrs[0].addr
    	else:
    		return ""

    def dehydrate_addr2(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 1):
    		return addrs[1].addr
    	else:
    		return ""

    def dehydrate_addr3(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 2):
    		return addrs[2].addr
    	else:
    		return ""

    def dehydrate_addr4(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 3):
    		return addrs[3].addr
    	else:
    		return ""

    def dehydrate_addr5(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 4):
    		return addrs[4].addr
    	else:
    		return ""

    def dehydrate_addr6(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 5):
    		return addrs[5].addr
    	else:
    		return ""

    def dehydrate_addr7(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 6):
    		return addrs[6].addr
    	else:
    		return ""

    def dehydrate_addr8(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 7):
    		return addrs[7].addr
    	else:
    		return ""

    def dehydrate_addr9(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 8):
    		return addrs[8].addr
    	else:
    		return ""

    def dehydrate_addr10(self, Transcript):
    	addrs = SealedAddress.objects.filter(transcript=Transcript)
    	if (len(addrs) > 9):
    		return addrs[9].addr
    	else:
    		return ""

class GradesheetResource(resources.ModelResource):
    class Meta:
        model = Gradesheet
        fields = ('bitsID', 'refNo','name','phone_number','corrEmail','hostel','roomNo','ps2Station','noOfSemesters','sealedCopies','amtcal','paidAmount','postalAddressLocation','postalAddress','remarks','paymentApproved','paymentDisapproved','paymentInprocess','approved','disapproved','printed','posted','inprocess')
        export_order = ('bitsID', 'refNo','name','phone_number','corrEmail','hostel','roomNo','ps2Station','noOfSemesters','sealedCopies','amtcal','paidAmount','postalAddressLocation','postalAddress','remarks','paymentApproved','paymentDisapproved','paymentInprocess','approved','disapproved','printed','posted','inprocess')
        

    addr1 = Field(column_name='Address 1')
    addr2 = Field(column_name='Address 2')
    addr3 = Field(column_name='Address 3')
    addr4 = Field(column_name='Address 4')
    addr5 = Field(column_name='Address 5')
    addr6 = Field(column_name='Address 6')
    addr7 = Field(column_name='Address 7')
    addr8 = Field(column_name='Address 8')
    addr9 = Field(column_name='Address 9')
    addr10 = Field(column_name='Address 10')

    sem1 = Field(column_name="Semester_1")
    year1 = Field(column_name="Year_1")
    copies1 = Field(column_name="Copies_1")
    sem2 = Field(column_name="Semester_2")
    year2 = Field(column_name="Year_2")
    copies2 = Field(column_name="Copies_2")
    sem3 = Field(column_name="Semester_3")
    year3 = Field(column_name="Year_3")
    copies3 = Field(column_name="Copies_3")
    sem4 = Field(column_name="Semester_4")
    year4 = Field(column_name="Year_4")
    copies4 = Field(column_name="Copies_4")
    sem5 = Field(column_name="Semester_5")
    year5 = Field(column_name="Year_5")
    copies5 = Field(column_name="Copies_5")
    sem6 = Field(column_name="Semester_6")
    year6 = Field(column_name="Year_6")
    copies6 = Field(column_name="Copies_6")
    sem7 = Field(column_name="Semester_7")
    year7 = Field(column_name="Year_7")
    copies7 = Field(column_name="Copies_7")
    sem8 = Field(column_name="Semester_8")
    year8 = Field(column_name="Year_8")
    copies8 = Field(column_name="Copies_8")
    sem9 = Field(column_name="Semester_9")
    year9 = Field(column_name="Year_9")
    copies9 = Field(column_name="Copies_9")
    sem10 = Field(column_name="Semester_10")
    year10 = Field(column_name="Year_10")
    copies10 = Field(column_name="Copies_10")
    sem11 = Field(column_name="Semester_11")
    year11 = Field(column_name="Year_11")
    copies11 = Field(column_name="Copies_11")
    sem12 = Field(column_name="Semester_12")
    year12 = Field(column_name="Year_12")
    copies12 = Field(column_name="Copies_12")
    sem13 = Field(column_name="Semester_13")
    year13 = Field(column_name="Year_13")
    copies13 = Field(column_name="Copies_13")
    sem14 = Field(column_name="Semester_14")
    year14 = Field(column_name="Year_14")
    copies14 = Field(column_name="Copies_14")
    
    def dehydrate_addr1(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 0):
    		return addrs[0].addr
    	else:
    		return ""

    def dehydrate_addr2(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 1):
    		return addrs[1].addr
    	else:
    		return ""

    def dehydrate_addr3(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 2):
    		return addrs[2].addr
    	else:
    		return ""

    def dehydrate_addr4(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 3):
    		return addrs[3].addr
    	else:
    		return ""

    def dehydrate_addr5(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 4):
    		return addrs[4].addr
    	else:
    		return ""

    def dehydrate_addr6(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 5):
    		return addrs[5].addr
    	else:
    		return ""

    def dehydrate_addr7(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 6):
    		return addrs[6].addr
    	else:
    		return ""

    def dehydrate_addr8(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 7):
    		return addrs[7].addr
    	else:
    		return ""

    def dehydrate_addr9(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 8):
    		return addrs[8].addr
    	else:
    		return ""

    def dehydrate_addr10(self, Gradesheet):
    	addrs = SealedAddressGradesheet.objects.filter(gradesheet=Gradesheet)
    	if (len(addrs) > 9):
    		return addrs[9].addr
    	else:
    		return ""

    def dehydrate_sem1(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 0):
    		return grads[0].semester
    	else:
    		return ""

    def dehydrate_year1(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 0):
    		return grads[0].year
    	else:
    		return ""

    def dehydrate_copies1(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 0):
    		return grads[0].copies
    	else:
    		return ""
    
    def dehydrate_sem2(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 1):
    		return grads[1].semester
    	else:
    		return ""

    def dehydrate_year2(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 1):
    		return grads[1].year
    	else:
    		return ""

    def dehydrate_copies2(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 1):
    		return grads[1].copies
    	else:
    		return ""
    
    def dehydrate_sem3(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 2):
    		return grads[2].semester
    	else:
    		return ""

    def dehydrate_year3(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 2):
    		return grads[2].year
    	else:
    		return ""

    def dehydrate_copies3(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 2):
    		return grads[2].copies
    	else:
    		return ""
    
    def dehydrate_sem4(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 3):
    		return grads[3].semester
    	else:
    		return ""

    def dehydrate_year4(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 3):
    		return grads[3].year
    	else:
    		return ""

    def dehydrate_copies4(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 3):
    		return grads[3].copies
    	else:
    		return ""
    
    def dehydrate_sem5(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 4):
    		return grads[4].semester
    	else:
    		return ""

    def dehydrate_year5(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 4):
    		return grads[4].year
    	else:
    		return ""

    def dehydrate_copies5(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 4):
    		return grads[4].copies
    	else:
    		return ""
    
    def dehydrate_sem6(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 5):
    		return grads[5].semester
    	else:
    		return ""

    def dehydrate_year6(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 5):
    		return grads[5].year
    	else:
    		return ""

    def dehydrate_copies6(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 5):
    		return grads[5].copies
    	else:
    		return ""
    
    def dehydrate_sem7(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 6):
    		return grads[6].semester
    	else:
    		return ""

    def dehydrate_year7(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 6):
    		return grads[6].year
    	else:
    		return ""

    def dehydrate_copies7(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 6):
    		return grads[6].copies
    	else:
    		return ""
    
    def dehydrate_sem8(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 7):
    		return grads[7].semester
    	else:
    		return ""

    def dehydrate_year8(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 7):
    		return grads[7].year
    	else:
    		return ""

    def dehydrate_copies8(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 7):
    		return grads[7].copies
    	else:
    		return ""
    
    def dehydrate_sem9(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 8):
    		return grads[8].semester
    	else:
    		return ""

    def dehydrate_year9(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 8):
    		return grads[8].year
    	else:
    		return ""

    def dehydrate_copies9(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 8):
    		return grads[8].copies
    	else:
    		return ""
    
    def dehydrate_sem10(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 9):
    		return grads[9].semester
    	else:
    		return ""

    def dehydrate_year10(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 9):
    		return grads[9].year
    	else:
    		return ""

    def dehydrate_copies10(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 9):
    		return grads[9].copies
    	else:
    		return ""
    
    def dehydrate_sem11(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 10):
    		return grads[10].semester
    	else:
    		return ""

    def dehydrate_year11(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 10):
    		return grads[10].year
    	else:
    		return ""

    def dehydrate_copies11(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 10):
    		return grads[10].copies
    	else:
    		return ""
    
    def dehydrate_sem12(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 11):
    		return grads[11].semester
    	else:
    		return ""

    def dehydrate_year12(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 11):
    		return grads[11].year
    	else:
    		return ""

    def dehydrate_copies12(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 11):
    		return grads[11].copies
    	else:
    		return ""
    
    def dehydrate_sem13(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 12):
    		return grads[12].semester
    	else:
    		return ""

    def dehydrate_year13(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 12):
    		return grads[12].year
    	else:
    		return ""

    def dehydrate_copies13(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 12):
    		return grads[12].copies
    	else:
    		return ""
    
    def dehydrate_sem14(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 13):
    		return grads[13].semester
    	else:
    		return ""

    def dehydrate_year14(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 13):
    		return grads[13].year
    	else:
    		return ""

    def dehydrate_copies14(self, Gradesheet):
    	grads = GradesheetCopies.objects.filter(gradesheet=Gradesheet)
    	if (len(grads) > 13):
    		return grads[13].copies
    	else:
    		return ""
    