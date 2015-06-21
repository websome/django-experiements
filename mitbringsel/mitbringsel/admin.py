from django.contrib import admin

from .models import Mitbringsel, MitbringselType

admin.site.register(MitbringselType)

class TemporalAdminMixin(admin.ModelAdmin):
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if hasattr(instance, 'created_by') and hasattr(instance, 'modified_by'):
                if not instance.pk:
                    instance.created_by = request.user
                instance.modified_by = request.user
            instance.save()
        formset.save_m2m()
        super(TemporalAdminMixin, self).save_formset(request, form, formset, change)

@admin.register(Mitbringsel)
class MitbringselAdmin(TemporalAdminMixin):
    fields = ['text', 'type', 'comment', 'definitiv']
    pass