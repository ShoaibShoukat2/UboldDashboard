from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()

class CustomView(LoginRequiredMixin, TemplateView):
    pass

#auth pages
custom_pages_coming_soon_view = CustomView.as_view(template_name="extra/coming-soon.html")
custom_pages_faqs_view = CustomView.as_view(template_name="extra/faqs.html")
custom_pages_gallery_view = CustomView.as_view(template_name="extra/gallery.html")
custom_pages_invoice_view = CustomView.as_view(template_name="extra/invoice.html")
custom_pages_maintenance_view = CustomView.as_view(template_name="extra/maintenance.html")
custom_pages_pricing_view = CustomView.as_view(template_name="extra/pricing.html")
custom_pages_search_results_view = CustomView.as_view(template_name="extra/search-results.html")
custom_pages_sitemap_view = CustomView.as_view(template_name="extra/sitemap.html")
custom_pages_starter_view = CustomView.as_view(template_name="extra/starter.html")
custom_pages_timeline_view = CustomView.as_view(template_name="extra/timeline.html")
custom_pages_404_alt_view = CustomView.as_view(template_name="extra/404-alt.html")
custom_pages_404_two_view = CustomView.as_view(template_name="extra/404-two.html")
custom_pages_404_view = CustomView.as_view(template_name="extra/404.html")
custom_pages_500_two_view = CustomView.as_view(template_name="extra/500-two.html")
custom_pages_500_view = CustomView.as_view(template_name="extra/500.html")