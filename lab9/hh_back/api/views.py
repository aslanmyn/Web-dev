from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy

def get_companies(request):
    companies = Company.objects.all()
    data = {'companies': list(companies.values())}
    return JsonResponse(data)

def get_company(request, id):
    company = get_object_or_404(Company, pk=id)
    data = {'company': model_to_dict(company)}
    return JsonResponse(data)

def get_company_vacancies(request, id):
    company = get_object_or_404(Company, pk=id)
    vacancies = company.vacancy_set.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def get_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, pk=id)
    data = {'vacancy': model_to_dict(vacancy)}
    return JsonResponse(data)

def get_top_ten_vacancies(request):
    top_ten_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'top_ten_vacancies': list(top_ten_vacancies.values())}
    return JsonResponse(data)
