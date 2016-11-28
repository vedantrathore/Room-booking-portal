import poplib

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import *
from django.views.decorators.csrf import csrf_exempt

try:
    from django.db.models.loading import get_model
except ImportError:
    from django.apps import apps

    get_model = apps.get_model
from .forms import BookForm, LoginForm
from .models import *

error = ""


def index(request):
    global error
    if 'user_id' in request.COOKIES:
        return HttpResponseRedirect('login')
    error = ""
    form = LoginForm()
    return render(request, 'bookmyroom/index.html', {'error_already_exits': False, 'form': form})  # possible mistake


@csrf_exempt
def login(request):
    global error
    room = Room_Booking.objects.order_by('date', 'room_name', 'in_time')
    if 'user_id' in request.COOKIES:
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])  # didn't understand maybe its signup
        except Exception as E:
            error = "error 1"
            print (E)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'bookmyroom/dashboard.html', {'room_booking': room})  # possible mistake
    elif 'username' in request.POST and 'password' in request.POST and 'server' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        ip = request.POST['server']
        login_valid = 0
        serv = poplib.POP3_SSL(ip, 995)
        try:
            serv.user(username)
            serv.pass_(password)
            if ('+OK'):
                login_valid = 1
                print username
                print password
        except:
            raise Http404
        if login_valid:
            user = (authenticate(username=username, password=password))
            temp =str(user)
            print temp
            if temp != "None":
                response = render(request, 'bookmyroom/dashboard.html', {'room_booking': room},
                                  context_instance=RequestContext(request))
                response.set_cookie('user_id', user.id)
                return response
            else:
                user = User(username=username, password=make_password(password))
                user.email = username + 'iitg@ernet.in'
                user.save()
                response = render(request,'bookmyroom/dashboard.html',{'room_booking':room})
                response.set_cookie('user_id',user.id)
                return response
        else:
            error = "error 3"
            return HttpResponseRedirect('/')



@csrf_exempt
def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('user_id')
    return response


@csrf_exempt
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            room_booking = form.save(commit=False)
            room_booking.user = User.objects.get(id=request.COOKIES['user_id'])
            room_booking.book_time = timezone.now()
            room_booking.room_status = True
            try:
                form.validate_form()
            except Exception as E:
                return render(request, 'bookmyroom/book_edit.html', {'form': form, 'error': E})
            room_booking.save()
            return redirect('my_bookings')
    else:
        form = BookForm()
    return render(request, 'bookmyroom/book_edit.html', {'form': form})


def my_bookings(request):
    user = User.objects.get(id=request.COOKIES['user_id'])
    rooms = Room_Booking.objects.filter(user__username=user.username)
    return render(request, 'bookmyroom/my_bookings.html', {'rooms': rooms})
