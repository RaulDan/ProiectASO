from django.shortcuts import render, redirect
from django.contrib.auth import views as authentificationView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import RegisterUser, UploadImage
from .models import ChatRoom, Message
from django.http import JsonResponse, HttpResponse
from django.views.generic import CreateView, ListView


def homePage(request):
    return render(request, 'homePage.html')


class MessageListView(ListView):
    model=Message
    msg=model.objects.filter(roomId=0)
    # model = Message.objects.filter(roomId=0)
    template_name = 'homePage.html'
    context_object_name = 'messages'
    ordering = ['-publishDate']


# def messagesChatRoom(request, room):
#     roomData = ChatRoom.objects.get(roomName=room)
#     message = Message.objects.filter(roomId=roomData.id)



def roomPage(request, room):
    print("ENTER:" + room)
    roomData = ChatRoom.objects.get(roomName=room)
    messages = Message.objects.filter(roomId=roomData.id)
    return render(request, 'room.html', {
        'room': room,
        'roomData': roomData,
        'messages':messages
    })


# Page a new Room is created or enter an existing one
def loadRoom(request):
    room = request.POST['room_name']
    print(room + " XXXXXXXXx")

    if ChatRoom.objects.filter(roomName=room).exists():
        print("EXISTS")
        return redirect('/' + room + '/?roomPage')
        # return redirect('home')
    else:
        createdRoom = ChatRoom.objects.create(roomName=room)
        createdRoom.save()
        print("CREATED")
        return redirect('/' + room + '/?roomPage')

    # return render(request,'homePage.html')


# Get a message to a chatRoom
def takeMessages(request, room):
    roomData = ChatRoom.objects.get(roomName=room)
    message = Message.objects.filter(roomId=roomData.id)
    return JsonResponse({"messages": list(message.values())})


def sendMessage(request):
    message = request.POST['message']
    roomId = request.POST['room_id']
    # newMessage=Message.objects.create(messageText=message)
    newMessage = Message.objects.create(messageText=message, roomId=roomId, author=request.user)
    newMessage.save()
    return HttpResponse("Hi, Message Sent Successfully!!")


# Page when enter the room page
def chatRoomPage(request):
    context = {
        'rooms': ChatRoom.objects.all()
    }

    return render(request, 'chatRoomPage.html', context)


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['messageText']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class CreateRoomChat(LoginRequiredMixin,CreateView):
#     model = ChatRoom
#     fields = ['roomName']


def registerPage(request):
    print("MTH:", request.method)
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            return redirect('home')
        else:
            print("bad")
    else:
        form = RegisterUser()
    return render(request, 'registerPage.html', {'form': form})


# def existingRoom(request):
#     roomName = request.POST['roomName']
#     userName = request.POST['username']
#
#     if ChatRoom.objects.filter(roomName=roomName).exists():
#         return redirect('chatRoom')
#     else:
#         createdRoom = ChatRoom.objects.create(roomName=roomName)
#         createdRoom.save()
#         return redirect('chatRoom')


def loginPage(request):
    return render(request, 'loginPage.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                print("LOgin Succes")
                login(request, user)
                return redirect('home')
    return render(request, 'login.html')


def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        print(username, " ", password2 + " " + password + " " + email)
        if username and password:
            user = User.objects.create_user(username=username, password=password, email=email)
            if user:
                print("User added")
                return redirect('login')
        # form = RegisterUser(request.POST)
        # if form.is_valid():
        #     print("VALIDDD")
        # if username and password:
        #     user = User.objects.create_user(username=username,password=password)
        #     if user:
        #         return redirect('lgn')
    return render(request, 'signup.html')

# Create your views here.
