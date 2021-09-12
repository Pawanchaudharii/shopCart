from django.contrib import admin
from AdminApp.models import Electronics,Fashion,ElectronicsProduct,FashionProduct

# Register your models here.
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ("id", "ele_name")

class FashionAdmin(admin.ModelAdmin):
    list_display = ("id","fashion_name")


class ElectronicsProductAdmin(admin.ModelAdmin):
    list_display = ("id","electronicsproductname","electronicsproduct_image","price","description","electronics")

class FashionProductAdmin(admin.ModelAdmin):
    list_display = ("id","fashionproductname","fashionproduct_image","price","description","fashion")

admin.site.register(Electronics, ElectronicsAdmin)
admin.site.register(Fashion, FashionAdmin)
admin.site.register(ElectronicsProduct, ElectronicsProductAdmin)
admin.site.register(FashionProduct, FashionProductAdmin)