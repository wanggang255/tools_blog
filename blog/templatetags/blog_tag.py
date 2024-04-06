from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

class CommonMarkdown:
    @staticmethod
    def _convert_markdown(value):
        md = markdown.Markdown(
            extensions=[
                'extra',
                'codehilite',
                'toc',
                'tables',
            ]
        )
        body = md.convert(value)
        toc = md.toc
        return body, toc

    @staticmethod
    def get_markdown_with_toc(value):
        body, toc = CommonMarkdown._convert_markdown(value)
        return body, toc

    @staticmethod
    def get_markdown(value):
        body, toc = CommonMarkdown._convert_markdown(value)
        return body


@register.filter()
@stringfilter
def custom_markdown(content):
    return mark_safe(CommonMarkdown.get_markdown(content))