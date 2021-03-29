from django.shortcuts import render,redirect
from Voting_process.models import Election,Voters,Candidate,Position
import csv, io
import secrets
from django.contrib import messages
from django.core.mail import send_mail
import datetime
from django.db.models import F

# Create your views here.
def settings_upload(request):
    user_elections=Election.objects.filter(user=request.user)
    position_all = Position.objects.all()

    return render(request,'dashboard_setting.html',{'user_elections':user_elections,'position_all':position_all})

def create_voters(request):
    prompt = {
        'order': 'Order of the csv should be voting_id,user,voters_election,voters_id,voters_email'
    }
    if request.method == 'GET':
        return render(request, 'dashboard_setting.html')
    csv_file =request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is  not a csv file')
        return render(request, 'dashboard_setting.html')
    else:

        data_set = csv_file.read().decode('UTF-8')

        io_string = io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            vote_e = column[1]

            voters_email = column[2]


            query_vote_e=Election.objects.filter(election_title=vote_e)
            vo_id=secrets.token_hex(16)
            for query_vote in query_vote_e:
                vote_e=query_vote

            for i in query_vote_e:
                i=i
            voters_id_object=Voters.objects.filter(voting_id=column[0],voters_email=column[2],voters_election=query_vote)

            if voters_id_object:
                continue
            else:
                if i.user == request.user:
                    __, created = Voters.objects.update_or_create(
                        voting_id=column[0],
                        voters_email=column[2],
                        user=request.user,
                        voters_election=query_vote,
                        voters_id=vo_id,
                    )

                    message = "your voting id for {} is {}".format(vote_e, vo_id)

                    send_mail('CampusVoting',
                              message, 'campusvoting111@gmail.com',
                              [voters_email],
                              fail_silently=True)
                    print(vo_id)
                else:
                    messages.info(request, 'you are not allowed to upload voters for this election')
                    return redirect('settings_upload')
        context = {}
        messages.info(request,'Voters Uploaded')
        return redirect('settings_upload')


def candidate_upload(request):
    if request.method=='POST':
        candidate_name=request.POST['candidate_name']
        candidate_pic = request.POST['candidate_pic']
        candidate_election = request.POST['candidate_election']
        candidate_code = request.POST['candidate_code']
        candidate_position = request.POST['candidate_position']
        user = request.user
        candidate_election=Election.objects.filter(election_title=candidate_election)
        print(candidate_position)
        position_obj=Position.objects.filter(position=candidate_position)
        print(position_obj)
        for positions in position_obj:
            print(positions)
        candidate_position_obj=Candidate.objects.filter(candidate_position=positions)
        print(candidate_position_obj)
        for cand_elect in candidate_election:
            candidate_uploadsave=Candidate(candidate_name=candidate_name,candidate_pic=candidate_pic,
                                      candidate_election=cand_elect,candidate_code=candidate_code,user=user,candidate_position=positions)
            if cand_elect.user==request.user:
                candidate_uploadsave.save()
                messages.info(request,f"Election Candidate,{candidate_name} profile has been created")
                return redirect('settings_upload')
            else:
                messages.info(request, 'you are not allowed to upload a candidate for this election')
                return redirect('settings_upload')
    else:
        return redirect('settings_upload')

def create_election(request):
    if request.method=='POST':
        election_title=request.POST['election_title']
        election_code=request.POST['election_code']
        election_title_search=Election.objects.filter(election_title=election_title)
        election_code_search=Election.objects.filter(election_code=election_code)
        if election_title_search:
            messages.info(request,'Election already exists, please enter another election name')
            return render(request, 'dashboard_setting.html')

        else:
            if election_code_search:
                messages.info(request, 'Election Code already in use, please choose another one ')
                return render(request, 'dashboard_setting.html')
            else:
                create_election_save=Election(election_title=election_title,election_code=election_code,user=request.user)
                create_election_save.save()
                messages.info(request,'Election Created')
                return redirect('settings_upload')
    else:
        return render(request,'dashboard_setting.html')

def election_result_control(request):
    election_shows=request.POST['election_shows']
    election_title=request.POST['election_title']
    election_showupdate= Election.objects.filter(election_title=election_title).update(election_shows=election_shows)
    messages.info(request,f'Change on {election_title} is now effected ')
    return redirect('settings_upload')

def resend_voting_id(request):
    voting_id=request.POST['voting_id']
    election_title=request.POST['election_title']
    election_title_queries=Election.objects.filter(election_title=election_title)
    for election_title_query in election_title_queries:
        voting_id_search=Voters.objects.filter(voting_id=voting_id,voters_election=election_title_query)
    for voting_id_search_result in voting_id_search:
        message = "your voting id for {} is {}".format(election_title, voting_id_search_result.voters_id)
        print(voting_id_search_result.voters_id)
        send_mail('CampusVoting',
                  message, 'campusvoting111@gmail.com',
                  [voting_id_search_result.voters_email],
                  fail_silently=True)
    messages.info(request,'email sent')
    return redirect('settings_upload')


def election_start_date_update(request):
    if request.method=='POST':
        election_title=request.POST['election_title']
        year=request. POST['year']
        month=request. POST['month']
        day=request. POST['day']
        hour=request. POST['hour']
        minutes=request. POST['minutes']
        election_start_time=datetime.datetime(int(year),int(month),int(day),int(hour),int(minutes))
        Electionobjquery = Election.objects.filter(election_title=election_title).update(election_start_time=election_start_time)
        messages.info(request, f' the start date for {election_title} is now {election_start_time} ')
        return redirect('settings_upload')

    redirect('settings_upload')


def election_end_date_update(request):
    if request.method=='POST':
        election_title=request.POST['election_title']
        year=request. POST['year']
        month=request. POST['month']
        day=request. POST['day']
        hour=request. POST['hour']
        minutes=request. POST['minutes']
        election_end_time=datetime.datetime(int(year),int(month),int(day),int(hour),int(minutes))
        Electionobjquery = Election.objects.filter(election_title=election_title).update(election_end_time=election_end_time)
        messages.info(request, f' the end date for {election_title} is now {election_end_time} ')
        return redirect('settings_upload')

    redirect('settings_upload')


def check_election_result(request):
    if request.method == 'POST':
        election_title = request.POST['election_title']
        position=request.POST['position']
        elections=Election.objects.filter(election_title=election_title)
        position_qry=Position.objects.filter(position=position)

        for election in elections:
            pass
        for position_q in position_qry:
            pass
        candidates=Candidate.objects.filter(candidate_election=election,candidate_position=position_q)
        return render(request,'result_admin.html',{'candidates':candidates,'election_title':election_title,'position':position})

    return render(request, 'result_admin.html')

