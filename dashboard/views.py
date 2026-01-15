from django.shortcuts import render
from dashboard.models import StudentEnquiry

# def dashboard_home(request):
#     return render(request, 'main/index.html')

def dashboard_home(request):
    return render(request, 'main/index.html')

def home(request):
    success = False

    if request.method == "POST":
        StudentEnquiry.objects.create(
            name=request.POST.get('name'),
            qualification=request.POST.get('qualification'),
            interested_course=request.POST.get('course'),
            contact_number=request.POST.get('contact'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        success = True

    return render(request, 'main/index_home.html', {'success': success})