from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'Period',
        'price',
        'Artist_Display_Name',
        'Dimensions',
        'Classification',
        'Medium',
    )

# pk,model,name,Period,price,Artist_Display_Name,Artist_Display_Bio,Artist_Alpha_Sort,Artist_Nationality,Artist_Begin_Date,Artist_End_Date,Artist_ULAN_URL,Artist_Wikidata_URL,Object_Date,Object_Begin_Date,Object_End_Date,Medium,Dimensions,Credit_Line,Classification,Link_Resource,Object_Wikidata_URL,Tags,Tags_AAT_URL,Tags_Wikidata_URL
admin.site.register(Product, ProductAdmin)