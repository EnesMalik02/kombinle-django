from django.shortcuts import render

def ana_sayfa(request):
    return render(request, 'veriler/ana_sayfa.html')  # ana_sayfa.html şablonuna yönlendirme

def filtrele(request):
    return render(request, 'veriler/filtrele.html')  # filtrele.html adlı bir şablona yönlendirme
