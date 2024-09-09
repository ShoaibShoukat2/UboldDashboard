from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()

class ComponentsView(LoginRequiredMixin, TemplateView):
    pass

# ecommerce
components_base_ui_tabs_accordions_view = ComponentsView.as_view(template_name="components/base-ui/tabs-accordions.html")
components_base_ui_avatars_view = ComponentsView.as_view(template_name="components/base-ui/avatars.html")
components_base_ui_buttons_view = ComponentsView.as_view(template_name="components/base-ui/buttons.html")
components_base_ui_cards_view = ComponentsView.as_view(template_name="components/base-ui/cards.html")
components_base_ui_carousel_view = ComponentsView.as_view(template_name="components/base-ui/carousel.html")
components_base_ui_dropdowns_view = ComponentsView.as_view(template_name="components/base-ui/dropdowns.html")
components_base_ui_video_view = ComponentsView.as_view(template_name="components/base-ui/video.html")
components_base_ui_general_view = ComponentsView.as_view(template_name="components/base-ui/general.html")
components_base_ui_grid_view = ComponentsView.as_view(template_name="components/base-ui/grid.html")
components_base_ui_images_view = ComponentsView.as_view(template_name="components/base-ui/images.html")
components_base_ui_list_group_view = ComponentsView.as_view(template_name="components/base-ui/list-group.html")
components_base_ui_modals_view = ComponentsView.as_view(template_name="components/base-ui/modals.html")
components_base_ui_notifications_view = ComponentsView.as_view(template_name="components/base-ui/notifications.html")
components_base_ui_tooltips_popovers_view = ComponentsView.as_view(template_name="components/base-ui/tooltips-popovers.html")
components_base_ui_portlets_view = ComponentsView.as_view(template_name="components/base-ui/portlets.html")
components_base_ui_progress_view = ComponentsView.as_view(template_name="components/base-ui/progress.html")
components_base_ui_ribbons_view = ComponentsView.as_view(template_name="components/base-ui/ribbons.html")
components_base_ui_spinners_view = ComponentsView.as_view(template_name="components/base-ui/spinners.html")
components_base_ui_typography_view = ComponentsView.as_view(template_name="components/base-ui/typography.html")
components_base_ui_offcanvas_view = ComponentsView.as_view(template_name="components/base-ui/offcanvas.html")


# extended
components_extended_dragula_view = ComponentsView.as_view(template_name="components/extended/dragula.html")
components_extended_nestable_view = ComponentsView.as_view(template_name="components/extended/nestable.html")
components_extended_range_slider_view = ComponentsView.as_view(template_name="components/extended/range-slider.html")
components_extended_animation_view = ComponentsView.as_view(template_name="components/extended/animation.html")
components_extended_sweet_alert_view = ComponentsView.as_view(template_name="components/extended/sweet-alert.html")
components_extended_tour_view = ComponentsView.as_view(template_name="components/extended/tour.html")
components_extended_scrollspy_view = ComponentsView.as_view(template_name="components/extended/scrollspy.html")
components_extended_loading_buttons_view = ComponentsView.as_view(template_name="components/extended/loading-buttons.html")

# widgets
components_widgets_view = ComponentsView.as_view(template_name="components/widgets.html")

# icons
components_icons_two_tone_view = ComponentsView.as_view(template_name="components/icons/two-tone.html")
components_icons_feather_view = ComponentsView.as_view(template_name="components/icons/feather.html")
components_icons_mdi_view = ComponentsView.as_view(template_name="components/icons/mdi.html")
components_icons_dripicons_view = ComponentsView.as_view(template_name="components/icons/dripicons.html")
components_icons_font_awesome_view = ComponentsView.as_view(template_name="components/icons/font-awesome.html")
components_icons_themify_view = ComponentsView.as_view(template_name="components/icons/themify.html")
components_icons_simple_line_view = ComponentsView.as_view(template_name="components/icons/simple-line.html")
components_icons_weather_view = ComponentsView.as_view(template_name="components/icons/weather.html")

# forms
components_forms_elements_view = ComponentsView.as_view(template_name="components/forms/elements.html")
components_forms_advanced_view = ComponentsView.as_view(template_name="components/forms/advanced.html")
components_forms_validation_view = ComponentsView.as_view(template_name="components/forms/validation.html")
components_forms_pickers_view = ComponentsView.as_view(template_name="components/forms/pickers.html")
components_forms_wizard_view = ComponentsView.as_view(template_name="components/forms/wizard.html")
components_forms_masks_view = ComponentsView.as_view(template_name="components/forms/masks.html")
components_forms_quilljs_view = ComponentsView.as_view(template_name="components/forms/quilljs.html")
components_forms_file_uploads_view = ComponentsView.as_view(template_name="components/forms/file-uploads.html")
components_forms_x_editable_view = ComponentsView.as_view(template_name="components/forms/x-editable.html")
components_forms_image_crop_view = ComponentsView.as_view(template_name="components/forms/image-crop.html")



# charts
components_charts_apex_view = ComponentsView.as_view(template_name="components/charts/apex.html")
components_charts_flot_view = ComponentsView.as_view(template_name="components/charts/flot.html")
components_charts_morris_view = ComponentsView.as_view(template_name="components/charts/morris.html")
components_charts_chartjs_view = ComponentsView.as_view(template_name="components/charts/chartjs.html")
components_charts_peity_view = ComponentsView.as_view(template_name="components/charts/peity.html")
components_charts_chartist_view = ComponentsView.as_view(template_name="components/charts/chartist.html")
components_charts_c3_view = ComponentsView.as_view(template_name="components/charts/c3.html")
components_charts_sparklines_view = ComponentsView.as_view(template_name="components/charts/sparklines.html")
components_charts_knob_view = ComponentsView.as_view(template_name="components/charts/knob.html")


# tables
components_tables_basic_view = ComponentsView.as_view(template_name="components/tables/basic.html")
components_tables_datatables_view = ComponentsView.as_view(template_name="components/tables/datatables.html")
components_tables_editable_view = ComponentsView.as_view(template_name="components/tables/editable.html")
components_tables_responsive_view = ComponentsView.as_view(template_name="components/tables/responsive.html")
components_tables_footables_view = ComponentsView.as_view(template_name="components/tables/footables.html")
components_tables_bootstrap_view = ComponentsView.as_view(template_name="components/tables/bootstrap.html")
components_tables_tablesaw_view = ComponentsView.as_view(template_name="components/tables/tablesaw.html")
components_tables_jsgrid_view = ComponentsView.as_view(template_name="components/tables/jsgrid.html")

# maps
components_maps_google_view = ComponentsView.as_view(template_name="components/maps/google.html")
components_maps_vector_view = ComponentsView.as_view(template_name="components/maps/vector.html")
components_maps_mapael_view = ComponentsView.as_view(template_name="components/maps/mapael.html")