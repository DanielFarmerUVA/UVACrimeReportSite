from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.files.storage import default_storage
import boto3
from .models import Report
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    return render(request,"home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def report(request):
    api_key = settings.GOOGLE_MAPS_API_KEY
    if request.method == 'POST' and request.POST.get('action') == 'report':
        return render(request, 'report.html',{'api_key': api_key})
    # Create your views here.
    return render(request, 'report.html',{'api_key': api_key})

def report_upload(request):
    if request.method == 'POST':
        lastName = request.POST.get('lastName', '')
        firstName = request.POST.get('firstName', '')

        email = request.POST.get('email', '')

        crimeType = request.POST.get('crimeType', '')
        subject = request.POST.get('subject', 'No Subject')
        timeOfIncident = request.POST.get('timeOfIncident', '')

        reportDescription = request.POST.get('reportDescription', '')
        descriptionItems = request.POST.get('descriptionItems', '')
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)


        file = request.FILES.get('reportFile', None)
        discussion = request.POST.get('discussion', '')

        report = Report(email = email, 
        crimeType = crimeType,
        subject = subject,
        timeOfIncident = timeOfIncident,
        reportDescription=reportDescription,
        discussion = discussion
        )
        if file:
            report.file = file

        if latitude and longitude:
            report.latitude = float(latitude)
            report.longitude = float(longitude)

        if lastName and firstName:
            report.lastName = lastName
            report.firstName = firstName
        if descriptionItems:
            report.descriptionItems = descriptionItems


        report.save()
        if email:
            send_mail(
                'Report Submission Confirmation', 
                f"Your report is #{report.id} and has been received. We will review it and update you on its status.",
                "noreply.admin@gmail.com", 
                [email]
                )
        return render(request, 'submitted.html')
    else:
        return render(request, 'report.html')

    # return render(request, 'report.html')

def anon_home(request):
    return render(request, "anon_login.html")

def user_home(request):
    if(request.user.email):
        user_email = request.user.email  # Assuming your User model has an email field
        user_reports = Report.objects.filter(email=user_email)  # Fetch reports by the user's email
        return render(request, 'user-home.html', {'user_reports': user_reports})

def admin_home(request):
    s3_client = boto3.client('s3')
    
    # Get list of objects (submissions) from the S3 bucket
    bucket_name = 'a-03-static'
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    # Submission data from S3 response
    submissions = []
    if 'Contents' in response:
        for obj in response['Contents']:
            submissions.append(obj['Key'])
    
    # Fetch report data from the database
    reports = Report.objects.all()

    # Set status to "New" for reports that have no status set
    for report in reports:
        if not report.status:
            report.status = 'New'
            report.save()

    # Pass both submissions and reports data to the template
    return render(request, 'admin-home.html', {'submissions': submissions, 'reports': reports})


def change_status(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        notes = request.POST.get('notes', '')
        report.status = status
        report.notes = notes
        report.save()
        return redirect('admin_home')

    return render(request, 'admin-home.html', {'reports': Report.objects.all()})



def admin_report_detail(request, report_id):
    if not (request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)):
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    report = get_object_or_404(Report, id=report_id)
    api_key = settings.GOOGLE_MAPS_API_KEY

    # Update status to 'In Progress' if status is 'New'
    if report.status == 'New':
        report.status = 'In Progress'
        report.save()
    
    if request.method == 'POST':
        if 'note' in request.POST:
            note = request.POST.get('note')
            previous_status = report.status
            report.notes = note
            report.status = 'Resolved'

            send_mail(
                'Report Resolved', 
                f"Your report is #{report.id} is resolved. View the notes through the user dashboard.",
                "noreply.admin@gmail.com", 
                [report.email])
            report.save()
    context = {
        'report': report,
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'is_admin_view': True  # Indicate this is an admin view
    }

    return render(request, 'report_detail.html', context)


def user_report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    context = {
        'report': report,
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'is_admin_view': False  # Indicate this is not an admin view
    }
    return render(request, 'report_detail.html', context)