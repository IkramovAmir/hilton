# Hilton Hotel Loyihasi

## Loyiha Sharhi
Hilton Hotel loyihasi mehmonxona operatsiyalarini boshqarish uchun mo‘ljallangan veb-tizim bo‘lib, foydalanuvchilarni boshqarish, xonalarni bron qilish va boshqa muhim funksiyalarni o‘z ichiga oladi.

## Xususiyatlar
- **Foydalanuvchilarni boshqarish:** Mijozlar ro‘yxatdan o‘tishi, tizimga kirishi va profilini boshqarishi mumkin.
- **Xonalarni boshqarish:** Mehmonxona mavjud xonalarni, ularning narxlarini va bron qilish jarayonini boshqarishi mumkin.
- **Bron qilish tizimi:** Mijozlar uchun xonalarni osongina bron qilish va bron qilish tarixini ko‘rish imkoniyati mavjud.

## Ishlatilgan texnologiyalar
- **Backend:** Python, MySQL (`mysql.connector` orqali)
- **Frontend:** HTML, CSS
- **Framework/Libraries:** Flask

## Ma'lumotlar bazasi tuzilishi
Loyiha quyidagi jadvallardan iborat:
1. **Foydalanuvchilar:** Mijozlar haqidagi ma’lumotlarni saqlaydi.
2. **Xonalar:** Mavjud xonalar haqida ma’lumot saqlaydi.
3. **Bronlar:** Xonalarni bron qilish jarayonlarini boshqaradi.

## O‘rnatish va ishga tushirish
### Talablar
- Kompyuteringizda Python o‘rnatilgan bo‘lishi kerak
- MySQL ma’lumotlar bazasi serveri o‘rnatilgan bo‘lishi kerak
- Kerakli Python kutubxonalari: `mysql-connector-python`

### O‘rnatish va ishga tushirish bosqichlari
1. Repozitoriydan nusxa olish:
   ```sh
   git clone https://github.com/your-repo/hilton.git
   cd hilton-hotel
   ```
2. Kerakli kutubxonalarni o‘rnatish:
   ```sh
   pip install mysql-connector-python flask
   ```
3. Ma’lumotlar bazasini sozlash:
   - `db.py` faylidagi `DB` klassini MySQL ma’lumotlaringiz bilan yangilang.
   - Ma’lumotlar bazasi yaratish skriptini ishga tushiring:
   ```sh
   python init_db.py
   ```
4. Veb-serverni ishga tushirish:
   ```sh
   python app.py
   ```
5. Brauzeringizda `http://localhost:5000` manziliga o‘ting.

## Hissa qo‘shish qoidalari
1. Repozitoriyani fork qiling.
2. Yangi branch yarating (`feature/sizning-xususiyatingiz`).
3. O‘zgartirishlarni commit qiling.
4. Branchingizni push qiling va pull request yuboring.

## Litsenziya
Bu loyiha MIT litsenziyasi asosida tarqatiladi.

