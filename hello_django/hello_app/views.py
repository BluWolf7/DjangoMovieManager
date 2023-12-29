from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def printHello(request):
    # return HttpResponse("<b>hello django</b>")
    movie_data= { 'movies':[{
        'title': 'Godfather',
        'year': '1990',
        'summary': 'story of an underworld king',
        'success': True
    },
    {
        'title': 'Inception',
        'year': '2010',
        'summary': 'Christopher nolan\'s best work',
        'success': True
    },
    {
        'title': 'Goldfish',
        'year': '1980',
        'success': False
    },
    {
        'title': 'Lion King',
        'year': '1997',
        'summary': 'story of a jungle king',
        'success': True
    },
    {
        'title': 'Avatar',
        'year': '2014',
        'summary': 'story of an alien king',
        'success': True
    },
    {
        'title': 'Drishyam',
        'year': '2013',
        'summary': 'story of a georgekutty king',
        'success': True
    },
    {
        'title': 'Leo',
        'year': '2023',
        'summary': 'story of a \'njan leo allada\' king',
        'success': True
    },{
        'title': 'BigB',
        'year': '2010',
        'summary': 'story of a \'allah bilalika\' king',
        'success': False
    }
    ,{
        'title': 'Sagar Alias Jacky',
        'year': '2010',
        'summary': 'story of a \' sagar enna mitrathe ninak aryu jacky enna shathruvine ariyilla\' king',
        'success': False
    }
    ,{
        'title': 'Memories',
        'year': '2015',
        'summary': 'story of \' wow a cyclodikal move\'',
        'success': False
    }

    ]}
    return render(request, 'hello.html',movie_data)

