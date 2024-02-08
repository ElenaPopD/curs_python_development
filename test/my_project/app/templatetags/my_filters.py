from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter(name="starrating")
def starrating(value):
    if value is None:
        # Returnați un mesaj sau markup-ul HTML pentru "niciun rating"
        return mark_safe('<p>Nu exista rating-uri inca</p>')
    
    return_value = ""
    for i in range(5):
        classes = "bi"
        if value > i:
            if value < i + 1:
                classes += " bi-star-half"
            else:
                classes += " bi-star-fill"
            classes += " text-warning"
        else:
            classes += " bi-star"
        return_value += f'<i class="{classes}"></i>'
    return mark_safe(return_value)