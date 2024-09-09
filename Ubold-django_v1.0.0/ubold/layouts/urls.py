from django.urls import path

from .views import (
    horizontal_layouts_view,
    detached_layouts_view,
    two_column_layouts_view,
    two_tone_icons_layouts_view,
    preloader_layouts_view,
    )

app_name = "layouts"

urlpatterns = [
    path("horizontal", view=horizontal_layouts_view, name="layouts.horizontal"),
    path("detached", view=detached_layouts_view, name="layouts.detached"),
    path("two_column_layouts", view=two_column_layouts_view, name="layouts.two_column_layouts"),
    path("two_tone_icons_layouts", view=two_tone_icons_layouts_view, name="layouts.two_tone_icons_layouts"),
    path("preloader_layouts", view=preloader_layouts_view, name="layouts.preloader_layouts"),
]
