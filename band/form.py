__author__ = 'uiandwe'


from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields
from .models import Detail


class DetailForm(forms.ModelForm):
     detail_error={'required':(u'상세정보를 입력해주세요'),}
     detail = summer_fields.SummernoteTextFormField(error_messages=detail_error)
     class Meta:
           model = Detail
           fields = ('detail',)
           widgets= {
                'foo' : SummernoteWidget(),
                'bar' : SummernoteInplaceWidget(),
           }