from django.shortcuts import render
from django.contrib.auth import get_user_model
from chats.models import ChatModel
# Create your views here.


User = get_user_model()


def index(request):
    if request.user.is_authenticated:
        users = User.objects.exclude(username=request.user.username)
        return render(request, 'chats/index.html', context={'users': users})
    return render(request, 'users/auth.html', {})

def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id is not None and user_obj.id is not None:
        if request.user.id > user_obj.id:
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'
    else:
        # Handle the case where either request.user.id or user_obj.id is None
        thread_name = None

    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'chats/main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})

# def chatPage(request, username):
#     user_obj = User.objects.get(username=username)
#     users = User.objects.exclude(username=request.user.username)

#     if request.user.id > len(user_obj.id):
#         thread_name = f'chat_{request.user.id}-{user_obj.id}'
#     else:
#         thread_name = f'chat_{user_obj.id}-{request.user.id}'
#     message_objs = ChatModel.objects.filter(thread_name=thread_name)
#     return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
