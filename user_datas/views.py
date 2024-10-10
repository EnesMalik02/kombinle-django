# myapp/views.py
from django.shortcuts import render
from .models import ClothingSearch
from django.db.models import Count

def search_results(request):
    # Query parameters from the URL (optional filtering)
    country = ['Turkey', 'Germany', 'France', 'USA', 'UK']
    age = 18
    gender = ["Erkek", "Kadın"]
    
    # Sorguya göre filtreleme
    filters = {}
    if country:
        filters['country'] = country
    if age:
        filters['age'] = age
    if gender:
        filters['gender'] = gender
    
    # Filtreye göre sorgulama ve en çok aranan kelimeleri sayıp sıralama
    results = ClothingSearch.objects.filter(**filters).values('search_term').annotate(count=Count('search_term')).order_by('-count')
    
    return render(request, 'myapp/search_results.html', {'results': results, 'country': country, 'age': age, 'gender': gender})
