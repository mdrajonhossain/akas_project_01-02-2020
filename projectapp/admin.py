from django.contrib import admin
from .models import studentformsave
from .models import stdsubjectlist
from .models import stdnotice
from .models import Stdsubjectentry
from .models import stdclassrouting
from .models import stdresult
from .models import stdaccountingsite
from .models import Logintype


from .models import teacherform




# Register your models here.
admin.site.register(studentformsave)
admin.site.register(stdsubjectlist)
admin.site.register(stdnotice)
admin.site.register(Stdsubjectentry)
admin.site.register(stdclassrouting)
admin.site.register(stdresult)
admin.site.register(stdaccountingsite)
admin.site.register(Logintype)




admin.site.register(teacherform)









# admin customization
admin.site.site_header = "Admin Login System"