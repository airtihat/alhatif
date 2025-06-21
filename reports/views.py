from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Report
from .forms import ReportForm
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User

# تحقق من صلاحية المستخدم للوصول إلى الصفحات
def has_permission(user):
    # تحقق من أن المستخدم لديه صلاحية معينة للوصول
    return user.is_staff or user.groups.filter(name='Admin').exists()  # مثال على توسيع صلاحيات المستخدم

# ✅ عرض رئيسي - /reports/
@login_required
@user_passes_test(has_permission)
def report_home(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

# ✅ صفحة إرسال تقرير جديد - /reports/submit/
@login_required
@user_passes_test(has_permission)
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)  # تأكد من إرسال الملفات مع النموذج
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  # تعيين المستخدم الحالي للتقرير
            report.save()
            messages.success(request, 'تم إرسال التقرير بنجاح ✅')
            return redirect('reports:report_home')  # الرجوع إلى قائمة التقارير
    else:
        form = ReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})

# ✅ عرض تفاصيل تقرير - /reports/<id>/
@login_required
@user_passes_test(has_permission)
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})

# ✅ تحميل تقرير - /reports/<id>/download/
@login_required
@user_passes_test(has_permission)
def report_download(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    
    # فرضًا أن عندك ملف PDF محفوظ داخل report.file
    response = HttpResponse(report.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{report.subject}.pdf"'
    return response
