from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Election(models.Model):
    election_title=models.CharField(max_length=400)
    election_code=models.CharField(max_length=100)
    election_shows=models.IntegerField(default=0)
    election_show=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    election_start_time=models.DateTimeField(auto_now_add=True)
    election_end_time=models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.election_title)

class Voters(models.Model):
    voting_id=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    voters_election=models.ForeignKey(Election, on_delete=models.CASCADE)
    voters_id=models.CharField(max_length=100)
    voters_email=models.EmailField(max_length=200)
    def __str__(self):
        return '{}'.format(self.voting_id)

class Position(models.Model):
    position=models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.position)

class Candidate(models.Model):
    candidate_name=models.CharField(max_length=100)
    candidate_pic=models.ImageField(upload_to='pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate_election=models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate_code=models.CharField(max_length=100)
    candidate_vote=models.IntegerField(default=0,editable=False)
    candidate_position=models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.candidate_name)
class Votes(models.Model):
    vote_ids=models.CharField(max_length=100)
    vote_candidate_code=models.CharField(max_length=100)
    vote_position=models.CharField(max_length=100)
    vote_candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    voters_id = models.CharField(max_length=100)


