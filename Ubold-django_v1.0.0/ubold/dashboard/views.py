import json
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

from ubold.utils.general import list_of_dict_to_list_to_obj, GenericObject
from ubold.dashboard.data.store import (
    topUsersBalancesDict,
    revenueHistoryDict,
    topSellingProductsDict,
    inboxDict,
    projectsDict,
    statisticsDashboard1Dict,
    statisticsDashboard2Dict,
    projectionsVsActualsStatDist,
    revenueStatDist,
    lifetimeSalesStatDict,
    dashboard4BarChartStatDict,
    incomeAmountsStatDict,
    showcaseUsersDict
)

from ubold.dashboard.data.charts_data import (
    totalRevenue,
    salesAnalyticsDict,
    lifetimeSalesSeries1,
    lifetimeSalesSeries2,
    incomeAmounts,
    totalUsers,
    revenueDict,
    projectionsVsActualsDict,
    lifetimeSalesDonutDict,
    dashboard4BarChartDict,
    incomeAmountsChartDict
)

User = get_user_model()


class DashboardOneView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topUsersBalances"] = list_of_dict_to_list_to_obj(
            topUsersBalancesDict)
        context["revenueHistory"] = list_of_dict_to_list_to_obj(
            revenueHistoryDict)
        context["total_revenue"] = totalRevenue
        context["salesAnalytics"] = json.dumps(salesAnalyticsDict)
        context['statistics'] = list_of_dict_to_list_to_obj(
            statisticsDashboard1Dict)
        return context


first_dashboard_view = DashboardOneView.as_view()



class DashboardSecondView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard-2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topSellingProducts"] = list_of_dict_to_list_to_obj(
            topSellingProductsDict)
        context['statistics'] = list_of_dict_to_list_to_obj(
            statisticsDashboard2Dict)
        context['lifetimeSalesSeries1'] = lifetimeSalesSeries1
        context['lifetimeSalesSeries2'] = lifetimeSalesSeries2
        context['incomeAmounts'] = incomeAmounts
        context['totalUsers'] = totalUsers
        return context


second_dashboard_view = DashboardSecondView.as_view()


class DashboardThirdView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard-3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inbox"] = list_of_dict_to_list_to_obj(inboxDict)
        context["revenue"] = json.dumps(revenueDict)
        context["projectionsVsActuals"] = json.dumps(projectionsVsActualsDict)
        context["projectionsVsActualsStat"] = GenericObject(projectionsVsActualsStatDist)
        context["revenueStat"] = GenericObject(revenueStatDist)
        return context


thrid_dashboard_view = DashboardThirdView.as_view()


class DashboardForthView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard-4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = []
        for data in projectsDict:
            obj = GenericObject(data)
            obj.Team = list_of_dict_to_list_to_obj(obj.Team)
            context["projects"].append(obj)
        context["lifetimeSalesDonut"] = GenericObject(lifetimeSalesDonutDict)
        context["dashboard4BarChart"] = json.dumps(dashboard4BarChartDict)
        context["incomeAmountsChart"] = json.dumps(incomeAmountsChartDict)
        context["lifetimeSalesStat"] = GenericObject(lifetimeSalesStatDict)
        context["dashboard4BarChartStat"] = GenericObject(dashboard4BarChartStatDict)
        context["incomeAmountsStat"] = GenericObject(incomeAmountsStatDict)
        context["showcaseUsers"] = list_of_dict_to_list_to_obj(showcaseUsersDict)
        return context




forth_dashboard_view = DashboardForthView.as_view()


# demo
demo_default_rtl_view = DashboardOneView.as_view(template_name="demos/default-rtl.html")
demo_default_dark_view = DashboardOneView.as_view(template_name="demos/default-dark.html")

demo_purple_view = DashboardOneView.as_view(template_name="demos/purple.html")
demo_purple_rtl_view = DashboardOneView.as_view(template_name="demos/purple-rtl.html")
demo_purple_dark_view = DashboardOneView.as_view(template_name="demos/purple-dark.html")

demo_material_view = DashboardOneView.as_view(template_name="demos/material.html")
demo_material_rtl_view = DashboardOneView.as_view(template_name="demos/material-rtl.html")
demo_material_dark_view = DashboardOneView.as_view(template_name="demos/material-dark.html")

demo_creative_horizontal_view = TemplateView.as_view(template_name="demos/creative-horizontal.html")
demo_creative_horizontal_rtl_view = TemplateView.as_view(template_name="demos/creative-horizontal-rtl.html")
demo_creative_horizontal_dark_view = TemplateView.as_view(template_name="demos/creative-horizontal-dark.html")

demo_modern_detached_view = TemplateView.as_view(template_name="demos/modern-detached.html")
demo_modern_detached_rtl_view = TemplateView.as_view(template_name="demos/modern-detached-rtl.html")
demo_modern_detached_dark_view = TemplateView.as_view(template_name="demos/modern-detached-dark.html")

demo_saas_two_column_view = TemplateView.as_view(template_name="demos/saas-two-column.html")
demo_saas_two_column_rtl_view = TemplateView.as_view(template_name="demos/saas-two-column-rtl.html")
demo_saas_two_column_dark_view = TemplateView.as_view(template_name="demos/saas-two-column-dark.html")