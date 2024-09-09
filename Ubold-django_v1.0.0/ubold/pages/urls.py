from django.urls import path

from .views import (

    custom_pages_coming_soon_view,
    custom_pages_faqs_view,
    custom_pages_gallery_view,
    custom_pages_invoice_view,
    custom_pages_maintenance_view,
    custom_pages_pricing_view,
    custom_pages_search_results_view,
    custom_pages_sitemap_view,
    custom_pages_starter_view,
    custom_pages_timeline_view,
    custom_pages_404_alt_view,
    custom_pages_404_two_view,
    custom_pages_404_view,
    custom_pages_500_two_view,
    custom_pages_500_view,
)


app_name = "pages"
urlpatterns = [

    # pages
    path("coming-soon", view=custom_pages_coming_soon_view, name="coming-soon"),
    path("faqs", view=custom_pages_faqs_view, name="faqs"),
    path("gallery", view=custom_pages_gallery_view, name="gallery"),
    path("invoice", view=custom_pages_invoice_view, name="invoice"),
    path("maintenance", view=custom_pages_maintenance_view, name="maintenance"),
    path("pricing", view=custom_pages_pricing_view, name="pricing"),
    path("search-results", view=custom_pages_search_results_view, name="search-results"),
    path("sitemap", view=custom_pages_sitemap_view, name="sitemap"),
    path("starter", view=custom_pages_starter_view, name="starter"),
    path("timeline", view=custom_pages_timeline_view, name="timeline"),
    path("404-alt", view=custom_pages_404_alt_view, name="404-alt"),
    path("404-two", view=custom_pages_404_two_view, name="404-two"),
    path("404", view=custom_pages_404_view, name="404"),
    path("500", view=custom_pages_500_view, name="500"),
    path("500-two", view=custom_pages_500_two_view, name="500-two"),
]
