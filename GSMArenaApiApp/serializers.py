from rest_framework import serializers

from GSMArenaApiApp.models import Phone
from GSMArenaApiApp.utils import getRate


class PhoneSerializer(serializers.ModelSerializer):
    priceUSD = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = "__all__"

    def get_priceUSD(self, obj):
        price = obj.price.replace('&thinsp;', '')
        try:
            aux = price.split(' / ')[0].split(';')
            simbol = aux[0] + ";"
            amount = float(aux[1].replace(',', ''))
            usdPrice = getRate(simbol, amount)
        except:
            if 'About' in price:
                aux = price.split(" ")
                coin = aux[2]
                amount = float(aux[1])
                usdPrice = getRate('', amount, coin)
        return usdPrice