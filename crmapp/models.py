from django.db import models
from datetime import date


# Create your models here.
class Counsellor(models.Model):
    counsellor_id = models.CharField(max_length=60, primary_key=True)
    counsellor_name = models.CharField(max_length=120)
    phone_no = models.IntegerField(max_length=12)


class CourseModel(models.Model):
    Course_name = models.CharField(max_length=120, unique=True)
    duration = models.FloatField(max_length=20)

    def __str__(self):
        return self.Course_name


class Batch(models.Model):
    STATUS = (
        ('B', 'yet to Begin'),
        ('G', 'onGoing'),
        ('C', 'Completed'),
    )
    batch_code = models.CharField(max_length=80, unique=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    starting_date = models.DateField(default=date.today())
    course_fee = models.FloatField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return str(self.batch_code) + str(self.course)


class Enquiry(models.Model):
    STUD_STATUS = (
        (0, 'Pending'),
        (1, 'Admitted'),
        (2, 'Cancel'),
    )
    Counsellor_id = models.ForeignKey(Counsellor, on_delete=models.CASCADE)
    enquiry_id = models.CharField(max_length=60, primary_key=True)
    student_name = models.CharField(max_length=120)
    phone_no = models.IntegerField(max_length=12)
    email = models.CharField(max_length=20)
    qualification = models.CharField(max_length=60)
    college_name = models.CharField(max_length=100)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    enquiry_date = models.DateField(default=date.today())
    followup_date = models.DateField()
    stud_status = models.IntegerField(max_length=1, choices=STUD_STATUS)

    def __str__(self):
        return str(self.enquiry_id)


class Admission(models.Model):
    admission_no = models.CharField(max_length=10, unique=True)
    enquiry_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE)

    fees = models.FloatField(max_length=60)
    batch_code = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())

    def __str__(self):
        return str(self.admission_no) + str(self.fees)


class Payment(models.Model):
    FEE_STATUS = (
        ('0', 'Pending'),
        ('1', 'Paid'),

    )
    admission_no = models.ForeignKey(Admission, on_delete=models.CASCADE)
    Amount = models.IntegerField(max_length=60)
    payment_date = models.DateField(default=date.today())
    payment_status = models.IntegerField(max_length=1, choices=FEE_STATUS)

    def __str__(self):
        return self.Amount
