from .models import Asset
from django.views.generic import DetailView, ListView


class AssetListView(ListView):
    model = Asset


class AssetDetailView(DetailView):
    model = Asset


# from django.shortcuts import render, get_object_or_404

# def index(request):
#     result = Asset.objects.order_by('-symbol')[:5]
#     context = {
#         'result': result,
#     }
#
#     return render(request, 'assets/index.html', context)
#
#
# def detail(request, symbol):
#     result = get_object_or_404(Asset, symbol=symbol)
#     return render(request, 'assets/detail.html', {'result': result})
