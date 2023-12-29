from django.shortcuts import render
from . models import MovieInfo, Director
from .forms import MovieForm,DirectorForm
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'base_generic.html') 

@login_required(login_url='login')
def addDirector(request):
    frm =DirectorForm()
    if request.POST:
        frm= DirectorForm(request.POST,request.FILES)
        if frm.is_valid():
            try:
                frm.save()
            except ValueError as e:
                    print(e)
    else:
        print(frm.errors)
        frm = DirectorForm()
    
    return render(request,'addDirector.html',{'frm':frm})

@login_required(login_url='login')
def listDirectors(request):
    data_set = Director.objects.all()
    return render(request,'directorList.html',{'directors':data_set})

@login_required(login_url='login')
def editDirector(request,pk):
    director_to_be_edited = Director.objects.get(pk=pk)

    if request.POST:
        form = DirectorForm(request.POST, request.FILES, instance=director_to_be_edited)
        if form.is_valid():
            form.save()
    else:
            form =DirectorForm(instance=director_to_be_edited)
    return render(request,'addDirector.html',{'frm':form}) 

@login_required(login_url='login')
def deleteDirector(request,pk):
    director_to_be_deleted = Director.objects.get(pk=pk)
    director_to_be_deleted.delete()
    data_set = Director.objects.all()
    return render(request,'directorList.html',{'directors':data_set}) 

@login_required(login_url='login')
def create(request):
    frm = MovieForm()
    if request.POST:
        frm = MovieForm(request.POST, request.FILES)  # Include request.FILES
        if frm.is_valid():
            try:
                frm.save()
            except ValueError as e:
                print(e)
        else:
            print(frm.errors)
            frm = MovieForm()

    return render(request, 'create.html', {'frm': frm})

@login_required(login_url='login')
def edit(request,pk):
        instance_to_be_edited =MovieInfo.objects.get(pk=pk)
        if request.POST:
            frm = MovieForm(request.POST,request.FILES,instance=instance_to_be_edited)
            if frm.is_valid():
                # instance_to_be_edited.save
                 frm.save()
        else:
            recent_visits= request.session.get('recent_visits',[])
            recent_visits.insert(0,pk)
            request.session['recent_visits']= recent_visits
            frm = MovieForm(instance=instance_to_be_edited)
        return render(request,'create.html',{'frm':frm})

        

        # instance_to_be_edited =MovieInfo.objects.get(pk=pk)

        # if request.POST:
        #     title = request.POST.get('title')
        #     year = request.POST.get('year')
        #     description = request.POST.get('description')
        #     instance_to_be_edited.title=title
        #     instance_to_be_edited.year=year
        #     instance_to_be_edited.description=description
        #     instance_to_be_edited.save()

        # frm = MovieForm(instance=instance_to_be_edited)
        # return render(request,'create.html',{'frm':frm})

@login_required(login_url='login')
def delete(request,pk):
    instance_to_be_deleted =MovieInfo.objects.get(pk=pk)
    instance_to_be_deleted.delete()
    data_set = MovieInfo.objects.all()
    return render(request,'list1.html',{'movies':data_set})

@login_required(login_url='login')
def list1(request):

    recent_visits= request.session.get('recent_visits',[])
    count = request.session.get('count',0)
    print(request.COOKIES)
    count= int(count)
    count = count + 1
    request.session['count']=count
    # visits= int(request.COOKIES.get('visits',0))
    # visits = visits + 1
    recent_movie_set = MovieInfo.objects.filter(pk__in=recent_visits)
    data_set = MovieInfo.objects.all()
    # data_set = MovieInfo.objects.exclude(year__gte=2010).filter(title__startswith='T').order_by('year')
    response = render(request,'list1.html',{'movies':data_set,'visits':count, 'recent_movies':recent_movie_set})
    # response.set_cookie('visits',visits)
    return response

@login_required(login_url='login')
def list(request):
    movie_data= { 'movies':[{
        'title': 'Godfather',
        'year': '1990',
        'summary': 'story of an underworld king',
        'success': True,
        'img':'godfather.jpeg'
    },
    {
        'title': 'Inception',
        'year': '2010',
        'summary': 'Christopher nolan\'s best work',
        'success': True,
        'img':'inception.webp'
    },
    {
        'title': 'Goldfish',
        'year': '1980',
        'success': False,
        'img':'goldfish.jpeg'
    },
    {
        'title': 'Lion King',
        'year': '1997',
        'summary': 'story of a jungle king',
        'success': True,
        'img':'lionking.webp'
    },
    {
        'title': 'Avatar',
        'year': '2014',
        'summary': 'story of an alien king',
        'success': True,
        'img':'avatar.jpeg'
    },
    {
        'title': 'Drishyam',
        'year': '2013',
        'summary': 'story of a georgekutty king',
        'success': True,
        'img':'drishyam.jpeg'
    },
    {
        'title': 'Leo',
        'year': '2023',
        'summary': 'story of a \'njan leo allada\' king',
        'success': True,
        'img':'leo.jpeg'
    },{
        'title': 'BigB',
        'year': '2010',
        'summary': 'story of a \'allah bilalika\' king',
        'success': False,
        'img':'bigb.jpeg'
    }
    ,{
        'title': 'Sagar Alias Jacky',
        'year': '2010',
        'summary': 'story of a \' sagar enna mitrathe ninak aryu jacky enna shathruvine ariyilla\' king',
        'success': False,
        'img':'saj.jpeg'
    }
    ,{
        'title': 'Memories',
        'year': '2015',
        'summary': 'story of \' ih ih ih +  wow a cyclodikal move\'',
        'success': False,
        'img':'memories.jpeg'
    }

    ]}
    return render(request,'list.html',movie_data)