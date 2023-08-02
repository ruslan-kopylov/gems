from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')

    @staticmethod
    def get_gems(obj):
        my_gems = {deal.gem.name for deal in obj.deals.all()}
        top_five = Customer.top_five_customers()
        top_five.remove(obj)
        other_gems = set()
        for customer in top_five:
            other_gems.update({deal.gem.name for deal in customer.deals.all()})
        return list(my_gems.intersection(other_gems))
