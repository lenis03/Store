from django.shortcuts import render
from django.db.models import Q, F

from store import models


def show_data(request):
    quesry_set = models.OrderItem.objects.values_list('product').distinct()
    print(list(quesry_set))
    products = models.Product.objects.filter(id__in=quesry_set)
    return render(request, 'store/index.html', {'products': list(products)})
