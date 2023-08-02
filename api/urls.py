from django.urls import path

from api.views import load_deals, CustomersListView

urlpatterns = [
    path(
        'load_deals/',
        load_deals,
    ),
    path(
        'top_five_customers/',
        CustomersListView.as_view({'get': 'list'}),
    ),

]
