from django.shortcuts import render,redirect
from login.models import *
from blog_app.models import *
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
# Create your blog_app views here.
def wall(request):
  if 'user_id' not in request.session:
    return redirect('/')
  context = {
    'users': User.objects.all(),
    'posts': Message.objects.all(),
    'comments': Comment.objects.all()
  }
  return render(request, 'wall.html', context)

def create_message(request):
  new_post = Message.objects.create(
    message = request.POST['message'],
    author = User.objects.get(id=request.session['user_id'])
  )
  return redirect('/wall')

def create_comment(request, post_id):
  post = Message.objects.get(id = post_id)
  poster = User.objects.get(id = request.session['user_id'])
  Comment.objects.create(
    comment = request.POST['com'],
    author = poster,
    message = post

  )
  return redirect('/wall')

#remove a user if needed
def delete(request, user_id):
  to_del = User.objects.get(id=user_id)
  to_del.delete()
  return redirect('/wall')

def delete_post(request, post_id):
  to_be_deleted_post = Message.objects.get(id=post_id)
  current_user = User.objects.get(id=request.session['user_id'])
  current_post = Message.objects.get(id=post_id)
  current_time = datetime.now()
  if current_post.author.id == current_user.id:
    to_be_deleted_post.delete()
    messages.success(request, "You successfully deleted Your post")
    return redirect('/wall')
 
  return redirect('/wall')