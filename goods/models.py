from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.category_name}'

class Company(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Goods(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}-{self.price}-{self.category}'