# Agent Ko'rsatmalari va Qoidalari (Agent Guidelines)

Ushbu repository'da ishlaydigan barcha sun'iy intellekt agentlari (AI Agent / Antigravity Agent) quyidagi qoidalarga qat'iy rioya qilishi lozim:

## 1. Toza Kod va Standartlar (Clean Code & Standards)
- **Standartlarga rioya**: Kod yozishda tanlangan dasturlash tili standartlariga (masalan, Python uchun PEP 8, qat'iy tiplashtirish/type hints) amal qiling.
- **Tushunarlilik**: O'zgaruvchilar, funksiyalar va sinf nomlari ingliz tilida, aniq va maqsadli bo'lishi lozim.
- **Arxitektura va Modullilik**: Kodni kichik, qayta ishlatiluvchi va yagona vazifaga yo'naltirilgan (Single Responsibility) funksiya va modullarga ajrating.

## 2. Rejalashtirish (Planning Before Execution)
- Har qanday kod o'zgartirish, refaktoring yoki yangi funksiya qo'shishdan oldin foydalanuvchiga **qisqacha va aniq reja** taqdim eting.
- Reja qaysi fayllar o'zgartirilishi, nima sababdan va qanday ketma-ketlikda amalga oshirilishini aks ettirishi shart.

## 3. Izohlar va Hujjatlashtirish (Docstrings & Comments)
- Har bir funksiya, klass va muhim modullar uchun tushunarli **docstring** (parametrlar, qaytariladigan qiymat va vazifasi) yozing.
- Murakkab algoritmlar va noaniq mantiqiy qismlarga kod ichida izohlar (inline comments) qoldiring.
- Mavjud izohlar va ma'lumotlarni asossiz ravishda o'chirib tashlamang.

## 4. Testlash va Ishonchlilik (Testing)
- Har bir yangi funksionallik yoki xato tuzatilgandan so'ng `tests/` papkasida testlarni yozing yoki yangilang.
- O'zgarishlar kiritilgandan so'ng testlarni ishga tushirib, tizim barqarorligini tekshiring.

## 5. Xavfsizlik (Security)
- Maxfiy ma'lumotlar (API kalitlar, parollar, tokenlar) hech qachon kod ichida ochiq (hardcoded) saqlanmasligi kerak. Doimo atrof-muhit o'zgaruvchilari (`.env`) dan foydalaning.
