from django.urls import path
from . import views

from .views import (barcodedeleteview, barcodeapiView, barcodefileapiView, BarcodeGenerateView, Barcodedeleteview, codeGenerateView)

urlpatterns = [
    path('', views.index, name='index'),
    # path('barcodedata/', barcodelistview.as_view(), name='barcodelistview'),
    path('barcode-generator/<int:pk>/', barcodedeleteview.as_view(), name='barcodedeleteview'),
    path('barcode-generator/', barcodeapiView.as_view(), name='barcodeapiView'),

    # path('barcodedatafile/', barcodefilelistview.as_view(), name='barcodefilelistview'),
    # path('barcode-creator/<int:pk>/', barcodefiledeleteview.as_view(), name='barcodefiledeleteview'),
    path('barcode-creator/', barcodefileapiView.as_view(), name='barcodefileapiView'),

    # path('Barcodeindata/', Barcodeinlistview.as_view(), name='Barcodeinlistview'),
    path('barcode/', BarcodeGenerateView.as_view(), name='BarcodeGenerateView'),
    path('barcode/<int:pk>/', Barcodedeleteview.as_view(), name='Barcodedeleteview'),


    # path('codeindata/', codeinlistview.as_view(), name='codeinlistview'),
    path('barcodecreate/', codeGenerateView.as_view(), name='codeGenerateView'),
    # path('barcodecreate/<int:pk>/', codedeleteview.as_view(), name='codedeleteview'),
]