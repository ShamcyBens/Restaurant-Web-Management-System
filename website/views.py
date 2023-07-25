from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm, ReservationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from googleapiclient.discovery import build
from restaurant_website.settings import YOUTUBE_API_KEY
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required    
from .models import Profile
# Create your views here.

def home(request):
    return render(request, "website/home.html")      
                

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome Back {username}!')
                return redirect('home')  # Redirect to home page after successful login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'website/login.html', {'form': form})
    
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)  # Create a profile instance for the new user
            username = form.cleaned_data.get('username') #Clean the Username field before entering data
            email = form.cleaned_data.get('email') #Clean the Username field before entering data

            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the profile page
    else:
        form = RegistrationForm()
    return render(request, 'website/register.html', {'form': form})

@login_required()
def make_reservartion(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reserv_form = form.save()
            name =  form.cleaned_data.get('name')
            phonenumber =  form.cleaned_data.get('phonenumber')
            email = form.cleaned_data.get('email') 
            from_date = form.cleaned_data.get('from_date')     
            to_date = form.cleaned_data.get('to_date')     
            
            messages.success(request, f'Reservation Made for {{name}}! with address {email}')
            return redirect('/home')
    else:
        form = ReservationForm()
    return render(request, 'website/Reservation.html', {"form": form})
                
    

def send_mail(request):
    send_mail(
    "Subject here",
    "Here is the message.",
    "from@example.com",
    ["to@example.com"],
    fail_silently=False,
)


def logout_view(request):
    logout(request)
    return redirect('/login')

def blog(request):
    return render(request, 'website/blog.html')  
   

@login_required()
def profile(request):
    # Get the profile of the currently logged-in user
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'website/profile.html', {'profile': profile})
 
@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'website/profile_update.html', {'form': form})    
   
                           
               
@login_required()
def search_videos(request):
    query = request.GET.get('query')  # Get the search query from the request

    # Create a YouTube API service object
    youtube = build('youtube', 'v3', developerKey='AIzaSyAw4EAmzaQY6aM7nRbut9Xo127n2D5saAs')

    # Make the search request to the YouTube API
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=10
    ).execute()

    # Extract video data from the API response
    video_results = []
    for search_result in search_response.get('items', []):        
        video_data = {
        'title': search_result['snippet']['title'],
        'description': search_result['snippet']['description'],
        'video_id': search_result['id'].get('videoId', '')
    }
    video_results.append(video_data)
    context = {
        'query': query,
        'video_results': video_results
    }
    print("Query", query)
    print("Result",video_results)
    return render(request, 'website/search.html', context)






