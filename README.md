# Loyiha Nomi (Project Name)

Loyiha tavsifi (Bu yerga loyihaning asosiy maqsadi va vazifalari haqida qisqacha ma'lumot yozing).

---

## 📁 Loyiha Tuzilishi (Project Layout)

```text
Antigiravity_IDE_agent/
├── src/                  # Asosiy manba kodlari (Source code)
│   ├── __init__.py
│   └── main.py           # Dasturning asosiy kirish nuqtasi (Entrypoint)
├── tests/                # Avtomatlashtirilgan testlar (Unit tests)
│   ├── __init__.py
│   └── test_main.py      # Boshlang'ich testlar
├── .env.example          # Muhit o'zgaruvchilari namunasi
├── .gitignore            # Git e'tiborsiz qoldiradigan fayllar
├── agent.md              # AI Agent uchun qoidalar va ko'rsatmalar
├── README.md             # Loyiha haqida umumiy hujjat
└── requirements.txt      # Loyiha kutubxonalari ro'yxati
```

---

## 🚀 Ishga Tushirish (Quick Start)

### 1. Repository'ni klonlash yoki ochish
```bash
git clone <repository_url>
cd Antigiravity_IDE_agent
```

### 2. Virtual muhitni (venv) yaratish va faollashtirish
```bash
# Virtual muhit yaratish
python3 -m venv venv

# Linux / macOS:
source venv/bin/activate

# Windows (Command Prompt):
# venv\Scripts\activate.bat

# Windows (PowerShell):
# venv\Scripts\Activate.ps1
```

### 3. Kerakli kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Dasturni ishga tushirish
```bash
python -m src.main
```

### 5. Testlarni tekshirish
```bash
# unittest yordamida:
python -m unittest discover tests

# yoki pytest orqali:
pytest
```

---

## ⚙️ Sozlamalar (.env)
Loyihada konfiguratsiya yoki maxfiy kalitlar ishlatilsa, `.env.example` dan nusxa olib `.env` yarating:
```bash
cp .env.example .env
```

---

## 🤝 Hissa Qo'shish (Contributing)
1. Fork qiling yoki yangi feature branch oching (`git checkout -b feature/yangilik`).
2. O'zgarishlarni kiriting va `tests/` orqali testlarni tekshiring.
3. Commit va Push qiling, so'ngra Pull Request yuboring.
4. AI Agent bilan ishlashda [agent.md](agent.md) qoidalariga rioya qiling.

---

## 📄 Litsenziya
Ushbu loyiha MIT litsenziyasi ostida tarqatiladi.
