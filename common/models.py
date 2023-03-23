import os, datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create class for lab member
class lab_member(models.Model):
    class Meta:
        verbose_name = "Lab Member"

    # last name of lab member
    first_name = models.CharField(max_length=70, verbose_name="First Name")

    # last name of lab member
    last_name = models.CharField(max_length=70, verbose_name="Last Name")

    # Email of lab member
    email = models.CharField(
        max_length=254, null=True, blank=True, verbose_name="Email"
    )

    # Phone number of lab member
    phone = models.CharField(max_length=13, null=True, blank=True, verbose_name="Phone")

    # Index for title of lab member
    title = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Title",
        choices=(
            ("Principal Investigator", "Principal Investigator"),
            ("Research Staff", "Research Staff"),
            ("Postdoc", "Postdoc"),
            ("Graduate Student", "Graduate Student"),
            ("Research Assistant", "Research Assistant"),
            ("Undergraduate Student", "Undergraduate Student"),
        ),
    )

    # Field for member blurb
    blurb = models.TextField(verbose_name="Blurb")

    # Define if member is alumni
    alumni = models.BooleanField(verbose_name="Lab Alumni")

    # Photo of lab member
    photo = models.ImageField(
        upload_to="portraits/", null=True, blank=True, verbose_name="Photo"
    )

    # Cv of lab member
    cv = models.FileField(upload_to="cv/", null=True, blank=True, verbose_name="CV")

    # Return the name of the model
    def __str__(self):
        return self.last_name + ", " + self.first_name


# Create class for publication
class publication(models.Model):
    class Meta:
        verbose_name = "Publication"

    # Publication Title
    title = models.CharField(
        max_length=350, unique=True, verbose_name="Publication Title"
    )

    # Publication Container
    container = models.TextField(default=datetime.date.today, verbose_name="Citation")

    # Publication Date
    date = models.DateField(verbose_name="Date Published")

    # Paper Upload
    paper = models.FileField(
        upload_to="papers/", null=True, blank=True, verbose_name="Paper"
    )

    # Return the name of the model
    def __str__(self):
        return self.title


# Create class for publication links
class publication_link(models.Model):
    class Meta:
        verbose_name = "Publication Link"

    # Create foreign key to publication class
    publication = models.ForeignKey(
        publication, on_delete=models.CASCADE, verbose_name="Publication Link"
    )

    # Publication Link Name
    name = models.CharField(max_length=350, null=True, blank=True, verbose_name="Name")

    # Publication Title
    link = models.CharField(max_length=350, unique=True, verbose_name="Link")

    # Return the name of the model
    def __str__(self):
        return self.link


# Create class for news item
class news_item(models.Model):
    class Meta:
        verbose_name = "News Item"

    # news title
    title = models.CharField(max_length=350, verbose_name="Title")

    # post Date
    pub_date = models.DateField(null=True, verbose_name="Date Published")

    # content
    content = RichTextUploadingField()

    # title
    def __str__(self):
        return self.title


# Create class for current study listing
class current_study(models.Model):
    class Meta:
        verbose_name = "Current Study"

    # Create title for Study
    title = models.CharField(max_length=350, verbose_name="Title")

    # Create study description
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    # create link to study form
    link = models.CharField(max_length=1000, null=True, verbose_name="Link")

    # flier attachement
    flier = models.FileField(
        upload_to="attachments/", null=True, blank=True, verbose_name="Flier"
    )

    def __str__(self):
        return self.title


# Create class for data listing
class data_listing(models.Model):
    class Meta:
        verbose_name = "Data Listing"

    # Create title for data listing
    title = models.CharField(max_length=350, verbose_name="Title")

    # Create description for data listing
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    # create link to data listing
    link = models.CharField(max_length=1000, null=True, verbose_name="Link")

    # image for data_listing
    image = models.ImageField(
        upload_to="data_listing_images/", null=True, blank=True, verbose_name="Image"
    )

    def __str__(self):
        return self.title


# Create class for software listing
class software_listing(models.Model):
    class Meta:
        verbose_name = "Software Listing"

    # Create title for software listing
    title = models.CharField(max_length=350, verbose_name="Title")

    # Create description for software listing
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    # create link to software listing
    link = models.CharField(max_length=1000, null=True, verbose_name="Link")

    # image for software listing
    image = models.ImageField(
        upload_to="software_listing_images/",
        null=True,
        blank=True,
        verbose_name="Image",
    )

    def __str__(self):
        return self.title
