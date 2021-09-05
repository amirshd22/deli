from django.contrib import admin
from .models import OnlineClass, OnlineClassItems, Reviews,Subject,Category,Comments
# Register your models here.


admin.site.register(OnlineClassItems)
admin.site.register(OnlineClass)
admin.site.register(Reviews)
admin.site.register(Comments)
admin.site.register(Subject)
admin.site.register(Category)

