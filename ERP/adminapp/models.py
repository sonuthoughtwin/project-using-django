from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


from django.db.models.fields import CharField


class Branch(models.Model):
    branch=models.CharField(max_length=100)
    def __str__(self):
        return self.branch

class Course(models.Model):
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
    duration=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    branch=models.ForeignKey(Branch,on_delete=CASCADE)
    def __str__(self):
        return self.course

class Designation(models.Model):
    designation=models.CharField(max_length=100)
    def __str__(self):
        return self.designation

class Payment(models.Model):
    paymentId=models.CharField(max_length=100)
    mode=models.CharField(max_length=100)

class Enquirysource(models.Model):
    enquiry=models.CharField(max_length=100)

class Staff(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    joindate=models.DateField()
    designation=models.ForeignKey(Designation,on_delete=CASCADE)
    experience=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    identification=models.CharField(max_length=100)
    idnumber=models.CharField(max_length=100)
    branchId=models.ForeignKey(Branch,on_delete=CASCADE)
    def __str__(self):
        return self.name

class StudentEnquiry(models.Model):
    fullname=models.CharField(max_length=100)
    mobileNo=models.CharField(max_length=100)
    dob=models.DateField()
    clgName=models.CharField(max_length=100)
    highQualification=models.CharField(max_length=100)
    enquiryDate=models.DateField()
    courseId=models.ForeignKey(Course,on_delete=CASCADE)
    enqsrcId=models.ForeignKey(Enquirysource,on_delete=CASCADE)
    branchId=models.ForeignKey(Branch,on_delete=CASCADE)
    staffId=models.ForeignKey(Staff,on_delete=CASCADE)
    pfdj=models.DateField()
    status=models.CharField(max_length=100)
    remark=models.CharField(max_length=100)
class StuRegistration(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=CASCADE)
    regDate=models.DateField()
    totalfee=models.IntegerField()
    discountfee=models.IntegerField()
    paymentRefNo=models.CharField(max_length=100)
    staffId=models.ForeignKey(Staff,on_delete=CASCADE)
    branch=models.ForeignKey(Branch,on_delete=CASCADE)
    remark=models.CharField(max_length=100)
    regStatus=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class Fee(models.Model):
    regId=models.ForeignKey(StuRegistration,on_delete=CASCADE)
    feedate=models.DateField()
    totalfee=models.IntegerField()
    installment=models.CharField(max_length=100)
    discountfee=models.IntegerField()
    submitedfee=models.IntegerField()
    remainingfee=models.IntegerField()
    staffid=models.ForeignKey(Staff,on_delete=CASCADE)
    paymentId=models.ForeignKey(Payment,on_delete=CASCADE)
    paymentRefNo=models.CharField(max_length=100)
    receiptNo=models.IntegerField()
    branch=models.ForeignKey(Branch,on_delete=CASCADE)
    remark=models.CharField(max_length=100)







