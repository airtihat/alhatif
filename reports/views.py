from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages
from .forms import ReportForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Report
from .forms import ReportForm



def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, 'تم إرسال التقرير بنجاح ✅')
            return redirect('reports:submit_report')
    else:
        form = ReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})

def report_home(request):
    return render(request, 'reports/report_list.html')



# ✅ عرض رئيسي - /reports/
def report_home(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

# ✅ صفحة إرسال تقرير جديد - /reports/submit/
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_home')  # يرجع إلى قائمة التقارير
    else:
        form = ReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})

# ✅ عرض تفاصيل تقرير - /reports/<id>/
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})

# ✅ تحميل تقرير - /reports/<id>/download/
def report_download(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    
    # فرضًا أن عندك ملف PDF محفوظ داخل report.file
    response = HttpResponse(report.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{report.subject}.pdf"'
    return response
