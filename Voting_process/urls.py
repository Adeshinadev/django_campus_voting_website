from django.urls import path
from Voting_process import views

urlpatterns=[
    path('voter_search',views.voter_search, name='voter_search'),
    path('Candidate_display',views.Candidate_display, name='Candidate_display'),
    path('vote',views.vote,name='vote'),
    path('voters_eligibility',views.voters_eligibility,name='voters_eligibility'),

]