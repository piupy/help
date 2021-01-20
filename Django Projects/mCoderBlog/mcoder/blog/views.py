
from django.shortcuts import render,redirect
from .models import Post,BlogComment
from django.contrib import messages

def home(request):
    allPosts = Post.objects.all().order_by('-views')[:3]
    params = { 'allPosts' : allPosts, 'user' : request.user }
    return render(request, "blog/home.html",params)


def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:    
            replyDict[reply.parent.sno].append(reply)
    params = { 'post' : post, 'comments' : comments, 'user' : request.user, 'replyDict' : replyDict }
    return render(request, "blog/blogpost.html",params)



def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment','')
        user = request.user
        postSno = request.POST.get('postSno','')
        post = Post.objects.filter(sno=postSno).first()
        parentSno = request.POST.get('parentSno','')
        if parentSno == '':
            postedComment = BlogComment(comment=comment,user=user,post=post)
            postedComment.save()
            messages.success(request,'Comment posted successfully')
        else:
            reply = request.POST.get('reply','')
            parent = BlogComment.objects.filter(sno=parentSno).first()
            postedComment = BlogComment(comment=reply,user=user,post=post,parent=parent)
            postedComment.save()
            messages.success(request,'Reply posted successfully')
    return redirect(f'/blog/{post.slug}')










