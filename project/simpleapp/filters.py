from django_filters import FilterSet
from .models import Post
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
#@    date_range = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))


#    forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))
    class Meta:
        # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {
           # поиск по названию
            'title': ['icontains'],
           # количество товаров должно быть больше или равно
        #   'rating': ['gt'],
            'rating': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],

            'daterimePost': ['exact', 'year__gt']

        }
