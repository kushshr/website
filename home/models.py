from django.db import models

from wagtail.core.models import Page


from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from home.core.utils import *

class HomePage(Page):

    templates = 'home/home_page.html'
    # Main Banner
    main_banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_divider = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title_nl = models.CharField(max_length=140, blank=True)
    main_banner_body_en = RichTextField(blank=True)
    main_banner_body_nl = RichTextField(blank=True)
    main_banner_subtitle_en = models.CharField(max_length=255, blank=True)
    main_banner_subtitle_nl = models.CharField(max_length=255, blank=True)

    # What We Do
    what_we_do_section_header_en = models.CharField(max_length=140, blank=True)
    what_we_do_section_header_nl = models.CharField(max_length=140, blank=True)

    # Translated fields
    translated_title = TranslatedField(
        'title',
        'title_nl',
    )
    main_banner_body = TranslatedField(
        'main_banner_body_en',
        'main_banner_body_nl',
    )
    main_banner_subtitle = TranslatedField(
        'main_banner_subtitle_en',
        'main_banner_subtitle_nl',
    )
    what_we_do_section_header = TranslatedField(
        'what_we_do_section_header_en',
        'what_we_do_section_header_nl',
    )

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('main_banner_body_en', classname="full"),
        FieldPanel('main_banner_subtitle_en', classname="full"),
        # InlinePanel('related_links', label="Related links"),
    ]

class Contacts(models.Model):
    name = models.TextField(default='',null=False)
    email = models.EmailField()
    message = models.TextField(default='')

    def embed(self):
        return {'name':self.name,
                'email':self.email,
                'message':self.message}

