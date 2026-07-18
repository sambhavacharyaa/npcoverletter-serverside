from django.db import models


class CoverLetterSubmission(models.Model):
    PERSONAL = 'personal'
    BUSINESS = 'business'
    TYPE_CHOICES = [
        (PERSONAL, 'Personal'),
        (BUSINESS, 'Business'),
    ]

    submission_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=150, default='bisup')       # full_name OR company_name
    email = models.EmailField()
    domain_name = models.CharField(max_length=100)   # e.g. "bisup"
    domain_tld = models.CharField(max_length=2, default='.com.np')      # e.g. ".com.np"
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.domain_name}{self.domain_tld} — {self.name} ({self.get_submission_type_display()})"

    @property
    def full_domain(self):
        return f"{self.domain_name}{self.domain_tld}"