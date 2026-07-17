from django.contrib import admin
from .models import CoverLetterSubmission


@admin.register(CoverLetterSubmission)
class CoverLetterSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_domain', 'submission_type', 'name', 'email', 'created_at')
    list_filter = ('submission_type', 'created_at')
    search_fields = ('domain_name', 'name', 'email')
    readonly_fields = ('submission_type', 'name', 'email', 'domain_name', 'domain_tld', 'created_at')

    def has_add_permission(self, request):
        return False

    def full_domain(self, obj):
        return obj.full_domain
    full_domain.short_description = 'Domain'