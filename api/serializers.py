from django.core.cache import cache
from rest_framework import serializers

from customers.models import Customer
from customers.services import get_top_five_customers


class CustomerSerializer(serializers.ModelSerializer):
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')

    @staticmethod
    def get_gems(obj):
        gems = cache.get('gems')
        if gems:
            return gems
        my_gems = {deal.gem.name for deal in obj.deals.all()}
        top_five = get_top_five_customers()
        top_five.remove(obj)
        other_gems = set()
        for customer in top_five:
            other_gems.update({deal.gem.name for deal in customer.deals.all()})
        gems = list(my_gems.intersection(other_gems))
        cache.set('gems', gems)
        return gems
