from django import template


register = template.Library()


@register.filter()
def censor(value):

    wrong_words = ['Цукерберг', 'вареник', 'идиот', 'Достоевский', 'токсик']
    for i in wrong_words:
        if i.find(value):
            value = value.replace(i[1::], "*" * len(i))
    return f'{value}'
