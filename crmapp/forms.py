from django import forms
from django.forms import ModelForm
from .models import Counsellor, CourseModel, Batch, Payment, Enquiry, Admission


class CounsellorCreateForm(ModelForm):
    class Meta:
        model = Counsellor
        fields = "__all__"


class CourseCreateForm(ModelForm):
    class Meta:
        model = CourseModel
        fields = "__all__"


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = "__all__"


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"


class EnquiryForm(ModelForm):
    followup_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Enquiry
        fields = "__all__"



class FollowUpForm(forms.Form):
    followup_date=forms.DateField(widget=forms.SelectDateWidget(),required=False)

class AdmissionCreateForm(ModelForm):
    class Meta:
        model = Admission
        fields = "__all__"
