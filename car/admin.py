from django.contrib import admin
from car.models import PhonesCategoryModel, PhonesColorModel, PhoneBrandModel, PhoneTagModel, PhoneModel

admin.site.register(PhonesCategoryModel)
admin.site.register(PhonesColorModel)
admin.site.register(PhoneBrandModel)
admin.site.register(PhoneTagModel)
admin.site.register(PhoneModel)


