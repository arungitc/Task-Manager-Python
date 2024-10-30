from django.shortcuts import render
from .models import Report
from .forms import ReportForm, CustomUserRegistrationForm
# UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
import csv
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def report_list(request):
    reports = Report.objects.all().order_by('-created_at')

    
    return render(request, 'main.html', 
                  {'reports': reports})

@login_required
def report_create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('report_list')
    else:
      form = ReportForm()
    return render(request, 'report_form.html',
                  {'form': form})

@login_required
def report_edit(request, report_id):
    report = get_object_or_404(Report, pk=report_id, user = 
                               request.user)
    if request.method == 'POST':
      form = ReportForm(request.POST, request.FILES, 
                        instance=report)
      if form.is_valid():
         report = form.save(commit=False)
         report.user = request.user
         report.save()
         return redirect('report_list')
      pass
    else:
      form = ReportForm(instance=report)
    return render(request, 'report_form.html',
                  {'form': form})

@login_required
def report_delete(request, report_id):
   report = get_object_or_404(Report, pk=report_id, 
                     user = request.user)
   if request.method == "POST":
      report.delete()
      return redirect('report_list')
   return render(request, 'report_confirm_delete.html',
                  {'report': report})





# def register(request):
#    if request.method == 'POST':
#       form = UserRegistrationForm(request.POST)
#       if form.is_valid():
#          user = form.save(commit=False)
#          user.set_password(form.cleaned_data['password1'])
#          user.save()
#          login(request, user)
#          return redirect('report_list')
#    else:
#       form = UserRegistrationForm()
#    return render(request, 'registration/register.html',
#                   {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('report_list')  # Redirect to a home page or wherever you want
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# def logged_out(request):
#     logout(request)
#     return render(request, 'logged_out.html')  # Redirect to the homepage or any other page


# def login(request):
#    return render(request, 'registration/login.html')



def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Table-data.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'DocId', 'Name of Institutes','Head', 'Subject', 'Email ID', 'Date', 'PDF', 'Other Pdf'])  # Header row

    for obj in Report.objects.all():
        writer.writerow([obj.user, obj.docId, obj.Name_of_Institutes, obj.head_under_project_website, 
                         obj.subject, obj.email, obj.date,obj.pdf_link, obj.other_pdf, 
                          ])  # Data rows

    return response

  
   
