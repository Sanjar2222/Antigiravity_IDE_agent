---
name: python-unit-tester
description: Pytest yordamida Python kodi uchun unit-testlar yozadi hamda ularni terminalda ishga tushirib test qiladi. Test yozish, mavjud testlarni yurgizish yoki xatoliklarni aniqlashda ishlatiladi.
---

# Python Unit Testlarini Yozish va Test Qilish Ko'nikmasi

Python kodi uchun testlar yozish va ularni sinovdan o'tkazishda quyidagi qadamlarga amal qiling:

## 1. Test Yozish Qoidalari
1. **Framework**: Testlash tizimi sifatida doimo `pytest` dan foydalaning.
2. **Nomlash Konvensiyasi**: Test fayllari `test_` bilan boshlanishi va test funksiyalari `test_<funksiya_nomi>` formatida bo'lishi shart.
3. **Tasdiqlashlar (Assertions)**: Test natijalarini tekshirish uchun standart Python `assert` operatorlaridan foydalaning.
4. **Chekka Holatlar (Edge Cases)**: Chegaraviy shartlar, noto'g'ri kiritilgan ma'lumotlar va kutilgan xatoliklar (`pytest.raises` yordamida) uchun test holatlarini qo'shing.

## 2. Test Qilish (Ishga Tushirish) Qoidalari
1. **Buyruqni Bajarish**: Yangi test yozilgach yoki kod o'zgargach, testlarni terminal orqali darhol ishga tushiring:
   ```bash
   pytest
   # yoki aniq test faylini batafsil ko'rish uchun:
   pytest tests/test_<nom>.py -v
   ```
2. **Natijani Tahlil Qilish**: Barcha testlar muvaffaqiyatli (PASSED) o'tganiga ishonch hosil qiling.
3. **Xatoni To'g'rilash**: Agar biror test yiqilsa (FAILED), xatolik sababini aniqlab, kod yoki testni tuzating va qayta tekshiring.
