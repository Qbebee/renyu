from django.db import models
from django.db.models import fields,BigAutoField
#from django.forms.fields import RegexField
from django.utils.html import format_html


# Create your models here.
class Fanduier(models.Model):
    """翻堆明细表"""
    name_list = (
        ('刘健全', '刘健全'),
        ('刘振良', '刘振良'),
        ('刘国亮', '刘国亮'),
        ('瞿明', '瞿明'),
        ('陈明友','陈明友'),
        ('盛文明', '盛文明'),
        ('黄伟林', '黄伟林'),
        ('周振兴', '周振兴'),
        ('游国平', '游国平'),
        ('聂勇', '聂勇'),
        ('龙占东', '龙占东'),
    )
    id = BigAutoField(verbose_name="流水号",primary_key=True,auto_created=True)
    fadriq = models.DateField(verbose_name = "翻堆日期", auto_now_add=False,null=False)
    #fadriq = models.CharField(verbose_name = "翻堆日期",blank=False,max_length=15,null=False)
    name = models.CharField(verbose_name = "姓名", choices=name_list, null=False, blank=False, max_length=20, help_text='必须是中文姓名')
    #,validators=RegexField(regex="r'[\u4e00-\u9fa5]+'")
    #name = ChoiceField( "姓名",null=False,max_length=20,Choices=['瞿明','盛文明','刘振良','刘国亮','黄伟林','刘健全','周振兴'])
    bans = models.IntegerField(verbose_name = "原板数",null=False,blank=False)
    sanj = models.CharField(verbose_name = "原散件数",null=True,blank=True,max_length=80,help_text='散件之间的间隔逗号必须是英文状态下的逗号')
    bans2 = models.IntegerField(verbose_name = "整合板数",null=False,blank=False)
    sanj2 = models.IntegerField(verbose_name = "整合散件数",null=True,blank=True)
    
   # sanj = models.CharField(verbose_name = "原散件数",null=True,blank=True,max_length=80)

    def __str__(self):
        return self.name
    
    def colored_name(self):
        if self.bans2>= 40:
            color_code = 'red'
        elif self.bans2>=30 and self.bans2<40:
            color_code = 'green' 
        else:
            color_code = 'blue'     
        return format_html('<span style="color:{};">{}</span>',color_code,self.bans2,)  

    colored_name.short_description = '板数色别'

    class Meta:
        verbose_name = "翻堆明细数"
        verbose_name_plural = "翻堆明细数"
       # ordering = ('-status','-fadriq')


class FDReporter(models.Model):
    """翻堆汇总表"""
    id = BigAutoField(verbose_name="流水号",primary_key=True,auto_created=True)
    name = models.CharField(verbose_name = "姓名",max_length=10)
    yearday = models.CharField(verbose_name = "所在年月",max_length=20,null=False,blank=False,editable=True)
    days = models.IntegerField(verbose_name = "出勤天数",null=False,blank=False,editable=True)
    sbans = models.IntegerField(verbose_name = "初次汇总板数",null=False,blank=False,editable=True)
    ssanj = models.IntegerField(verbose_name = "初次汇总散件数",null=False,blank=False,editable=True)
    sbans2 = models.IntegerField(verbose_name = "整合汇总板数",null=False,blank=False,editable=True)
    ssanj2 = models.IntegerField(verbose_name = "整合汇总散件数",null=False,blank=False,editable=True)

    totals = models.IntegerField(verbose_name = "总件数",editable=True)
    
  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "翻堆汇总表"
        verbose_name_plural = "翻堆汇总表"
       # ordering = ('-status','-name')
        


class GondanNote(models.Model): 
    """每日出工流水"""
    cgplacelist =(
        ('联包机全包','联包机全包'),
        ('联包机半包','联包机半包'),
        ('可乐迷你罐翻包','可乐迷你罐翻包'),
        ('芬达雪碧可乐混包','芬达雪碧可乐混包'),
        ('手工提扣一组','手工提扣一组'),
        ('手工提扣二组','手工提扣二组'),
        ('手工提扣三组','手工提扣三组'),
        ('机制提扣线', '机制提扣线'),
        ('贴二维码','贴二维码'),
        ('洗玻璃瓶外线','洗玻璃瓶外线'),
        ('洗玻璃瓶内线','洗玻璃瓶内线'),
        ('大旺翻堆区','大旺翻堆区'),
        ('大旺A3改装区','大旺A3改装区'),
        ('大旺A3抓条','大旺A3抓条'),
        ('大旺A3一楼抓包','大旺A3一楼抓包'),
        ('大旺A1一楼改装','大旺A3一楼改装'),
        ('大旺脱袋','大旺脱袋'),
        ('大旺铁罐','大旺铁罐'),
        ('其他','其他')

    )
    id = BigAutoField(verbose_name="流水号",primary_key=True,auto_created=True)
    name = models.CharField(verbose_name="姓名", max_length=10)
    cgdate = models.DateField(verbose_name="出工日期",auto_now_add=False,null=False,blank=False,editable=True)
    cgplace = models.CharField(verbose_name="出工地点",max_length=20,choices=cgplacelist,editable=True)
    grdescription = models.TextField(verbose_name="工日描述",max_length=200)
    begtime = models.TimeField(verbose_name="开工时间",)
    endtime = models.TimeField(verbose_name="收工时间")
    remark = models.CharField(verbose_name="补充说明", max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name + self.grdescription

    class Meta:
        verbose_name = "出工流水" 
        verbose_name_plural = "出工流水"  
        
class SocietyInsureCardInfo(models.Model):
    """职工社保卡信息总表"""
    id = BigAutoField(verbose_name="流水号",primary_key=True,auto_created=True)
    bank = models.CharField(verbose_name="开户银行",max_length=20)
    unit = models.CharField(verbose_name="主办机构",max_length=20)
    name = models.CharField(verbose_name="姓名",max_length=20)
    card_no = models.CharField(verbose_name="社保卡号码",max_length=20)
    during = models.CharField(verbose_name="有效期至",max_length=10)
    account_no = models.CharField(verbose_name="银行卡号",max_length=25)
    land_address = models.CharField(verbose_name="户籍地址",max_length=50)
    
    def __str__(self):
        return self.name + self.card_no
    
    class Meta:
        verbose_name = "职工社保卡信息总表"
        verbose_name_plural = "职工社保卡信息总表"
    
    
# Create your models here.
