from django.contrib import admin
from .models import Voters,Election,Candidate,Votes,Position
# Register your models here.
admin.site.register(Voters)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Votes)
admin.site.register(Position)
class CandidateAdmin(admin.ModelAdmin):
    readonly_fields=('candidate_vote',)