from django.db import models


class Product(models.Model):
    Is_Highlight = models.BooleanField(default=False)
    Department = models.CharField(max_length=254, null=True, blank=True)
    AccessionYear = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    Period = models.CharField(max_length=254, null=True, blank=True)
    Culture = models.CharField(max_length=254, null=True, blank=True)
    Constituent_ID = models.CharField(max_length=254, null=True, blank=True)
    Artist_Role = models.CharField(max_length=254, null=True, blank=True)
    Artist_Prefix = models.CharField(max_length=254, null=True, blank=True)
    Artist_Display_Name = models.CharField(max_length=254, null=True, blank=True)
    Artist_Display_Bio = models.CharField(max_length=254, null=True, blank=True)
    Artist_Suffix = models.CharField(max_length=254, null=True, blank=True)
    Tags = models.CharField(max_length=254, null=True, blank=True)
    Artist_Alpha_Sort = models.CharField(max_length=254, null=True, blank=True)
    Artist_Nationality = models.CharField(max_length=254, null=True, blank=True)
    Artist_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_Gender = models.CharField(max_length=254, null=True, blank=True)
    Artist_ULAN_URL = models.URLField(max_length=1024, null=True, blank=True)
    Artist_Wikidata_URL = models.URLField(max_length=1024, null=True, blank=True)
    Object_Date = models.CharField(max_length=254, null=True, blank=True)
    Object_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Object_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Medium = models.CharField(max_length=254, null=True, blank=True)
    Dimensions = models.CharField(max_length=254, null=True, blank=True)
    Credit_Line = models.CharField(max_length=254, null=True, blank=True)
    Classification = models.CharField(max_length=254, null=True, blank=True)
    Link_Resource = models.URLField(max_length=1024, null=True, blank=True)
    Repository = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name

# Migrate above