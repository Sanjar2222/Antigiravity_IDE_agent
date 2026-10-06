"""Loyiha uchun asosiy kirish nuqtasi (Entrypoint)."""


def greeting(name: str = "Foydalanuvchi") -> str:
    """Foydalanuvchiga salomlashish xabarini qaytaradi.

    Args:
        name: Foydalanuvchi yoki loyiha nomi.

    Returns:
        Salomlashish matni.
    """
    return f"Assalomu alaykum, {name}! Loyiha muvaffaqiyatli ishga tushirildi."


def main() -> None:
    """Asosiy dastur funksiyasi."""
    message = greeting()
    print(message)


if __name__ == "__main__":
    main()
