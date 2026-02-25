from django.contrib import admin
from .models import (
    Kategoriya, XizmatKorsatishNuqtasi, Mahsulot,
    Aviakompaniya, Parvoz, Yolovchi, Chipta, Bagaj, Xodim
)


# ==========================================
# 1. KATEGORIYA
# ==========================================
@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']
    search_fields = ['nomi']


# ==========================================
# 2. XIZMAT KO'RSATISH NUQTASI
# ==========================================
@admin.register(XizmatKorsatishNuqtasi)
class XizmatKorsatishNuqtasiAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kategoriya', 'joylashuv', 'ochilish_vaqti', 'yopilish_vaqti']
    list_filter = ['kategoriya']
    search_fields = ['nomi', 'joylashuv']


# ==========================================
# 3. MAHSULOT
# ==========================================
@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'nuqta', 'narxi', 'mavjud']
    list_filter = ['mavjud', 'nuqta']
    search_fields = ['nomi']
    list_editable = ['mavjud', 'narxi']


# ==========================================
# 4. AVIAKOMPANIYA
# ==========================================
@admin.register(Aviakompaniya)
class AviakompaniyaAdmin(admin.ModelAdmin):
    list_display = ['kodi', 'nomi', 'veb_sayt']
    search_fields = ['nomi', 'kodi']


# ==========================================
# 5. PARVOZ
# ==========================================
@admin.register(Parvoz)
class ParvozAdmin(admin.ModelAdmin):
    list_display = ['parvoz_raqami', 'aviakompaniya', 'qayerdan', 'qayerga', 'uchish_vaqti', 'holat', 'terminal', 'gate']
    list_filter = ['holat', 'aviakompaniya']
    search_fields = ['parvoz_raqami', 'qayerdan', 'qayerga']
    list_editable = ['holat']


# ==========================================
# 6. YO'LOVCHI
# ==========================================
@admin.register(Yolovchi)
class YolovchiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'familiya', 'pasport_raqam', 'telefon', 'email']
    search_fields = ['ism', 'familiya', 'pasport_raqam']


# ==========================================
# 7. CHIPTA
# ==========================================
@admin.register(Chipta)
class ChiptaAdmin(admin.ModelAdmin):
    list_display = ['yolovchi', 'parvoz', 'orindiq_raqami', 'sinf', 'narxi', 'holat']
    list_filter = ['sinf', 'holat', 'parvoz']
    search_fields = ['yolovchi__ism', 'yolovchi__familiya', 'parvoz__parvoz_raqami']
    list_editable = ['holat']


# ==========================================
# 8. BAGAJ
# ==========================================
@admin.register(Bagaj)
class BagajAdmin(admin.ModelAdmin):
    list_display = ['teg_raqami', 'chipta', 'vazni_kg', 'holat']
    list_filter = ['holat']
    search_fields = ['teg_raqami']
    list_editable = ['holat']


# ==========================================
# 9. XODIM
# ==========================================
@admin.register(Xodim)
class XodimAdmin(admin.ModelAdmin):
    list_display = ['ism', 'familiya', 'lavozim', 'smena', 'telefon', 'faol']
    list_filter = ['lavozim', 'smena', 'faol']
    search_fields = ['ism', 'familiya']
    list_editable = ['faol']
