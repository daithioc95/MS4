from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=99)
    description = models.TextField(null=True, blank=True)
    Period = models.CharField(max_length=254, null=True, blank=True)
    Artist_Display_Name = models.CharField(max_length=254,
                                           null=True, blank=True)
    Artist_Display_Bio = models.CharField(max_length=254, null=True,
                                          blank=True)
    Artist_Nationality = models.CharField(max_length=254, null=True,
                                          blank=True)
    Artist_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_ULAN_URL = models.URLField(max_length=1024, null=True, blank=True)
    Artist_Wikidata_URL = models.URLField(max_length=1024,
                                          null=True, blank=True)
    Object_Date = models.CharField(max_length=254, null=True, blank=True)
    Object_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Object_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Medium = models.CharField(max_length=254, null=True, blank=True)
    Dimensions = models.CharField(max_length=1024, null=True, blank=True)
    Credit_Line = models.CharField(max_length=1024, null=True, blank=True)
    Classification = models.CharField(max_length=254, null=True, blank=True)
    Link_Resource = models.CharField(max_length=254, null=True, blank=True)
    Object_Wikidata_URL = models.URLField(max_length=1024,
                                          null=True, blank=True)
    Tags = models.CharField(max_length=254, null=True, blank=True)
    Tags_AAT_URL = models.CharField(max_length=254, null=True, blank=True)
    Tags_Wikidata_URL = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
