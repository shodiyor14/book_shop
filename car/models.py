from django.db import models


# class CarModels():
#     title = models.CharField(max_length=1000,)
#     price = models.PositiveIntegerField()
#     descritption = models.TextField()
#     wheel_size = models.CharField(max_length=55)
#     max_speed = models.PositiveIntegerField()
#     image = models.ImageField(upload_to='car')
#     created_at = models.DateTimeField(auto_now_add=True)


class PhonesCategoryModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class PhonesColorModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class PhoneBrandModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class PhoneTagModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PhoneModel(models.Model):
    title = models.CharField(max_length=100,)
    price = models.PositiveIntegerField()
    os = models.CharField(max_length=15,)
    os_version = models.CharField(max_length=15,)
    Type_of_sim_card = models.CharField(max_length=15,)
    Built_in_memory = models.CharField(max_length=30,)
    ram = models.CharField(max_length=15,)
    Product_weight_with_packaging_kg = models.CharField(max_length=15,)
    Product_height_cm = models.CharField(max_length=15,)
    Country_of_manufacture = models.CharField(max_length=10,)
    Degree_of_dust_and_moisture_protection = models.CharField(max_length=15,)
    Depth_cm = models.CharField(max_length=15,)
    created_at = models.DateTimeField(auto_now_add=True)
    Display_Screen_Type = models.CharField(max_length=10,)
    Screen_diagonal = models.CharField(max_length=15,)
    Screen_resolution = models.CharField(max_length=15,)
    Processor = models.CharField(max_length=15,)
    Number_of_processor_cores = models.CharField(max_length=19,)
    Processor_clock_speed = models.CharField(max_length=15,)
    Number_of_SIM_cards = models.CharField(max_length=15,)
    Communication_standard = models.CharField(max_length=15,)
    category = models.ForeignKey(PhonesCategoryModel, on_delete=models.PROTECT, related_name='phone')
    color = models.ManyToManyField(PhonesColorModel, related_name='phone')
    brand = models.ForeignKey(PhoneBrandModel, on_delete=models.PROTECT, related_name='phone')
    tag = models.ManyToManyField(PhoneTagModel, related_name='phone')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
