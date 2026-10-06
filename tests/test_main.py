"""Main moduli uchun birlik (unit) testlar."""

import unittest
from src.main import greeting


class TestMain(unittest.TestCase):
    """Main modulidagi funksiyalarni testlash."""

    def test_greeting_default(self):
        """Standart parametr bilan greeting natijasini tekshirish."""
        result = greeting()
        self.assertEqual(
            result,
            "Assalomu alaykum, Foydalanuvchi! Loyiha muvaffaqiyatli ishga tushirildi."
        )

    def test_greeting_custom_name(self):
        """Maxsus parametr bilan greeting natijasini tekshirish."""
        result = greeting("Antigravity")
        self.assertEqual(
            result,
            "Assalomu alaykum, Antigravity! Loyiha muvaffaqiyatli ishga tushirildi."
        )


if __name__ == "__main__":
    unittest.main()
