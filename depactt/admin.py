from django.contrib import admin

# Register your models here.

# from .models import Event

from .models import Messaging

from .models import Event

from .models import Comment

from .models import Addreport


from .models import Groupmessages

from .models import Preevent

from .models import Details

from .models import Groupmembers

from .models import Registration

admin.site.register(Registration)
admin.site.register(Groupmembers)
admin.site.register(Details)
admin.site.register(Preevent)
admin.site.register(Groupmessages)
admin.site.register(Addreport)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Messaging)

# admin.site.register(Event)
