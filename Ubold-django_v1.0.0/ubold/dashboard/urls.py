from django.urls import path

from .views import (
    forth_dashboard_view,
    thrid_dashboard_view,
    second_dashboard_view,
    first_dashboard_view,
    # demo
    demo_default_rtl_view,
    demo_default_dark_view,
    demo_purple_view,
    demo_purple_dark_view,
    demo_purple_rtl_view,
    demo_creative_horizontal_view,
    demo_creative_horizontal_dark_view,
    demo_creative_horizontal_rtl_view,
    demo_material_view,
    demo_material_dark_view,
    demo_material_rtl_view,
    demo_modern_detached_view,
    demo_modern_detached_dark_view,
    demo_modern_detached_rtl_view,
    demo_saas_two_column_dark_view,
    demo_saas_two_column_rtl_view,
    demo_saas_two_column_view,
)

app_name = "dashboard"
urlpatterns = [

    # demo
    path("demo/default-rtl", view=demo_default_rtl_view, name="demo.default-rtl"),
    path("demo/default-dark", view=demo_default_dark_view, name="demo.default-dark"),
    path("demo/purple", view=demo_purple_view, name="demo.purple"),
    path("demo/purple-rtl", view=demo_purple_rtl_view, name="demo.purple-rtl"),
    path("demo/purple-dark", view=demo_purple_dark_view, name="demo.purple-dark"),
    path("demo/creative-horizontal", view=demo_creative_horizontal_view, name="demo.creative-horizontal"),
    path("demo/creative-horizontal-rtl", view=demo_creative_horizontal_rtl_view, name="demo.creative-horizontal-rtl"),
    path("demo/creative-horizontal-dark", view=demo_creative_horizontal_dark_view, name="demo.creative-horizontal-dark"),
    path("demo/material", view=demo_material_view, name="demo.material"),
    path("demo/material-rtl", view=demo_material_rtl_view, name="demo.material-rtl"),
    path("demo/material-dark", view=demo_material_dark_view, name="demo.material-dark"),
    path("demo/modern-detached", view=demo_modern_detached_view, name="demo.modern-detached"),
    path("demo/modern-detached-rtl", view=demo_modern_detached_rtl_view, name="demo.modern-detached-rtl"),
    path("demo/modern-detached-dark", view=demo_modern_detached_dark_view, name="demo.modern-detached-dark"),
    path("demo/saas-two-column", view=demo_saas_two_column_view, name="demo.saas-two-column"),
    path("demo/saas-two-column-rtl", view=demo_saas_two_column_rtl_view, name="demo.saas-two-column-rtl"),
    path("demo/saas-two-column-dark", view=demo_saas_two_column_dark_view, name="demo.saas-two-column-dark"),

    path("dashboard-4", view=forth_dashboard_view, name="dashboard-4"),
    path("dashboard-3", view=thrid_dashboard_view, name="dashboard-3"),
    path("dashboard-2", view=second_dashboard_view, name="dashboard-2"),
    path("index", view=first_dashboard_view, name="index"),
]
