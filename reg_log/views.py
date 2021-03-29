from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import profile
from Voting_process.models import Election,Candidate,Votes,Voters
# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return render(request,'signup.html')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return render(request, 'signup.html')
            else:
                if password1==password2:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return render(request, 'registration_form.html',{'username':username})
                else:
                    messages.info(request, 'password does not match')
                    return render(request, 'signup.html')


    else:
        return render(request,'signup.html')

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(username,)
        register_dashboard=profile.objects.filter(users__username=username)
        print(f'register_dashboard:{register_dashboard}')
        if user is not None:
            if register_dashboard:
                auth.login(request, user)
                all_elections = Election.objects.filter(user=request.user)
                return redirect('dashboard')
            else:
                return render(request, 'registration_form.html',{'username':username})


        else:
            messages.info(request,'incorrect EasyVoting ID / Email or Password')
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


def final_reg(request):

    if request.method=='POST':
        users=request.POST['users']
        user_objs=User.objects.filter(username=users)
        for user_obj in user_objs:
            users=user_obj
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            organization_name=request.POST['organization_name']
            type_of_organization=request.POST['type_of_organization']
            phone_no=request.POST['phone_no']
            final_reg_save=profile(users=users,first_name=first_name,last_name=last_name,organization_name=organization_name,
                           type_of_organization=type_of_organization,phone_no=phone_no)
            final_reg_save.save()
            return render(request,'signin.html')
    else:
        return render(request, 'registration_form.html')
def check_result(request):
    if request.method == 'POST':

        vote_ids=request.POST['vote_ids']
        voter_id_insts = Voters.objects.filter(voting_id=vote_ids)
        if voter_id_insts:
            for voter_id_inst in voter_id_insts:
                election_variable = voter_id_inst.voters_election
                cand = Candidate.objects.filter(candidate_election=election_variable)
                c=bool(election_variable.election_shows)


                return render(request,'chart.html', {'cand' : cand,'election_variable':election_variable,'c':c})
        else:
            return render(request,'index.html')
    else:
        return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')