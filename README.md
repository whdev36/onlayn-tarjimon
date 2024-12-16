# 🌐 Onlayn Tarjimon

Django asosida yaratilgan onlayn tarjimon ilovasi. Bu loyiha foydalanuvchilarga so‘zlarni ingliz tilidan o‘zbek tiliga tarjima qilish imkonini beradi.

![Django](https://img.shields.io/badge/Django-4.2-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![SQLite3](https://img.shields.io/badge/SQLite3-Database-lightgrey) ![Semantic-UI](https://img.shields.io/badge/Semantic--UI-CSS-orange)

## 🛠 Texnologiyalar

Loyihada quyidagi texnologiyalar va vositalardan foydalanilgan:

- 🐍 **Python**: Backend uchun asosiy dasturlash tili.
- 🌐 **Django**: Web-ilovalarni yaratish uchun ishlatilgan framework.
- 🎨 **Semantic-UI**: Foydalanuvchi interfeysi uchun UI kutubxonasi.
- 🗄 **SQLite3**: Ma‘lumotlar bazasi sifatida.

## ✨ Funksionallik

- 📖 So‘zlarni ingliz tilidan o‘zbek tiliga tarjima qilish.
- 🔍 Foydalanuvchi kiritgan so‘zlarni ma‘lumotlar bazasidan qidirish va natijalarni ko‘rsatish.
- 🖥 Foydalanuvchilarga qulay va minimalistik interfeys.

## ⚙️ O‘rnatish

Ushbu loyihani lokal mashinangizda ishga tushirish uchun quyidagi bosqichlarni bajaring:

### 1. 📥 Repositoriyani klonlash

```bash
git clone https://github.com/whdev36/onlayn-tarjimon.git
cd onlayn-tarjimon
```

### 2. 💻 Virtual muhit yaratish va faollashtirish

```bash
python -m venv venv
# Windows uchun
venv\Scripts\activate
# macOS/Linux uchun
source venv/bin/activate
```

### 3. 📦 Zaruriy kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 4. 🗄 Ma‘lumotlar bazasini sozlash

```bash
python manage.py migrate
```

### 5. 🚀 Loyihani ishga tushirish

```bash
python manage.py runserver
```

Brauzerda quyidagi manzilni oching:

```
http://127.0.0.1:8000/
```

## 📂 Loyiha tuzilmasi

- `onlayn_tarjimon/` – Django ilovasi uchun asosiy papka.
  - `models.py` – Ma‘lumotlar bazasi uchun model.
  - `views.py` – HTTP so‘rovlarini boshqarish uchun funksiya va mantiq.
  - `templates/` – HTML shablonlar.
- `db.sqlite3` – SQLite ma‘lumotlar bazasi fayli.
- `static/` – Statik fayllar (CSS, JS, rasmlar).

## 📝 Eslatma

Ushbu loyiha quyidagi [YouTube video darsligi](https://youtube.com/playlist?list=PLOvS2OkP87tQFMxb4ZFqs8WI0lW6wIhKf&si=9muyO2O8mfE4Gxg9) asosida tayyorlangan.

## 👨‍💻 Muallif

**whdev36**

GitHub: [whdev36](https://github.com/whdev36)

## 📜 License

MIT License

Bu loyiha MIT litsenziyasi asosida tarqatiladi. Qo‘shimcha ma‘lumot uchun quyidagi faylni ko‘ring: [LICENSE](./LICENSE).
