from django.urls import path

from .views import (
    apps_calendar_calendar_view,
    apps_chat_chat_view,

    apps_companies_view,

    apps_ecommerce_ecommerce_dashboard_view,

    apps_ecommerce_checkout_view,
    apps_ecommerce_customers_view,
    apps_ecommerce_order_detail_view,
    apps_ecommerce_orders_view,
    apps_ecommerce_product_edit_view,
    apps_ecommerce_products_details_view,
    apps_ecommerce_products_view,
    apps_ecommerce_sellers_view,
    apps_ecommerce_cart_view,

    apps_crm_dashboard_view,
    apps_crm_contacts_view,
    apps_crm_opportunities_view,
    apps_crm_leads_view,
    apps_crm_customers_view,

    apps_contacts_list_view,
    apps_contacts_profile_view,

    apps_file_manager_view,

    apps_email_inbox_view,
    apps_email_read_view,
    apps_email_compose_view,
    apps_email_templates_view,
    apps_email_templates_action_view,
    apps_email_templates_alert_view,
    apps_email_templates_billing_view,
    apps_email_send_view,
    apps_email_recieve_view,


    apps_project_create_view,
    apps_project_detail_view,
    apps_project_list_view,

    apps_social_feed_view,

    apps_task_details_view,
    apps_task_kanban_board_view,
    apps_task_list_view,

    apps_tickets_list_view,
    apps_tickets_detail_view,

    # event
    EventListView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    
    #domain
    AppsDomainAddDomainView,
    AppsDomainVerifyDomainView,
    AppsEmailReceiveBoxView

    


)




app_name = "apps"
urlpatterns = [
     
    #domain
    
     path("adddomain/", AppsDomainAddDomainView.as_view(), name="add-domain"),
     path("verifydomain/", AppsDomainVerifyDomainView.as_view(), name="verify-domain"),
     path("recieve-domain/", AppsEmailReceiveBoxView.as_view(), name="recieve-domain"),
     
     
     
     
    

    
    

     
    # calendar
    path("event/", view=EventListView.as_view(), name="event-list"),
    path("event/add/", view=EventCreateView.as_view(), name="event-add"),
    path("event/edit/<pk>", view=EventUpdateView.as_view(), name="event-edit"),
    path("event/remove/<pk>", view=EventDeleteView.as_view(), name="event-remove"),
    path("calendar", view=apps_calendar_calendar_view, name="calendar"),

    # chat
    path("chat", view=apps_chat_chat_view, name="chat"),

    # crm
    path("crm/customers", view=apps_crm_customers_view, name="crm.customers"),
    path("crm/contacts", view=apps_crm_contacts_view, name="crm.contacts"),
    path("crm/dashboard", view=apps_crm_dashboard_view, name="crm.dashboard"),
    path("crm/leads", view=apps_crm_leads_view, name="crm.leads"),
    path("crm/opportunities", view=apps_crm_opportunities_view, name="crm.opportunities"),

    # companies
    path("companies/companies", view=apps_companies_view, name="companies.companies"),

    # contacts
    path("contacts/list", view=apps_contacts_list_view, name="contacts.list"),
    path("contacts/profile", view=apps_contacts_profile_view, name="contacts.profile"),

    # ecommerce
    path("ecommerce/checkout", view=apps_ecommerce_checkout_view, name="ecommerce.checkout"),
    path("ecommerce/customers", view=apps_ecommerce_customers_view, name="ecommerce.customers"),
    path("ecommerce/dashboard",
         view=apps_ecommerce_ecommerce_dashboard_view, name="ecommerce.dashboard"),
    path("ecommerce/order-detail", view=apps_ecommerce_order_detail_view,
         name="ecommerce.order-detail"),
    path("ecommerce/orders", view=apps_ecommerce_orders_view, name="ecommerce.orders"),
    path("ecommerce/product-edit", view=apps_ecommerce_product_edit_view, name="ecommerce.product-edit"),
    path("ecommerce/product-detail", view=apps_ecommerce_products_details_view,
         name="ecommerce.product-detail"),
    path("ecommerce/products", view=apps_ecommerce_products_view, name="ecommerce.products"),
    path("ecommerce/sellers", view=apps_ecommerce_sellers_view, name="ecommerce.sellers"),
    path("ecommerce/cart", view=apps_ecommerce_cart_view,
         name="ecommerce.cart"),
    
    
    
    
    
    
    
    

    # email
    path("email/inbox", view=apps_email_inbox_view, name="email.inbox"),
    path("email/read", view=apps_email_read_view, name="email.read"),
    path("email/compose", view=apps_email_compose_view, name="email.compose"),
    path("email/templates", view=apps_email_templates_view, name="email.templates"),
    path("email/templates-action", view=apps_email_templates_action_view, name="email.templates-action"),
    path("email/templates-alert", view=apps_email_templates_alert_view, name="email.templates-alert"),
    path("email/templates-billing", view=apps_email_templates_billing_view,
         name="email.templates-billing"),
    
    path("email/send", view=apps_email_send_view, name="email.send"),
    path("email/recieve", view=apps_email_recieve_view, name="email.recieve"),
    
    






    

    # manager
    path("manager/file-manager", view=apps_file_manager_view, name="manager.file-manager"),

    # projects //TODO
    path("project/create", view=apps_project_create_view, name="project.create"),
    path("project/detail", view=apps_project_detail_view, name="project.detail"),
    path("project/list", view=apps_project_list_view, name="project.list"),

    # social
    path("social/feed", view=apps_social_feed_view, name="social.feed"),

    # tasks
    path("task/details", view=apps_task_details_view, name="task.details"),
    path("task/kanban-board", view=apps_task_kanban_board_view, name="task.kanban-board"),
    path("task/list", view=apps_task_list_view, name="task.list"),

    # tickets
    path("tickets/list", view=apps_tickets_list_view, name="tickets.list"),
    path("tickets/detail", view=apps_tickets_detail_view, name="tickets.detail"),

]


