from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from board.models import Post
from reply.forms import ReplyForm

@login_required(login_url='/user/login')
def create(request, bid):
    if request.method == "POST":
        replyForm = ReplyForm(request.POST)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            reply.writer = request.user
            post = Post()
            post.id = bid
            reply.post = post
            reply.save()
    return redirect('/board/read/'+str(bid))

@login_required(login_url='/user/login')
def delete(request, bid):
    if request.method == 'POST':
        replyForm = ReplyForm(request.POST)


        return
@login_required(login_url='/user/login')
def update():
    return


def delete(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/read/'+str(bid))
    post.delete()
    return redirect('/board/list')

def update(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/read/'+str(bid))

    if request.method=="GET":
        context = {'post': post}
        return render(request, "board/create.html", context)

    elif request.method=="POST":
        postForm = PostForm(request.POST ,instance=post)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/board/read/'+str(bid))
