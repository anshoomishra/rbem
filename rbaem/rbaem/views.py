from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "landing_page.html"