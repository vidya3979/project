from datetime import date

from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, ListView

from crmapp.forms import CounsellorCreateForm, AdmissionCreateForm, EnquiryForm, CourseCreateForm, BatchForm, \
    PaymentForm, FollowUpForm
from crmapp.models import Counsellor, Enquiry, CourseModel, Batch, Payment, Admission
from django.contrib.auth.decorators import login_required


def adminpage(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("password")
        if uname == 'vid123' and pwd == 'vidya3979':
            return render(request, "crmapp/base.html")
        else:
            return render(request, "crmapp/adminlogin.html")
    return render(request, "crmapp/adminlogin.html")


def log_out(request):
    logout(request)
    return redirect("adminlogin")


class CreateCounsellor(TemplateView):
    model = Counsellor
    form_class = CounsellorCreateForm
    context = {}
    template_name = "crmapp/counsellor_create.html"

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("View_Counsellor")
        return render(request, self.template_name, self.context)


class ListCounsellor(TemplateView):
    model = Counsellor
    context = {}
    template_name = "crmapp/viewcounsellor.html"

    def get(self, request, *args, **kwargs):
        counsellor = self.model.objects.all()
        self.context["counsellor"] = counsellor
        return render(request, self.template_name, self.context)


class UpdateCounsellor(TemplateView):
    model = Counsellor
    form_class = CounsellorCreateForm
    template_name = "crmapp/counsellor_create.html"
    context = {}

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        counsellor = self.model.objects.get(id=id)
        form = self.form_class(instance=counsellor)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        counsellor = self.get_object(id)
        form = self.form_class(request.POST, instance=counsellor)
        if form.is_valid():
            form.save()
            return redirect("View_Counsellor")
        self.context["form"] = form
        return render(request, self.template_name, self.context)


class DeleteCounsellor(DeleteView):
    model = Counsellor
    context_object_name = "Counsellor"
    success_url = reverse_lazy("View_Counsellor")


class CreateCourse(TemplateView):
    model = CourseModel
    form_class = CourseCreateForm
    context = {}
    template_name = "crmapp/course_create.html"

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("View_course")
        return render(request, self.template_name, self.form)


class ViewCourse(TemplateView):
    model = CourseModel
    context = {}
    template_name = "crmapp/viewcourse.html"

    def get(self, request, *args, **kwargs):
        courses = self.model.objects.all()
        self.context["courses"] = courses
        return render(request, self.template_name, self.context)


class UpdateCourse(TemplateView):
    model = CourseModel
    form_class = CourseCreateForm
    template_name = "crmapp/course_create.html"
    context = {}

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        course = self.model.objects.get(id=id)
        form = self.form_class(instance=course)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        course = self.get_object(id)
        form = self.form_class(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("View_course")
        self.context["form"] = form
        return render(request, self.template_name, self.context)


class DelCourse(DeleteView):
    model = CourseModel
    context_object_name = "CourseModel"
    success_url = reverse_lazy("View_course")


class CreateBatch(TemplateView):
    model = Batch
    form_class = BatchForm
    context = {}
    template_name = "crmapp/batch_create.html"

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("View_Batch")
        return render(request, self.template_name, self.context)


class UpdateBatch(TemplateView):
    model = Batch
    form_class = BatchForm
    template_name = "crmapp/batch_create.html"
    context = {}

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        batch = self.model.objects.get(id=id)
        form = self.form_class(instance=batch)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        batch = self.get_object(id)
        form = self.form_class(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect("View_Batch")
        self.context["form"] = form
        return render(request, self.template_name, self.context)


class DelBatch(DeleteView):
    model = Batch
    context_object_name = "Batch"
    success_url = reverse_lazy("View_Batch")


class ViewBatch(TemplateView):
    model = Batch
    context = {}
    template_name = "crmapp/viewbatch.html"

    def get(self, request, *args, **kwargs):
        batches = self.model.objects.all()
        self.context['batches'] = batches
        return render(request, self.template_name, self.context)


class CreatePayment(TemplateView):
    model = Payment
    form_class = PaymentForm
    context = {}
    template_name = "crmapp/payment_create.html"

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("View_Payment")
        return render(request, self.template_name, self.context)


class ViewPayment(TemplateView):
    model = Payment
    context = {}
    template_name = "crmapp/viewpayment.html"

    def get(self, request, *args, **kwargs):
        payments = self.model.objects.all()
        self.context['payments'] = payments
        return render(request, self.template_name, self.context)


class CreateEnquiry(TemplateView):
    model = Enquiry
    form_class = EnquiryForm
    template_name = "crmapp/create_enquiry.html"

    def get(self, request, *args, **kwargs):
        enquiry = self.model.objects.last()
        if enquiry:

            last_enquiryid = enquiry.enquiry_id
            lst = int(last_enquiryid.split("-")[1]) + 1
            enquiry_id = "EID-" + str(lst)

        else:
            enquiry_id = "EID-1000"

        form = self.form_class(initial={"enquiry_id": enquiry_id})
        students = Enquiry.objects.all()
       # paginator = Paginator(students, 3)
       # page_num = request.GET.get("page")
       # page_obj = paginator.get_page(page_num)
        self.context = {
            "form": form,
            "students":students
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            students = Enquiry.objects.all()
            self.context = {
                "form": self.form_class,
                "students": students
            }
            return redirect("Create_Enquiry")
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)


def load_course(request):
    course_id = request.GET.get("course_id")
    batches = Batch.objects.filter(course_name=course_id).all()
    return render(request, "crmapp/course_dropdown.html", {'batches': batches})


class Update_Enquiry(TemplateView):
    model = Enquiry
    form_class = EnquiryForm
    template_name = "crmapp/create_enquiry.html"

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        students = self.get_object(id)
        form = self.form_class(instance=students)
        self.context = {
            "form": form
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        students = self.get_object(id)
        form = self.form_class(request.POST, instance=students)
        self.context = {
            "form": form
        }
        if form.is_valid():
            form.save()
            return redirect("Create_Enquiry")
        return render(request, self.template_name, self.context)


class Enquiry_Delete(TemplateView):
    model = Enquiry

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        student = self.get_object(id)
        student.delete()
        return redirect("Create_Enquiry")


class SearchFollowUp(TemplateView):
    model = Enquiry
    template_name = "crmapp/listFollowup.html"

    def get(self, request, *args, **kwargs):
        dates = Enquiry.objects.filter(followup_date=date.today())
        self.context = {
            "dates": dates
        }
        return render(request, self.template_name, self.context)


class Create_Admission(TemplateView):
    model = Admission
    form_class = AdmissionCreateForm
    template_name = "crmapp/admission.html"

    def get_object(self, id):
        return Enquiry.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        admission = self.get_object.last()
        id = kwargs.get("id")
        students = self.get_object(id)

        if admission:
            last_adm = admission.admission_no
            lst = int(last_adm.split('-')[1]) + 1
            admission_no = 'LMNR-' + str(lst)

        else:
            admission_no = 'LMNR-1000'
            admission = Admission.objects.all()[::-1]
            eid = students.enquiry_id
            batch = students.batch
            form = self.form_class(initial={'admission_no': admission_no, 'eid': eid, 'batch_code': batch})
            paginator = Paginator(admission, 3)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)
            self.context = {
                "form": form,
                "page_obj": page_obj
            }

            return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            admission = Admission.objects.all()
            self.context = {
                "form": self.form_class,
                "admission": admission
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)
