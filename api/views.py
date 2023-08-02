from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from api.exceptions import NoFileError, WrongFileFormatError
from api.serializers import CustomerSerializer
from customers.models import Customer, Deal
from customers.services import parse_csv_file


class CustomersListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.top_five_customers()


@api_view(http_method_names=['POST'])
def load_deals(request):
    file = request.FILES.get('deals')
    if file is None:
        raise NoFileError
    elif not file.name.endswith('.csv'):
        raise WrongFileFormatError
    try:
        deals = parse_csv_file(file)
    except Exception as e:
        raise APIException(e)
    Deal.objects.bulk_create(deals)
    return Response({'message': 'DONE'})
