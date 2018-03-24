from django.contrib import admin
from .models import *

class BigCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Модель товара

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'property_1','property_2', 'property_3','property_4','property_5','property_6']
    list_filter = ['available', 'created', 'updated',]
    list_editable = ['price', 'stock', 'available','property_1','property_2', 'property_3','property_4','property_5','property_6']
    prepopulated_fields = {'slug': ('name', )}

class ComplectingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'property_1','property_2', 'property_3','property_4','property_5']
    list_filter = ['available', 'created', 'updated',]
    list_editable = ['price', 'stock', 'available','property_1','property_2','property_3','property_4','property_5']
    prepopulated_fields = {'slug': ('name', )}
    
class PerfAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'property_1','property_2', 'property_3','property_4']
    list_filter = ['available', 'created', 'updated',]
    list_editable = ['price', 'stock', 'available','property_1','property_2','property_3','property_4']
    prepopulated_fields = {'slug': ('name', )}

class AcsesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'property_1','property_2', 'property_3','property_4']
    list_filter = ['available', 'created', 'updated',]
    list_editable = ['price', 'stock', 'available','property_1','property_2','property_3','property_4']
    prepopulated_fields = {'slug': ('name', )}
    
class ProductStatAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')
    search_fields = ('__str__', )

class ShakeProductAdmin(admin.ModelAdmin):
    list_display = ['maincategory','name']
    list_editable = ['name']

class UtilityAdmin(admin.ModelAdmin):
    list_display = ['name','value']

class PCAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'property_1', 'property_2',
                    'property_3', 'property_4']
    list_filter = ['available', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('name',)}

class HubNotebookAdmin(admin.ModelAdmin):
    list_display = ['name']

class HubPCAdmin(admin.ModelAdmin):
    list_display = ['name']

class HubComplectingAdmin(admin.ModelAdmin):
    list_display = ['name']

class HubAcsesAdmin(admin.ModelAdmin):
    list_display = ['name']

class HubPerfAdmin(admin.ModelAdmin):
    list_display = ['name']

class PhotoPackAdmin(admin.ModelAdmin):
    list_display = ['name']

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['review']

admin.site.register(ShakeProduct, ShakeProductAdmin)
admin.site.register(Category_notebook, CategoryAdmin)
admin.site.register(Notebook, ProductAdmin)
admin.site.register(BigCategory, BigCategoryAdmin)
admin.site.register(Complecting, ComplectingAdmin)
admin.site.register(Perf, PerfAdmin)
admin.site.register(Acses, AcsesAdmin)
admin.site.register(ProductStat, ProductStatAdmin)
admin.site.register(Utility,UtilityAdmin)
admin.site.register(PC,PCAdmin)
admin.site.register(HubNotebook, HubNotebookAdmin)
admin.site.register(HubPC, HubPCAdmin)
admin.site.register(HubAcses, HubAcsesAdmin)
admin.site.register(HubPerf, HubPerfAdmin)
admin.site.register(HubComplecting, HubComplectingAdmin)
admin.site.register(PhotoPack,PhotoPackAdmin)
admin.site.register(Reviews,ReviewsAdmin)