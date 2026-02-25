from rest_framework import serializers
from .models import (
    Kategoriya, XizmatKorsatishNuqtasi, Mahsulot,
    Aviakompaniya, Parvoz, Yolovchi, Chipta, Bagaj, Xodim
)


class KategoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = '__all__'


class XizmatKorsatishNuqtasiSerializer(serializers.ModelSerializer):
    kategoriya_nomi = serializers.CharField(source='kategoriya.nomi', read_only=True)
    def get_rasm(self, obj):
        if obj.rasm:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.rasm.url)
        return None

    class Meta:
        model = XizmatKorsatishNuqtasi
        fields = '__all__'


class MahsulotSerializer(serializers.ModelSerializer):
    nuqta_nomi = serializers.CharField(source='nuqta.nomi', read_only=True)

    class Meta:
        model = Mahsulot
        fields = '__all__'


class AviakompaniyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviakompaniya
        fields = '__all__'


class ParvozSerializer(serializers.ModelSerializer):
    aviakompaniya_nomi = serializers.CharField(source='aviakompaniya.nomi', read_only=True)
    band_orindiqlar = serializers.IntegerField(read_only=True)
    bosh_orindiqlar = serializers.IntegerField(read_only=True)

    class Meta:
        model = Parvoz
        fields = '__all__'


class YolovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yolovchi
        fields = '__all__'


class ChiptaSerializer(serializers.ModelSerializer):
    yolovchi_ismi = serializers.CharField(source='yolovchi.__str__', read_only=True)
    parvoz_raqami = serializers.CharField(source='parvoz.parvoz_raqami', read_only=True)

    class Meta:
        model = Chipta
        fields = '__all__'


class BagajSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bagaj
        fields = '__all__'


class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = '__all__'