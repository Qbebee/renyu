from django import forms
from .models import Fanduier,FDReporter,GondanNote

class FanduierForm(forms.ModelForm):
    class Meta:
        model = Fanduier
        fields = ('id','fadriq','name','bans','sanj','bans2','sanj2')
        labels = {
            'fadriq':'请输入翻堆日期',
            'name':'请输入姓名',
            'bans':'请输入板数',
            'sanj':'请输入散件数',
            'bans2':'整合后整板数',
            'sanj2':'整合后散件数'
        }
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }
        """
        name_list = (
            ('刘健全','刘健全'),
            ('刘振良','刘振良'),
            ('刘国亮','刘国亮'),
            ('瞿明','瞿明'),
            ('盛文明','盛文明'),
            ('黄伟林','黄伟林'),
            ('周振兴','周振兴'),
            ('游国平','游国平'),      
        )
        widgets = (
            'name': forms.Select(choices=name_list),
        )
        """
class FDReporterForm(forms.ModelForm):
    class Meta:
        model = FDReporter
        fields = ('id','name','yearday','days','sbans','ssanj',"sbans2",'ssanj2','totals')
        labels = {
            'id':'ID',
            'name':'姓名',
            'yearday':'所在年月',
            'days':'出勤天数',
            'sbans':'初次汇总板数',
            'ssanj':'初次汇总散件数',
            'sbans2':'整合汇总板数',
            'ssanj2':'整合后散件数',
            'totals':'总件数'
        }
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }
    #totals = (int)(model.data['sbans2'])*198 + (int)(model.data['ssanj2'])


class GondanNoteForm(forms.ModelForm):
    class Meta:
        model = GondanNote
        fields = ('id','name','cgdate','cgplace','grdescription','begtime','endtime','remark')
        labels = {
            'id':'ID',
            'name':'姓名',
            'cgdate':'出工日期',
            'cgplace':'出工地点',
            'grdescription':'工日描述',
            'begtime':'开工时间',
            'endtime':'收工时间',
            'remark':'补充说明'
        }
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=11, label='请您输入手机号',
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'layui-input', 'placeholder': '请您输入手机号',
                                          'lay-verify': 'required|phone', 'id': 'username'}), )
    password = forms.CharField(max_length=20, label='请您输入密码',
                               widget=forms.widgets.PasswordInput(
                                   attrs={'class': 'layui-input', 'placeholder': '请您输入密码',
                                          'lay-verify': 'required|password', 'id': 'password'}), )

    # 自定义表单字段username的数据清洗
    def clean_username(self):
        if len(self.cleaned_data['username']) == 11:
            return self.cleaned_data['username']
        else:
            raise ValidationError('用户名为手机号码')


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': '请您输入手机号',
            'password': '请您输入密码',
        }
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }
        # 定义widgets，设置表单字段对应HTML元素控件的属性
        widgets = {
            'username': forms.widgets.TextInput(
                                   attrs={'class': 'layui-input', 'placeholder': '请您输入手机号',
                                          'lay-verify': 'required|phone', 'id': 'username'}),
            'password': forms.widgets.PasswordInput(
                                   attrs={'class': 'layui-input', 'placeholder': '请您输入密码',
                                          'lay-verify': 'required|password', 'id': 'password'})
        }

    # 自定义表单字段username的数据清洗
    def clean_username(self):
        if len(self.cleaned_data['username']) == 11:
            return self.cleaned_data['username']
        else:
            raise ValidationError('用户名为手机号码')
       