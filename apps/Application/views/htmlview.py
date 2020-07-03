from django.views.generic import TemplateView


class HtmlView(TemplateView):
    template_name = 'sites/hello_world.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'HTML Title'
        # context['headline'] = 'Headline'
        # context['subheadline'] = 'Subheadline'

        return context
