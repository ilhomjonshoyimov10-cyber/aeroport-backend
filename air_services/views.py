from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import (
    Kategoriya, XizmatKorsatishNuqtasi, Mahsulot,
    Aviakompaniya, Parvoz, Yolovchi, Chipta, Bagaj, Xodim
)
from .serializers import (
    KategoriyaSerializer, XizmatKorsatishNuqtasiSerializer, MahsulotSerializer,
    AviakompaniyaSerializer, ParvozSerializer, YolovchiSerializer,
    ChiptaSerializer, BagajSerializer, XodimSerializer
)


class KategoriyaViewSet(viewsets.ModelViewSet):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomi']


class XizmatKorsatishNuqtasiViewSet(viewsets.ModelViewSet):
    queryset = XizmatKorsatishNuqtasi.objects.all()
    serializer_class = XizmatKorsatishNuqtasiSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nomi', 'joylashuv']
    filterset_fields = ['kategoriya']

    def get_serializer_context(self):
        return {'request': self.request}


class MahsulotViewSet(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nomi']
    filterset_fields = ['mavjud', 'nuqta']


class AviakompaniyaViewSet(viewsets.ModelViewSet):
    queryset = Aviakompaniya.objects.all()
    serializer_class = AviakompaniyaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomi', 'kodi']


class ParvozViewSet(viewsets.ModelViewSet):
    queryset = Parvoz.objects.all()
    serializer_class = ParvozSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['parvoz_raqami', 'qayerdan', 'qayerga']
    filterset_fields = ['holat', 'aviakompaniya']


class YolovchiViewSet(viewsets.ModelViewSet):
    queryset = Yolovchi.objects.all()
    serializer_class = YolovchiSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['ism', 'familiya', 'pasport_raqam']


class ChiptaViewSet(viewsets.ModelViewSet):
    queryset = Chipta.objects.all()
    serializer_class = ChiptaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sinf', 'holat', 'parvoz']


class BagajViewSet(viewsets.ModelViewSet):
    queryset = Bagaj.objects.all()
    serializer_class = BagajSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['holat']


class XodimViewSet(viewsets.ModelViewSet):
    queryset = Xodim.objects.all()
    serializer_class = XodimSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['ism', 'familiya']
    filterset_fields = ['lavozim', 'smena', 'faol']


# ✅ Register
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username va parol kiritilishi shart!'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Bu username allaqachon mavjud!'}, status=400)

    User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'Muvaffaqiyatli ro\'yxatdan o\'tdingiz!'}, status=201)