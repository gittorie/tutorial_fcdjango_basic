from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm

# Create your views here.

def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, "board_detail.html", {'board':board})

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, "board_write.html", {'form':form})

def board_list(request):
    boards = Board.objects.all().order_by('-id') # -id에서 -는 역순 >>> 가장 최신 것부터 가져오겟다.
    return render(request, 'board_list.html', {'boards':boards})