from django.urls import path
from . import views
urlpatterns=[
    path('settings_upload',views.settings_upload,name='settings_upload'),
    path('create_voters',views.create_voters,name='create_voters'),
    path('candidate_upload',views.candidate_upload,name='candidate_upload'),
    path('create_election',views.create_election,name='create_election'),
    path('election_result_control',views.election_result_control,name='election_result_control'),
    path('resend_voting_id',views.resend_voting_id,name='resend_voting_id'),
    path('election_start_date_update',views.election_start_date_update,name='election_start_date_update'),
    path('election_end_date_update',views.election_end_date_update,name='election_end_date_update'),
    path('check_election_result',views.check_election_result,name='check_election_result')


]