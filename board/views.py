from django.shortcuts import render, get_object_or_404,redirect
from .forms import BoardForm
from .models import Board
from django.utils import timezone
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext


# Create your views here.

#글쓰기 함수
def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST) #BoardForm으로부터 받은 데이터를 처리하기위한 인스턴스 생성
        if form.is_valid(): #폼 검증 메소드
            board = form.save(commit=False) #board 오브젝트를 form으로부터 가져오지만, 실제로 DB반영은 하지 않는다
            board.update_date=timezone.now()
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

