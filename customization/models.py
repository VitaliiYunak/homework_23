from django.contrib.auth.models import User, AbstractUser
from django.db import models


class UpperTextModel(models.Model):
    upper_text = models.CharField(max_length=100, verbose_name="Текст")

    def __str__(self):
        return self.upper_text

    def save(self, *args, **kwargs):
        # Автоматичне перетворення тексту у верхній регістр
        if self.upper_text:
            self.upper_text = self.upper_text.upper()
        super().save(*args, **kwargs)

    def text_statistics(self):
        # Підрахунок кількості символів у тексті
        if not self.upper_text:
            return {"символів": 0, "слів": 0}
        return {
            "length": len(self.upper_text),
            "words": len(self.upper_text.split()),
        }
    class Meta:
        ordering = ["-upper_text"]
        indexes = [
            models.Index(fields=["-upper_text"]),
        ]


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
