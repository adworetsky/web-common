from django.contrib import admin
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from .models import *

# admin for lab member model
class labmemberadmin(admin.ModelAdmin):
    ordering = ("last_name",)
    fieldsets = (
        (
            "Lab Member Data",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "title",
                    "blurb",
                    "alumni",
                    "photo",
                    "cv",
                )
            },
        ),
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "title",
    )
    save_as = True


# inline model for publication link
class publicationlinkinline(admin.StackedInline):
    verbose_name = "Publication Link"
    model = publication_link


# admin for publication model
class publicationadmin(admin.ModelAdmin):
    ordering = ("-date",)
    fieldsets = (
        (
            "Publications",
            {
                "fields": (
                    "title",
                    "container",
                    "date",
                    "paper",
                )
            },
        ),
    )
    inlines = (publicationlinkinline,)
    search_fields = (
        "title",
        "container",
        "date",
    )
    save_as = True


# news item
class newsitemadmin(admin.ModelAdmin):
    ordering = ("title",)
    fieldsets = (
        (
            "News Post",
            {
                "fields": (
                    "title",
                    "pub_date",
                    "content",
                )
            },
        ),
    )
    search_fields = ("title",)
    save_as = True


# current study listing
class currentstudyadmin(admin.ModelAdmin):
    ordering = ("title",)
    fieldsets = (
        (
            "Current Study",
            {
                "fields": (
                    "title",
                    "description",
                    "link",
                    "flier",
                )
            },
        ),
    )
    search_fields = ("title",)
    save_as = True


# software listing
class datalistingadmin(admin.ModelAdmin):
    ordering = ("title",)
    fieldsets = (
        (
            "Data Listing",
            {
                "fields": (
                    "title",
                    "description",
                    "link",
                    "image",
                )
            },
        ),
    )
    search_fields = ("title",)
    save_as = True


# software listing
class softwarelistingadmin(admin.ModelAdmin):
    ordering = ("title",)
    fieldsets = (
        (
            "Software Listing",
            {
                "fields": (
                    "title",
                    "description",
                    "link",
                    "image",
                )
            },
        ),
    )
    search_fields = ("title",)
    save_as = True


# dlabsite models
admin.site.register(lab_member, labmemberadmin)
admin.site.register(publication, publicationadmin)
admin.site.register(news_item, newsitemadmin)
admin.site.register(current_study, currentstudyadmin)
admin.site.register(data_listing, datalistingadmin)
admin.site.register(software_listing, softwarelistingadmin)

# customize admin site names
admin.site.site_title = "Admin"
admin.site.site_header = "Admin Panel"
admin.site.index_title = "Home"
