from django.db import models


class LaptopCategoryModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class LaptopColorModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class LaptopBrandModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class LaptopTagModel(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class LaptopModel(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    Built_in_memory = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    Country_of_manufacture = models.CharField(max_length=100,)
    Display_screen_type = models.CharField(max_length=19)
    Screen_dioganal = models.CharField(max_length=19)
    Screen_Resolution = models.CharField(max_length=30)
    processor = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(LaptopCategoryModel, on_delete=models.PROTECT, related_name='laptop')
    color = models.ManyToManyField(LaptopColorModel, related_name='laptop')
    brand = models.ForeignKey(LaptopBrandModel, on_delete=models.PROTECT, related_name='laptop')
    tag = models.ManyToManyField(LaptopTagModel, related_name='laptop')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'laptop'
        verbose_name_plural = 'laptops'


class TvCategoryModel(models.Model):
    title = models.CharField(max_length=50, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TvColorModel(models.Model):
    title = models.CharField(max_length=50, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class TvBrandModel(models.Model):
    title = models.CharField(max_length=50, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class TvTagModel(models.Model):
    title = models.CharField(max_length=50, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class TvModel(models.Model):
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='TV', null=True)
    price = models.CharField(max_length=50, null=True)
    graphics_card = models.CharField(max_length=50, null=True)
    os_version = models.CharField(max_length=50, null=True)
    HD_Resolution = models.CharField(max_length=50, null=True)
    RAM = models.CharField(max_length=50, null=True)
    Overall_dimensions_without_packaging = models.CharField(max_length=50, null=True)
    Country_of_manufacture = models.CharField(max_length=100, null=True)
    Flash_memory = models.CharField(max_length=50, null=True)
    Screen_resolution = models.CharField(max_length=50, null=True)
    processor = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(TvCategoryModel, on_delete=models.PROTECT, related_name='tv')
    Number_of_colors = models.CharField(max_length=50, null=True)
    color = models.ManyToManyField(TvColorModel, related_name='tv')
    brand = models.ForeignKey(TvBrandModel, on_delete=models.PROTECT, related_name='tv')
    tag = models.ManyToManyField(TvTagModel, related_name='tv')
    Screen_format = models.CharField(max_length=50, null=True)
    Viewing_angle = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tv'
        verbose_name_plural = 'tvs'
