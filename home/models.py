from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
import datetime

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
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
    tomp_api_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tomp_cds_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    title_nl = models.CharField(max_length=140, blank=True)
    travel_operators_subtitle_en = models.CharField(max_length=255, blank=True)
    travel_operators_subtitle_nl = models.CharField(max_length=255, blank=True)
    maas_subtitle_en = models.CharField(max_length=255, blank=True)
    maas_subtitle_nl = models.CharField(max_length=255, blank=True)
    cities_subtitle_en = models.CharField(max_length=140, blank=True)
    cities_subtitle_nl = models.CharField(max_length=140, blank=True)
    tompapi_subtitle_en = models.CharField(max_length=140, blank=True)
    tompapi_subtitle_nl = models.CharField(max_length=140, blank=True)
    tompcds_subtitle_en = models.CharField(max_length=140, blank=True)
    tompcds_subtitle_nl = models.CharField(max_length=140, blank=True)
    get_in_touch_en = models.CharField(max_length=140, blank=True)
    get_in_touch_nl = models.CharField(max_length=140, blank=True)

    # Translated fields
    title = TranslatedField(
        'title',
        'title_nl',
    )

    travel_operators_subtitle = TranslatedField(
        'travel_operators_subtitle_en',
        'travel_operators_subtitle_nl',
    )

    maas_subtitle = TranslatedField(
        'maas_subtitle_en',
        'maas_subtitle_nl',
    )

    cities_subtitle = TranslatedField(
        'cities_subtitle_en',
        'cities_subtitle_nl',
    )

    tompapi_subtitle = TranslatedField(
        'tompapi_subtitle_en',
        'tompapi_subtitle_nl'
    )

    tompcds_subtitle = TranslatedField(
        'tompcds_subtitle_en',
        'tompcds_subtitle_nl'
    )

    get_in_touch = TranslatedField(
        'get_in_touch_en',
        'get_in_touch_nl'
    )

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('title_nl'),
        FieldPanel('travel_operators_subtitle_en', classname="full"),
        FieldPanel('travel_operators_subtitle_nl', classname="full"),
        FieldPanel('maas_subtitle_en', classname="full"),
        FieldPanel('maas_subtitle_nl', classname="full"),
        FieldPanel('cities_subtitle_en', classname="full"),
        FieldPanel('cities_subtitle_nl', classname="full"),
        FieldPanel('tompapi_subtitle_en', classname="full"),
        FieldPanel('tompapi_subtitle_nl', classname="full"),
        FieldPanel('tompcds_subtitle_en', classname="full"),
        FieldPanel('tompcds_subtitle_nl', classname="full"),
        FieldPanel('get_in_touch_en', classname="full"),
        FieldPanel('get_in_touch_nl', classname="full"),
        ImageChooserPanel('main_banner_image', classname="full"),
        ImageChooserPanel('tomp_api_image', classname="full"),
        ImageChooserPanel('tomp_cds_image', classname="full")
    ]
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)
        context['posts'] = Sections.objects.live().public().order_by('-created_at')
        return context

class Sections(Page):
    section_title = models.CharField(max_length=140, blank=True)
    content = StreamField(
        [
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True)

    content_panels = Page.content_panels + [
        FieldPanel('section_title'),
        StreamFieldPanel('content'),
    ]

class Contacts(models.Model):
    name = models.TextField(default='',null=False)
    email = models.EmailField()
    message = models.TextField(default='')

    def embed(self):
        return {'name':self.name,
                'email':self.email,
                'message':self.message}

