
from django.contrib import admin
from .models import Regulator, IndustrySector, RegulationType, Technology, Regulation
admin.site.site_header = "Chin Project Administration"
admin.site.site_title = "Chin Project Admin Portal"
admin.site.index_title = "Welcome to Chin Project Administration"
class RegulatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'jurisdiction', 'contact_information', 'regulatory_scope', 'legal_documents')
    list_filter = ('jurisdiction',)
    search_fields = ('name', 'jurisdiction')
    fieldsets = (
        (None, {
            'fields': ('name', 'jurisdiction', 'contact_information', 'regulatory_scope', 'legal_documents')
        }),
    )

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'jurisdiction':
            kwargs['choices'] = Regulator.JURISDICTION_CHOICES
        return super().formfield_for_choice_field(db_field, request, **kwargs)

class IndustrySectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class RegulationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class RegulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'regulator', 'industry_sector', 'regulation_type', 'technology', 'compliance_guidelines')
    list_filter = ('regulator', 'industry_sector', 'regulation_type', 'technology')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'regulator', 'industry_sector', 'regulation_type', 'technology', 'compliance_guidelines')
        }),
    )

admin.site.register(Regulator, RegulatorAdmin)
admin.site.register(IndustrySector, IndustrySectorAdmin)
admin.site.register(RegulationType, RegulationTypeAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Regulation, RegulationAdmin)

