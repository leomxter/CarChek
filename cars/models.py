from django.db import models

class Car(models.Model):
    number = models.CharField(
        max_length=10,
        verbose_name="Номер"

    )
    make = models.CharField(
        max_length=50,
        verbose_name="Бренд"

        )
    model = models.CharField(
        max_length=50,
        verbose_name="Модель"

        )
    year = models.CharField(
        max_length=50,
        verbose_name="Год"
    )

    def __str__(self):
        return self.number