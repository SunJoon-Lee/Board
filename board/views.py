from django.shortcuts import render, get_object_or_404,redirect
from .forms import BoardForm, UserForm
from .models import Board
from django.utils import timezone
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext


# Create your views here.

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})

#글쓰기 함수
def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST) #BoardForm으로부터 받은 데이터를 처리하기위한 인스턴스 생성
        if form.is_valid(): #폼 검증 메소드
            board = form.save(commit=False) #board 오브젝트를 form으로부터 가져오지만, 실제로 DB반영은 하지 않는다
            board.update_date=timezone.now()
            board.name = request.user.get_username()
            board.save()
            return redirect('show') #url의 name을 경로대신 입력한다.
    else:
        form = BoardForm() #forms.py의 BoardForm클래스의 인스턴스
        return render(request, 'post.html',{'form' : form})
        
def show(request):
    boards=Board.objects.order_by('-id')
    return render(request, 'show.html',{'boards':boards})

def detail(request,board_id):
    board_detail= get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board':board_detail})

def edit(request, pk):
        board = get_object_or_404(Board, pk=pk)
        if request.method == "POST":
                form = BoardForm(request.POST, instance =board)
                if form.is_valid():
                        board = form.save(commit=False)
                        board.update_date=timezone.now()
                        board.save()
                        return redirect('show')
        else:
                form = BoardForm(instance =board)
                return render(request, 'post.html',{'form' : form})

def delete(request, pk):
        board = Board.objects.get(id=pk)
        board.delete()
        return redirect('show')

def logout(request):
        return render(request, 'logout.html')

def logoutgo(request):
    django_logout(request)
    return redirect(request, 'logoutgo')        