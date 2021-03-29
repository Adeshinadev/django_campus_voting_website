from django.shortcuts import render,redirect
from .models import Voters,Candidate,Votes,Election,Position
from django.contrib import messages
from django.db.models import F
from datetime import *
from django.http import HttpResponseRedirect
# Create your views here.



def voter_search(request):
    if request.method=='POST':
        voter_id_user=request.POST['voter_id_user']
        voter_id_insts=Voters.objects.filter( voters_id=voter_id_user)
        # for voter_id_inst in voter_id_insts:
        #     associated_elect_manager=voter_id_inst.user
        #     candidate=Candidate.objects.filter(user__username=associated_elect_manager)
        #     return render(request,'voting_page.html',{'candidate':candidate})
        if voter_id_insts:
            for voter_id_inst in voter_id_insts:
                election_variable= voter_id_inst.voters_election
                election_objs=Election.objects.filter(election_title=election_variable)
                for election_obj in election_objs:
                    pass
                print(election_obj.election_start_time,datetime.today())
                today_date=datetime.now(timezone.utc)
                print(today_date)
                # if election_obj.election_start_time<election_obj.election_start_time:
                #     messages.info(request, "invalid election date configuration")
                #     return render(request, 'index.html')
                if today_date<election_obj.election_start_time:
                    messages.info(request, "Election hasn't started,you can't vote now")
                    return redirect('/')
                elif election_obj.election_end_time==today_date or election_obj.election_end_time<today_date:
                    messages.info(request, "Election has Ended,you can't vote anymore")
                    return redirect('/')
                else:
                    positions=Position.objects.all()
                    candidate = Candidate.objects.filter(candidate_election=election_variable)
                    messages.info(request,voter_id_user)
                    return render(request, 'position.html', {'candidate': candidate,'voter_id_user':voter_id_user,'positions':positions})
        else:
            return render(request,'error.html')
    else:
        print('not working')
        return render(request, 'index.html')

def Candidate_display(request):
    if request.method=='POST':
        voter_id_user=request.POST['voter_id_user']
        position=request.POST['position']

        voter_id_insts=Voters.objects.filter( voters_id=voter_id_user)

        if voter_id_insts:
            for voter_id_inst in voter_id_insts:
                election_variable = voter_id_inst.voters_election
                election_objs = Election.objects.filter(election_title=election_variable)
                for election_obj in election_objs:
                    pass
                print(election_obj.election_start_time, datetime.today())
                today_date = datetime.now(timezone.utc)
                print(today_date)
                # if election_obj.election_start_time<election_obj.election_start_time:
                #     messages.info(request, "invalid election date configuration")
                #     return render(request, 'index.html')
                if today_date < election_obj.election_start_time:
                    messages.info(request, "Election hasn't started,you can't vote now")
                    return redirect('/')
                elif election_obj.election_end_time == today_date or election_obj.election_end_time < today_date:
                    messages.info(request, "Election has Ended,you can't vote anymore")
                    return redirect('/')
                else:
                    positions = Position.objects.filter(position=position)
                    for position in positions:
                        pass
                    print(positions,'positions')
                    candidate = Candidate.objects.filter(candidate_election=election_variable,candidate_position=position)

                    messages.info(request, voter_id_user)
                    return render(request, 'voting_page.html',
                                  {'candidate': candidate, 'voter_id_user': voter_id_user, 'positions': positions})
        else:
            return render(request, 'error.html')
    else:
        print('not working')
        return render(request, 'index.html')


def vote(request):
    if request.method=='POST':
        voters_id=request.POST['voters_id']
        vote_candidate_code=request.POST['vote_candidate_code']
        vote_position=request.POST['vote_position']
        print(voters_id,vote_candidate_code)
        vote_candidate=Candidate.objects.filter(candidate_code=vote_candidate_code)
        print(vote_candidate)
        for o in vote_candidate:
            voted=Votes.objects.filter(voters_id=voters_id,vote_candidate_code=vote_candidate_code,vote_candidate=o,vote_position=vote_position)
            voteds=Votes.objects.filter(vote_ids=voters_id,vote_position=vote_position)
            print(voteds,'voteds')
            if voteds:
                voter_id_insts = Voters.objects.filter(voters_id=voters_id)
                # for voter_id_inst in voter_id_insts:
                #     associated_elect_manager=voter_id_inst.user
                #     candidate=Candidate.objects.filter(user__username=associated_elect_manager)
                #     return render(request,'voting_page.html',{'candidate':candidate})
                if voter_id_insts:
                    for voter_id_inst in voter_id_insts:
                        election_variable = voter_id_inst.voters_election
                        election_objs = Election.objects.filter(election_title=election_variable)
                        for election_obj in election_objs:
                            pass
                        print(election_obj.election_start_time, datetime.today())
                        today_date = datetime.now(timezone.utc)
                        print(today_date)
                        # if election_obj.election_start_time<election_obj.election_start_time:
                        #     messages.info(request, "invalid election date configuration")
                        #     return render(request, 'index.html')
                        if today_date < election_obj.election_start_time:
                            messages.info(request, "Election hasn't started,you can't vote now")
                            return redirect('/')
                        elif election_obj.election_end_time == today_date or election_obj.election_end_time < today_date:
                            messages.info(request, "Election has Ended,you can't vote anymore")
                            return redirect('/')
                        else:
                            positions = Position.objects.all()
                            candidate = Candidate.objects.filter(candidate_election=election_variable)
                            messages.info(request, f'vote not recorded,you have voted for {vote_position} category already')

                            return render(request, 'position.html',
                                          {'candidate': candidate, 'voter_id_user': voters_id,
                                           'positions': positions})















            else:
                print(voters_id)
                vt = Voters.objects.filter(voters_id=voters_id)

                for vote_candidat in vote_candidate:
                    if vt:
                        j=Votes(vote_ids=voters_id,vote_candidate_code=vote_candidate_code,vote_candidate=vote_candidat,vote_position=vote_position)
                        vote_candidateh= Candidate.objects.filter(candidate_code=vote_candidate_code).update(candidate_vote=F('candidate_vote') + 1)
                        print(vote_candidateh)
                        j.save()
                        voter_id_insts = Voters.objects.filter(voters_id=voters_id)
                        # for voter_id_inst in voter_id_insts:
                        #     associated_elect_manager=voter_id_inst.user
                        #     candidate=Candidate.objects.filter(user__username=associated_elect_manager)
                        #     return render(request,'voting_page.html',{'candidate':candidate})
                        if voter_id_insts:
                            for voter_id_inst in voter_id_insts:
                                election_variable = voter_id_inst.voters_election
                                election_objs = Election.objects.filter(election_title=election_variable)
                                for election_obj in election_objs:
                                    pass
                                print(election_obj.election_start_time, datetime.today())
                                today_date = datetime.now(timezone.utc)
                                print(today_date)
                                # if election_obj.election_start_time<election_obj.election_start_time:
                                #     messages.info(request, "invalid election date configuration")
                                #     return render(request, 'index.html')
                                if today_date < election_obj.election_start_time:
                                    messages.info(request, "Election hasn't started,you can't vote now")
                                    return redirect('/')
                                elif election_obj.election_end_time == today_date or election_obj.election_end_time < today_date:
                                    messages.info(request, "Election has Ended,you can't vote anymore")
                                    return redirect('/')
                                else:
                                    positions = Position.objects.all()
                                    candidate = Candidate.objects.filter(candidate_election=election_variable)
                                    messages.info(request, f'vote for {vote_position} category has been recorded')

                                    return render(request, 'position.html',
                                                  {'candidate': candidate, 'voter_id_user': voters_id,
                                                   'positions': positions})
                        else:
                            return render(request, 'error.html')
                    else:
                        return render(request,'index.html')

    else:
        return render(request,'index.html')

def voters_eligibility(request):
    if request.method == 'POST':
        matric_no=request.POST['matric_no']
        election_title=request.POST['election_title']
        election_object_search=Election.objects.filter(election_title=election_title)
        for election_object in election_object_search:
            search_voter=Voters.objects.filter(voting_id=matric_no,voters_election=election_object)
        if search_voter:
            messages.info(request,'YOU ARE AN ELIGIBLE VOTER')
            return redirect('/')
        else:
            messages.info(request, 'YOU ARE NOT AN ELIGIBLE VOTER')
            return redirect('/')

    else:
        return render(request, 'index.html')








