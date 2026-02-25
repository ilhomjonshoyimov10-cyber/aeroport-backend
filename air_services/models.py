from django.db import models


# ==========================================
# 1. KATEGORIYA
# ==========================================
class Kategoriya(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


# ==========================================
# 2. XIZMAT KO'RSATISH NUQTASI
# ==========================================
class XizmatKorsatishNuqtasi(models.Model):
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200)
    joylashuv = models.CharField(max_length=100)
    ochilish_vaqti = models.TimeField()
    yopilish_vaqti = models.TimeField()
    rasm = models.ImageField(upload_to='xizmatlar/', blank=True, null=True)
    tavsif = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Xizmat nuqtasi"
        verbose_name_plural = "Xizmat ko'rsatish nuqtalari"


# ==========================================
# 3. MAHSULOT
# ==========================================
class Mahsulot(models.Model):
    nuqta = models.ForeignKey(
        XizmatKorsatishNuqtasi,
        on_delete=models.CASCADE,
        related_name='mahsulotlar'
    )
    nomi = models.CharField(max_length=200)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    rasmi = models.ImageField(upload_to='mahsulotlar/', blank=True, null=True)
    mavjud = models.BooleanField(default=True)  # Sotuvda bormi?
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nomi} - {self.nuqta.nomi}"

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


# ==========================================
# 4. AVIAKOMPANIYA (YANGI)
# ==========================================
class Aviakompaniya(models.Model):
    nomi = models.CharField(max_length=200)           # "Uzbekistan Airways"
    kodi = models.CharField(max_length=10, unique=True)  # "HY", "SU"
    logotipi = models.ImageField(upload_to='aviakompaniyalar/', blank=True, null=True)
    veb_sayt = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.kodi} - {self.nomi}"

    class Meta:
        verbose_name = "Aviakompaniya"
        verbose_name_plural = "Aviakompaniyalar"


# ==========================================
# 5. PARVOZ (KENGAYTIRILGAN)
# ==========================================
class Parvoz(models.Model):

    class Holat(models.TextChoices):
        REJALASHTIRILGAN = 'rejalashtirilgan', 'Rejalashtirilgan'
        KECHIKKAN = 'kechikkan', 'Kechikkan'
        BEKOR_QILINGAN = 'bekor_qilingan', 'Bekor qilingan'
        UCHDI = 'uchdi', 'Uchdi'
        QONDI = 'qondi', 'Qo\'ndi'

    aviakompaniya = models.ForeignKey(
        Aviakompaniya,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='parvozlar'
    )
    parvoz_raqami = models.CharField(max_length=20, unique=True)  # "HY007"
    qayerdan = models.CharField(max_length=100)
    qayerga = models.CharField(max_length=100)
    uchish_vaqti = models.DateTimeField()
    qonish_vaqti = models.DateTimeField(null=True, blank=True)
    terminal = models.CharField(max_length=10, blank=True, null=True)   # "Terminal 2"
    gate = models.CharField(max_length=10, blank=True, null=True)       # "Gate 14"
    holat = models.CharField(
        max_length=20,
        choices=Holat.choices,
        default=Holat.REJALASHTIRILGAN
    )
    umumiy_orindiqlar = models.PositiveIntegerField(default=180)
    bosh_narx = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # USD
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def band_orindiqlar(self):
        return self.chiptalar.count()

    def bosh_orindiqlar(self):
        return self.umumiy_orindiqlar - self.band_orindiqlar()

    def __str__(self):
        return f"{self.parvoz_raqami}: {self.qayerdan} → {self.qayerga}"

    class Meta:
        verbose_name = "Parvoz"
        verbose_name_plural = "Parvozlar"
        ordering = ['uchish_vaqti']


# ==========================================
# 6. YO'LOVCHI (KENGAYTIRILGAN)
# ==========================================
class Yolovchi(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    pasport_raqam = models.CharField(max_length=20, unique=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tug_ilgan_sana = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    class Meta:
        verbose_name = "Yo'lovchi"
        verbose_name_plural = "Yo'lovchilar"


# ==========================================
# 7. CHIPTA (YANGI)
# ==========================================
class Chipta(models.Model):

    class Sinf(models.TextChoices):
        ECONOMY = 'economy', 'Economy'
        BUSINESS = 'business', 'Business'
        FIRST = 'first', 'First Class'

    class Holat(models.TextChoices):
        BAND = 'band', 'Band'
        BEKOR = 'bekor', 'Bekor qilingan'
        ISHLATILGAN = 'ishlatilgan', 'Ishlatilgan'

    yolovchi = models.ForeignKey(
        Yolovchi,
        on_delete=models.CASCADE,
        related_name='chiptalar'
    )
    parvoz = models.ForeignKey(
        Parvoz,
        on_delete=models.CASCADE,
        related_name='chiptalar'
    )
    orindiq_raqami = models.CharField(max_length=10)   # "14A"
    sinf = models.CharField(max_length=10, choices=Sinf.choices, default=Sinf.ECONOMY)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    holat = models.CharField(max_length=15, choices=Holat.choices, default=Holat.BAND)
    bron_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.yolovchi} | {self.parvoz.parvoz_raqami} | {self.orindiq_raqami}"

    class Meta:
        verbose_name = "Chipta"
        verbose_name_plural = "Chiptalar"
        unique_together = ['parvoz', 'orindiq_raqami']  # Bir o'rindiqqa 2 chipta bo'lmasin


# ==========================================
# 8. BAGAJ (YANGI)
# ==========================================
class Bagaj(models.Model):

    class Holat(models.TextChoices):
        QABUL_QILINDI = 'qabul', 'Qabul qilindi'
        YUKLANDA = 'yuklandi', 'Yuklanda'
        YETKAZILDI = 'yetkazildi', 'Yetkazildi'
        YO_QOLDI = 'yoqoldi', "Yo'qoldi"

    chipta = models.ForeignKey(Chipta, on_delete=models.CASCADE, related_name='bagajlar')
    vazni_kg = models.DecimalField(max_digits=5, decimal_places=2)  # kg
    holat = models.CharField(max_length=15, choices=Holat.choices, default=Holat.QABUL_QILINDI)
    teg_raqami = models.CharField(max_length=20, unique=True)       # "BG-00123"
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Bagaj {self.teg_raqami} - {self.chipta.yolovchi}"

    class Meta:
        verbose_name = "Bagaj"
        verbose_name_plural = "Bagajlar"


# ==========================================
# 9. XODIM (YANGI)
# ==========================================
class Xodim(models.Model):

    class Lavozim(models.TextChoices):
        OPERATOR = 'operator', 'Operator'
        XAVFSIZLIK = 'xavfsizlik', 'Xavfsizlik xodimi'
        TOZALOVCHI = 'tozalovchi', 'Tozalovchi'
        BOSHQARUVCHI = 'boshqaruvchi', 'Boshqaruvchi'
        PILOT = 'pilot', 'Pilot'
        STYUARDESSA = 'styuardessa', 'Styuardessa'

    class Smena(models.TextChoices):
        KUNDUZGI = 'kunduz', 'Kunduzgi (08:00-20:00)'
        TUNGI = 'tun', 'Tungi (20:00-08:00)'

    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=20, choices=Lavozim.choices)
    smena = models.CharField(max_length=10, choices=Smena.choices)
    telefon = models.CharField(max_length=20)
    ishlash_nuqtasi = models.ForeignKey(
        XizmatKorsatishNuqtasi,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='xodimlar'
    )
    yollanma_sanasi = models.DateField()
    faol = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ism} {self.familiya} ({self.get_lavozim_display()})"

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"