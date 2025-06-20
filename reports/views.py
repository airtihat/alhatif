from django.shortcuts import render, redirect
from django.contrib import messages
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
