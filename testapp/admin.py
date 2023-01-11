from django.contrib import admin

# Register your models here.
from testapp.models import job_detail, pic, tourism, ethnic

admin.site.register(job_detail)
admin.site.register(pic)
admin.site.register(tourism)
admin.site.register(ethnic)

"""
admin.site.site_header = '数据中心'
admin.site.site_title = 'XXX数据中心'
admin.site.index_title = u'XXXX数据中心'
"""
