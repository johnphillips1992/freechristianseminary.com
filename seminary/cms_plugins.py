from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from myproject.seminary.models import SectionPlugin, Section
from django.utils.translation import ugettext as _

class CMSSectionPlugin(CMSPluginBase):
    model = SectionPlugin
    name = _('Section List')
    render_template = 'seminary/cms/plugins/section.html'

    def render(self, context, instance, placeholder):
        if instance.sections is None:
            sections = 6
        context.update({
            'sections': Section.objects.all()[:instance.sections]
        })
        return context

plugin_pool.register_plugin(CMSSectionPlugin)
