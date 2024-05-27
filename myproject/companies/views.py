from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompanyForm
from .models import Company

def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            return redirect('companies:registration_success', company_id=company.id)
    else:
        form = CompanyForm()
    return render(request, 'companies/register_company.html', {'form': form})

def registration_success(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'companies/registration_success.html', {'company': company})
