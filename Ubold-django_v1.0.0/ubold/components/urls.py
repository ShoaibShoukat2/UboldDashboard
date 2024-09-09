from django.urls import path

from .views import (
    components_base_ui_tabs_accordions_view,
    components_base_ui_avatars_view,
    components_base_ui_buttons_view,
    components_base_ui_cards_view,
    components_base_ui_carousel_view,
    components_base_ui_dropdowns_view,
    components_base_ui_video_view,
    components_base_ui_general_view,
    components_base_ui_grid_view,
    components_base_ui_images_view,
    components_base_ui_list_group_view,
    components_base_ui_modals_view,
    components_base_ui_notifications_view,
    components_base_ui_tooltips_popovers_view,
    components_base_ui_portlets_view,
    components_base_ui_progress_view,
    components_base_ui_ribbons_view,
    components_base_ui_spinners_view,
    components_base_ui_typography_view,
    components_base_ui_offcanvas_view,

    components_extended_dragula_view,
    components_extended_nestable_view,
    components_extended_range_slider_view,
    components_extended_animation_view,
    components_extended_sweet_alert_view,
    components_extended_tour_view,
    components_extended_loading_buttons_view,
    components_extended_scrollspy_view,

    components_widgets_view,

    components_icons_feather_view,
    components_icons_font_awesome_view,
    components_icons_simple_line_view,
    components_icons_themify_view,
    components_icons_two_tone_view,
    components_icons_weather_view,
    components_icons_mdi_view,
    components_icons_dripicons_view,


    components_forms_elements_view,
    components_forms_advanced_view,
    components_forms_validation_view,
    components_forms_pickers_view,
    components_forms_wizard_view,
    components_forms_masks_view,
    components_forms_quilljs_view,
    components_forms_file_uploads_view,
    components_forms_x_editable_view,
    components_forms_image_crop_view,

    components_charts_apex_view,
    components_charts_flot_view,
    components_charts_morris_view,
    components_charts_chartjs_view,
    components_charts_peity_view,
    components_charts_chartist_view,
    components_charts_c3_view,
    components_charts_sparklines_view,
    components_charts_knob_view,

    components_tables_basic_view,
    components_tables_datatables_view,
    components_tables_editable_view,
    components_tables_responsive_view,
    components_tables_footables_view,
    components_tables_bootstrap_view,
    components_tables_tablesaw_view,
    components_tables_jsgrid_view,

    components_maps_google_view,
    components_maps_vector_view,
    components_maps_mapael_view,
)


app_name = "components"
urlpatterns = [

    # base_ui
    path("base_ui/tabs-accordions", view=components_base_ui_tabs_accordions_view, name="components.base_ui.tabs-accordions"),
    path("base_ui/avatars", view=components_base_ui_avatars_view, name="components.base_ui.avatars"),
    path("base_ui/buttons", view=components_base_ui_buttons_view, name="components.base_ui.buttons"),
    path("base_ui/cards", view=components_base_ui_cards_view, name="components.base_ui.cards"),
    path("base_ui/carousel", view=components_base_ui_carousel_view, name="components.base_ui.carousel"),
    path("base_ui/dropdowns", view=components_base_ui_dropdowns_view, name="components.base_ui.dropdowns"),
    path("base_ui/video", view=components_base_ui_video_view, name="components.base_ui.video"),
    path("base_ui/general", view=components_base_ui_general_view, name="components.base_ui.general"),
    path("base_ui/grid", view=components_base_ui_grid_view, name="components.base_ui.grid"),
    path("base_ui/images", view=components_base_ui_images_view, name="components.base_ui.images"),
    path("base_ui/list-group", view=components_base_ui_list_group_view, name="components.base_ui.list-group"),
    path("base_ui/modals", view=components_base_ui_modals_view, name="components.base_ui.modals"),
    path("base_ui/notifications", view=components_base_ui_notifications_view, name="components.base_ui.notifications"),
    path("base_ui/tooltips-popovers", view=components_base_ui_tooltips_popovers_view, name="components.base_ui.tooltips-popovers"),
    path("base_ui/portlets", view=components_base_ui_portlets_view, name="components.base_ui.portlets"),
    path("base_ui/progress", view=components_base_ui_progress_view, name="components.base_ui.progress"),
    path("base_ui/ribbons", view=components_base_ui_ribbons_view, name="components.base_ui.ribbons"),
    path("base_ui/spinners", view=components_base_ui_spinners_view, name="components.base_ui.spinners"),
    path("base_ui/typography", view=components_base_ui_typography_view, name="components.base_ui.typography"),
    path("base_ui/offcanvas", view=components_base_ui_offcanvas_view, name="components.base_ui.offcanvas"),

    # extended
    path("extended/dragula", view=components_extended_dragula_view, name="components.extended.dragula"),
    path("extended/nestable", view=components_extended_nestable_view, name="components.extended.nestable"),
    path("extended/range-slider", view=components_extended_range_slider_view, name="components.extended.range-slider"),
    path("extended/animation", view=components_extended_animation_view, name="components.extended.animation"),
    path("extended/sweet-alert", view=components_extended_sweet_alert_view, name="components.extended.sweet-alert"),
    path("extended/tour", view=components_extended_tour_view, name="components.extended.tour"),
    path("extended/scrollspy", view=components_extended_scrollspy_view, name="components.extended.scrollspy"),
    path("extended/loading-buttons", view=components_extended_loading_buttons_view, name="components.extended.loading-buttons"),

    # widgets
    path("extended/widgets", view=components_widgets_view, name="components.widgets"),

    # icons
    path("icons/two-tone", view=components_icons_two_tone_view, name="components.icons.two-tone"),
    path("icons/feather", view=components_icons_feather_view, name="components.icons.feather"),
    path("icons/mdi", view=components_icons_mdi_view, name="components.icons.mdi"),
    path("icons/dripicons", view=components_icons_dripicons_view, name="components.icons.dripicons"),
    path("icons/font-awesome", view=components_icons_font_awesome_view, name="components.icons.font-awesome"),
    path("icons/themify", view=components_icons_themify_view, name="components.icons.themify"),
    path("icons/simple-line", view=components_icons_simple_line_view, name="components.icons.simple-line"),
    path("icons/weather", view=components_icons_weather_view, name="components.icons.weather"),

    # forms
    path("forms/elements", view=components_forms_elements_view, name="components.forms.elements"),
    path("forms/advanced", view=components_forms_advanced_view, name="components.forms.advanced"),
    path("forms/validation", view=components_forms_validation_view, name="components.forms.validation"),
    path("forms/pickers", view=components_forms_pickers_view, name="components.forms.pickers"),
    path("forms/wizard", view=components_forms_wizard_view, name="components.forms.wizard"),
    path("forms/masks", view=components_forms_masks_view, name="components.forms.masks"),
    path("forms/quilljs", view=components_forms_quilljs_view, name="components.forms.quilljs"),
    path("forms/file-uploads", view=components_forms_file_uploads_view, name="components.forms.file-uploads"),
    path("forms/x-editable", view=components_forms_x_editable_view, name="components.forms.x-editable"),
    path("forms/image-crop", view=components_forms_image_crop_view, name="components.forms.image-crop"),

    # charts
    path("charts/apex", view=components_charts_apex_view, name="components.charts.apex"),
    path("charts/flot", view=components_charts_flot_view, name="components.charts.flot"),
    path("charts/morris", view=components_charts_morris_view, name="components.charts.morris"),
    path("charts/chartjs", view=components_charts_chartjs_view, name="components.charts.chartjs"),
    path("charts/peity", view=components_charts_peity_view, name="components.charts.peity"),
    path("charts/chartist", view=components_charts_chartist_view, name="components.charts.chartist"),
    path("charts/c3", view=components_charts_c3_view, name="components.charts.c3"),
    path("charts/sparklines", view=components_charts_sparklines_view, name="components.charts.sparklines"),
    path("charts/knob", view=components_charts_knob_view, name="components.charts.knob"),

    # tables
    path("tables/basic", view=components_tables_basic_view, name="components.tables.basic"),
    path("tables/datatables", view=components_tables_datatables_view, name="components.tables.datatables"),
    path("tables/editable", view=components_tables_editable_view, name="components.tables.editable"),
    path("tables/responsive", view=components_tables_responsive_view, name="components.tables.responsive"),
    path("tables/footables", view=components_tables_footables_view, name="components.tables.footables"),
    path("tables/bootstrap", view=components_tables_bootstrap_view, name="components.tables.bootstrap"),
    path("tables/tablesaw", view=components_tables_tablesaw_view, name="components.tables.tablesaw"),
    path("tables/jsgrid", view=components_tables_jsgrid_view, name="components.tables.jsgrid"),

    # maps
    path("maps/google", view=components_maps_google_view, name="components.maps.google"),
    path("maps/vector", view=components_maps_vector_view, name="components.maps.vector"),
    path("maps/mapael", view=components_maps_mapael_view, name="components.maps.mapael"),
]
