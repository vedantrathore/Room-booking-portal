from django.shortcuts import *
from django.views.decorators.csrf import csrf_exempt
try:
    from django.db.models.loading import get_model
except ImportError:
    from django.apps import apps
    get_model = apps.get_model
from .forms import BookForm
from .models import *

error = ""


# possible mistake taken from #1
def index(request):
    global error
    if 'user_id' in request.COOKIES:
        return HttpResponseRedirect('login')
    error = ""
    return render(request, 'bookmyroom/index.html', {'error_already_exits': False})  # possible mistake


@csrf_exempt
def login(request):
    global error
    room = Room_Booking.objects.order_by('in_time')
    if 'user_id' in request.COOKIES:
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])  # didn't understand maybe its signup
        except Exception as E:
            error = "error 1"
            print (E)
            return HttpResponseRedirect('index')
        else:
            return render(request, 'bookmyroom/dashboard.html', {'room_booking': room})  # possible mistake
    elif 'username' in request.POST and 'password' in request.POST:
        try:
            user = User.objects.get(name=request.POST['username'], password=request.POST['password'])
            if user.password == request.POST['password']:  # why again use
                response = render(request, 'bookmyroom/dashboard.html', {'room_booking': room})
                response.set_cookie('user_id', user.id)
                return response
        except Exception as E:
            error = "error 2"
            print (E)
            return HttpResponseRedirect('index')
    else:
        error = "error 3"
        return HttpResponseRedirect('index')


@csrf_exempt
def signup(request):
    room = Room_Booking.objects.order_by('in_time')
    if 'user_id' in request.COOKIES:
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])
        except Exception as E:
            print (E)
            error = "error 4"
            return HttpResponseRedirect('index')
        else:
            return render(request, 'bookmyroom/dashboard.html', {'room_booking': room})  # possible mistake
    elif 'username' in request.POST and 'password' in request.POST:
        try:
            users = User.objects.filter(name=request.POST['username'], password=request.POST['password'])
            if len(users) == 0:
                user = User(name=request.POST['username'], password=request.POST['password'],
                            email=request.POST['email'])
                user.save()
                response = render(request, 'bookmyroom/dashboard.html', {'room_booking': room})
                response.set_cookie('user_id', user.id)
                return response
            # else => call login after giving msg that you are already registered
            else:
                return render(request, 'bookmyroom/index.html', {'error_already_exist': True})
        except Exception as E:
            error = "error 5"
            print (E)
            return HttpResponseRedirect('index')
    else:
        return HttpResponseRedirect('index')


@csrf_exempt
def logout(request):
    response = HttpResponseRedirect('index')
    response.delete_cookie('user_id')
    return response


@csrf_exempt
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # old_booking=Room_Booking.objects.get()
            room_booking = form.save(commit=False)
            room_booking.user = User.objects.get(id=request.COOKIES['user_id'])
            room_booking.book_time = timezone.now()
            room_booking.room_status = True  # Implement booking clashes you jackass
            data = form.cleaned_data
            # if validate_booking(data, room_booking) == 1:
            #     pass
            # else:
            #     return render(request, 'bookmyroom/book_edit.html', {'error': 1,'username':room_booking.user.name,'in_time':room_booking.in_time,'out_time':room_booking.out_time,'form':form})
            room_booking.save()
            return redirect('my_bookings')
    else:
        form = BookForm()
    return render(request, 'bookmyroom/book_edit.html', {'form': form})


# This method is to check clashes of timings
def validate_booking(data, room_booking):
    name = data['room_name']
    in_time = data['in_time']
    out_time = data['out_time']
    # username=room_booking.user.name
    original_name = room_booking.room_name.room_name
    original_in_time = room_booking.in_time
    original_out_time = room_booking.out_time
    print "The name in form is ", name.room_name
    print "The original name is ", original_name
    print "The in time in form is  ", in_time
    print "The out time in form is  ", out_time
    print "The original in time is ", original_in_time
    print "The original out time is ", original_out_time
    if original_name != name.room_name:
        return 1
    else:
        if in_time < original_out_time and out_time > original_in_time:
            return 0
        else:
            return 1


def mail(request, pk):
    pass


def my_bookings(request):
    user = User.objects.get(id=request.COOKIES['user_id'])
    rooms = Room_Booking.objects.filter(user__name=user.name)
    return render(request, 'bookmyroom/my_bookings.html', {'rooms': rooms})


def book_detail(request, pk):
    room = get_object_or_404(Room_Booking, pk=pk)
    return render(request, 'bookmyroom/book_detail.html', {'room_booking': room})  # here there could be a problem


def book_edit(request, pk):
    room = get_object_or_404(Room_Booking, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=room)
        if form.is_valid():
            room_booking = form.save(commit=False)
            # room_booking.user = request.user
            room_booking.book_time = timezone.now()
            room_booking.save()
            return redirect('my_bookings')
    else:
        form = BookForm(instance=room)
    return render(request, 'bookmyroom/book_edit.html', {'form': form})
