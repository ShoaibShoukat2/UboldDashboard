import json
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import SentEmail, ReceivedEmail
from django.utils import timezone
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render
from django.db import transaction
from ubold.apps.models import Event
from ubold.apps.forms import EventForm
from django.contrib import messages
from django.shortcuts import redirect
from dotenv import load_dotenv
import os
from .models import Email 
from django.http import HttpResponseRedirect
from ubold.utils.general import list_of_dict_to_list_to_obj, GenericObject
from ubold.apps.data.ecommerce import (
    ecommerceStatisticsDict, 
    transactionHistoryDict,
    recentProductsDict,
    productsDict,
    outletDict,
    productDetailDict,
    customersDict,
    ordersDict,
    orderDict,
    sellersDict,
    cartProductsDict,
    cartSummaryDict,
    cartDiscountCode,
    cartDiscountRate,
    checkoutFastDeliveryDict,
    checkoutHomeAddress,
    checkoutOfficeAddress,
    checkoutOrderDict,
    checkoutStandardDeliveryDict,
    )

User = get_user_model()

# Load environment variables from .env file
load_dotenv()

MY_SENDGRID_API_KEY = os.getenv('MY_SENDGRID_API_KEY')

class EventListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        events_dict = []
        for event in events:
            events_dict.append(event.to_dict())
        return HttpResponse(json.dumps(events_dict), content_type='application/json')

class EventCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = EventForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            save_data = {}
            save_data["title"] = cleaned_data.get("title")
            save_data["category"] = cleaned_data.get("className")
            save_data["start_date"] = cleaned_data.get("start")
            if cleaned_data.get("allDay", None):
                save_data["all_day"] = cleaned_data.get("allDay")
            if cleaned_data.get("end", None):
                save_data["end_date"] = cleaned_data.get("end")
            event = Event.objects.create(**save_data)
            return HttpResponse(json.dumps(event.to_dict()), content_type='application/json')
        return HttpResponseBadRequest(json.dumps(form.errors), content_type='application/json')

class EventUpdateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        obj = get_object_or_404(Event, id=pk)
        form = EventForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            obj.title = cleaned_data.get("title")
            obj.category = cleaned_data.get("className")
            obj.start_date = cleaned_data.get("start")
            obj.all_day = cleaned_data.get("allDay", None)
            obj.end_date = cleaned_data.get("end", None)
            obj.save()
            return HttpResponse(json.dumps(obj.to_dict()), content_type='application/json')
        return HttpResponseBadRequest(json.dumps(form.errors), content_type='application/json')

class EventDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        obj = get_object_or_404(Event, id=pk)
        obj.delete()
        return HttpResponse(
            json.dumps({"message" : "The event has been removed successfully."}), 
            content_type='application/json'
            )        






class AppsView(LoginRequiredMixin, TemplateView):
    template_name = "apps/email/compose.html" 

    def post(self, request, *args, **kwargs):
        if self.template_name == "apps/email/compose.html":
            return self.handle_compose_post(request)
        
        elif self.template_name == "apps/email/recieve_mail.html":
            
            return self.handle_receive_mail_post(request)          
            
                

        
        return render(request, self.template_name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def handle_receive_mail_post(self, request):
        # Handle form submission from recieve_mail.html
        sender = request.POST.get('sender')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        
        # Save to your model or perform other actions
        # For example:
        received_email = ReceivedEmail(sender=sender, subject=subject, content=content)
        received_email.save()
        
        # Redirect or render a success message
        return render(request, self.template_name, {"message": "Email Recieve successfully"})
    




















    


    def handle_compose_post(self, request):
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        recipient = request.POST.get('recipient')

        # Sending email using SendGrid API
        try:
            response_status, response_body, response_headers = send_email(
                sg = sendgrid.SendGridAPIClient(api_key=MY_SENDGRID_API_KEY),
                from_email='info@learnity.store',
                to_emails=[recipient],
                subject=subject,
                content=body
            )
            

            
            if response_status == 202:
                # Save data to PostgreSQL
                self.save_email_to_database(subject, body, recipient)
                
                # Handle success - perhaps redirect or render a success message
                return render(request, self.template_name, {"message": "Email sent successfully"})
            else:
                # Handle SendGrid API error
                return render(request, self.template_name, {"error": "Failed to send email. Please try again."})
        
        except Exception as e:
            # Handle other exceptions



            return render(request, self.template_name, {"error": str(e)})

    def save_email_to_database(self, subject, body, recipient):
        # Save sent email data to PostgreSQL
        with transaction.atomic():
            SentEmail.objects.create(subject=subject, body=body, recipient=recipient)
            
            
            
                            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.template_name == "apps/email/send_mail.html":
            context['sent_emails'] = SentEmail.objects.all()
            
        elif self.template_name == "apps/email/inbox.html":

            # Retrieve all sent emails
            sent_emails = SentEmail.objects.all()
            
            # Retrieve all received emails
            received_emails = ReceivedEmail.objects.all()
            
            # Combine both types of emails into a single list with type indicator
            combined_emails = []
            for email in sent_emails:
                combined_emails.append({
                    'type': 'sent',
                    'sender_or_recipient': email.recipient,
                    'subject': email.subject,
                    'content': email.body,
                    'date': email.sent_at,
                })
            for email in received_emails:
                combined_emails.append({
                    'type': 'received',
                    'sender_or_recipient': email.sender,
                    'subject': email.subject,
                    'content': email.content,
                    'date': email.received_at,
                })
            
            context['combined_emails'] = combined_emails  
            
            
            return context  
            
        return context


                        

def send_email(api_key, from_email, to_emails, subject, content):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        return response.status_code, response.body, response.headers
    except Exception as e:
        return 0, str(e), None


SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')




class AppsDomainAddDomainView(View):
    template_name = "apps/domain/adddomain.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        domain = request.POST.get('domain')
        context = {}

        if not domain:
            context['messages'] = [{'text': "Please enter a domain.", 'tags': 'danger'}]
            return render(request, self.template_name, context)

        domain_info = self.add_domain_to_sendgrid(domain)

        if 'id' not in domain_info:
            error_message = self.format_error_message(domain_info)
            context['messages'] = [{'text': f"Error adding domain to SendGrid: {error_message}", 'tags': 'danger'}]
            return render(request, self.template_name, context)

        dns_records = self.get_dns_records(domain_info)
        context['messages'] = [{'text': "Domain added successfully! Please add the following DNS records to your domain's DNS settings.", 'tags': 'success'}]
        context['dns_records'] = dns_records
        context['domain_info'] = domain_info

        return render(request, self.template_name, context)

    def add_domain_to_sendgrid(self, domain):
        url = "https://api.sendgrid.com/v3/whitelabel/domains"
        headers = {
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "domain": domain,
            "automatic_security": True
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    


    def get_dns_records(self, domain_info):
        dns_records = []
        dns_info = domain_info.get('dns', {})
        for key, record in dns_info.items():
            dns_records.append({
                "type": record['type'],
                "name": record['host'],
                "content": record['data'],
                "ttl": 120  # Default TTL value
            })
        return dns_records

    def format_error_message(self, response_json):
        if 'errors' in response_json:
            return '; '.join([error['message'] for error in response_json['errors']])
        return "An unknown error occurred."








class AppsDomainVerifyDomainView(View):
    def post(self, request):
        domain_id = request.POST.get('domain_id')
        verification_result = self.verify_domain(domain_id)

        context = {
            "messages": []
        }

        if verification_result.get('valid', False):
            context['messages'].append({'text': "Domain verification successful!", 'tags': 'success'})
        else:
            error_message = self.format_error_message(verification_result)
            context['messages'].append({'text': f"Domain verification failed: {error_message}", 'tags': 'danger'})

        return render(request, 'apps/domain/adddomain.html', context)

    def verify_domain(self, domain_id):
        url = f"https://api.sendgrid.com/v3/whitelabel/domains/{domain_id}/validate"
        headers = {
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError on bad status
            return response.json()
        except requests.RequestException as e:
            return {"valid": False, "error": str(e)}

    def format_error_message(self, response_json):
        if 'errors' in response_json:
            return '; '.join([error['message'] for error in response_json['errors']])
        return "An unknown error occurred."
    
    
    
    
class AppsEmailReceiveBoxView(LoginRequiredMixin, TemplateView):
    template_name = "apps/domain/receive_mail_end.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch and display email data
        context['emails'] = Email.objects.all()  # Adjust as needed to display emails
        return context

    def post(self, request, *args, **kwargs):
        domain = request.POST.get('domain')
        url = request.POST.get('url')

        if domain and url:
            # Save domain and URL configuration
            self.save_domain_and_url(domain, url)
            messages.success(request, "Domain and URL configuration saved successfully.")
        else:
            messages.error(request, "Domain and URL are required.")

        return HttpResponseRedirect(request.path_info)
   
   
    

    def save_domain_and_url(self, domain, url):
        # Here you can save the domain and URL to your database or a configuration file
        # For demonstration, we'll just print the values
        print(f"Saving domain: {domain} and URL: {url}")
        # Implement saving logic here
        
        

    @staticmethod
    def process_email_webhook(request):
        """ Process incoming email data from SendGrid """
        try:
            # Parse the incoming JSON data from SendGrid
            data = json.loads(request.body.decode('utf-8'))
            
            # Process each email entry
            for email_data in data:
                Email.objects.create(
                    domain=email_data.get('domain', ''),
                    subject=email_data.get('subject', ''),
                    body=email_data.get('body', ''),
                    received_at=email_data.get('timestamp', '')
                )
            
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# View instance
apps_email_receive_box_view = AppsEmailReceiveBoxView.as_view()




# Define the view for adding a domain
apps_domain_adddomain_view = TemplateView.as_view(template_name="apps/domain/adddomain.html")

# Define the view for verifying a domain
apps_domain_verifydomain_view = TemplateView.as_view(template_name="apps/domain/verifydomain.html")



# calendar
apps_calendar_calendar_view = AppsView.as_view(template_name="apps/calendar/calendar.html")

#chat
apps_chat_chat_view = AppsView.as_view(template_name="apps/chat/chat.html")

# companies
apps_companies_view = AppsView.as_view(template_name="apps/companies/companies.html")

# contacts
apps_contacts_list_view = AppsView.as_view(template_name="apps/contacts/list.html")
apps_contacts_profile_view = AppsView.as_view(template_name="apps/contacts/profile.html")

# crm
apps_crm_customers_view = AppsView.as_view(template_name="apps/crm/customers.html")
apps_crm_contacts_view = AppsView.as_view(template_name="apps/crm/contacts.html")
apps_crm_dashboard_view = AppsView.as_view(template_name="apps/crm/dashboard.html")
apps_crm_leads_view = AppsView.as_view(template_name="apps/crm/leads.html")
apps_crm_opportunities_view = AppsView.as_view(template_name="apps/crm/opportunities.html")

# ecommerce

class EcommerceDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statistics'] = list_of_dict_to_list_to_obj(
            ecommerceStatisticsDict)
        context['transactionHistory'] = list_of_dict_to_list_to_obj(
            transactionHistoryDict)
        context['recentProducts'] = list_of_dict_to_list_to_obj(
            recentProductsDict)
        return context
apps_ecommerce_ecommerce_dashboard_view = EcommerceDashboardView.as_view()

class EcommerceProductsView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_list = list_of_dict_to_list_to_obj(
            productsDict)
        n = 4
        context['products'] = [products_list[i:i + n] for i in range(0, len(products_list), n)]  
        return context
apps_ecommerce_products_view = EcommerceProductsView.as_view()


class EcommerceProductDetailView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/product-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outletData'] = list_of_dict_to_list_to_obj(outletDict)
        productDetailData = GenericObject(productDetailDict)
        context["productImages"] = productDetailData.images
        context["productDetail"] = productDetailData.detail
        return context
apps_ecommerce_products_details_view = EcommerceProductDetailView.as_view()

class EcommerceCustomersView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/customers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = list_of_dict_to_list_to_obj(customersDict)
        return context
apps_ecommerce_customers_view = EcommerceCustomersView.as_view()

class EcommerceOrdersView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = []
        for data in ordersDict:
            obj = GenericObject(data)
            obj.products = list_of_dict_to_list_to_obj(obj.products)
            context["orders"].append(obj)
        return context
apps_ecommerce_orders_view = EcommerceOrdersView.as_view()

class EcommerceOrderDetailView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/order-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        trackerData = list_of_dict_to_list_to_obj(orderDict["trackOrderData"]["trackerData"])
        prodects = list_of_dict_to_list_to_obj(orderDict["billData"]["prodects"])
        context["order"] = GenericObject(orderDict)
        context["order"]["trackOrderData"]["trackerData"] = trackerData
        context["order"]["billData"]["prodects"] = prodects
        return context
apps_ecommerce_order_detail_view = EcommerceOrderDetailView.as_view()




class EcommerceSellersView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/sellers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["sellers"] = list_of_dict_to_list_to_obj(sellersDict)
        return context
apps_ecommerce_sellers_view = EcommerceSellersView.as_view()




class EcommerceCartView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cartProducts"] = list_of_dict_to_list_to_obj(cartProductsDict)
        context["cartSummary"] = GenericObject(cartSummaryDict)
        context["cartDiscountCode"] = cartDiscountCode
        context["cartDiscountRate"] = cartDiscountRate
        return context
apps_ecommerce_cart_view = EcommerceCartView.as_view()


class EcommerceCheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "apps/ecommerce/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homeAddress"] = GenericObject(checkoutHomeAddress)
        context["officeAddress"] = GenericObject(checkoutOfficeAddress)
        context["standardDelivery"] = GenericObject(checkoutStandardDeliveryDict)
        context["fastDelivery"] = GenericObject(checkoutFastDeliveryDict)
        context["order"] = GenericObject(checkoutOrderDict)
        context["order"]["products"] = list_of_dict_to_list_to_obj(checkoutOrderDict["products"])
        return context
apps_ecommerce_checkout_view = EcommerceCheckoutView.as_view()


apps_ecommerce_checkout_view = AppsView.as_view(template_name="apps/ecommerce/checkout.html")
apps_ecommerce_product_edit_view = AppsView.as_view(template_name="apps/ecommerce/product-edit.html")




# email
apps_email_inbox_view = AppsView.as_view(template_name="apps/email/inbox.html")
apps_email_read_view = AppsView.as_view(template_name="apps/email/read.html")
apps_email_compose_view = AppsView.as_view(template_name="apps/email/compose.html")
apps_email_templates_view = AppsView.as_view(template_name="apps/email/templates.html")
apps_email_templates_action_view = AppsView.as_view(template_name="apps/email/templates-action.html")
apps_email_templates_alert_view = AppsView.as_view(template_name="apps/email/templates-alert.html")
apps_email_templates_billing_view = AppsView.as_view(template_name="apps/email/templates-billing.html")

apps_email_send_view = AppsView.as_view(template_name="apps/email/send_mail.html")
apps_email_recieve_view = AppsView.as_view(template_name="apps/email/recieve_mail.html")
apps_email_recieve_box_view = AppsView.as_view(template_name="apps/email/recieve_mail_end.html")





# file manager
apps_file_manager_view = AppsView.as_view(template_name="apps/manager/file-manager.html")

# projects
apps_project_create_view = AppsView.as_view(template_name="apps/project/create.html")
apps_project_detail_view = AppsView.as_view(template_name="apps/project/detail.html")
apps_project_list_view = AppsView.as_view(template_name="apps/project/list.html")

# social
apps_social_feed_view = AppsView.as_view(template_name="apps/social/feed.html")

# tasks
apps_task_details_view = AppsView.as_view(template_name="apps/task/details.html")
apps_task_kanban_board_view = AppsView.as_view(template_name="apps/task/kanban-board.html")
apps_task_list_view = AppsView.as_view(template_name="apps/task/list.html")


# tickets
apps_tickets_list_view = AppsView.as_view(template_name="apps/tickets/list.html")
apps_tickets_detail_view = AppsView.as_view(template_name="apps/tickets/detail.html")



