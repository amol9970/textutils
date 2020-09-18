
# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def exerc1(request):
    return HttpResponse('''  
    <h1> This is navigation bar </h1>
    <body style="background-color:powderblue;">
    </body>
    <style >
        
         table, th, td {
            border: 1px solid black;
         }
      </style>
    
        <table>
            <tr>
                <th> Web-site Name </th>
                <th> Information </th>
            </tr>
            <tr>
                <th> <a href="https://codewithharry.com/videos/python-django-tutorials-hindi-10"> Code with Harry Lect-10 </a> </th>
                <th> Code with Harry Lect-10 </th>
            </tr>
            <tr>
                <th> <a href="https://www.google.com/">Google</a> </th>
                <th> Serach whatever is in your mind </th>
            </tr>
            <tr>
                <th> <a href="https://www.facebook.com/">facebook </a> </th>
                <th> log in here to facebook </th>
            </tr>
            <tr>
                <th> <a href="https://www.flipkart.com/">Flipkart </a> </th>
                <th> E-commerce website for shopping </th>
            </tr>
       
    ''')

def crea_homepage(request):
    return render(request,'crea_homepage.html')

def home(request):
    return HttpResponse("This is an homepage")

def index(request):
    return render(request,'index.html')


# render to access html file
def dis(request):
    params={'name':'Harry','place':'Mars'}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse('''<h1> Harry <h1>  <a href="https://www.youtube.com/watch?v=zs2Ux1jfDD0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6"> Django code with Harry </a>''')

def analyze(request):
    #return HttpResponse("punctuation removed <a href='\'>Next</a>")
    #get the text
    djtext=request.POST.get('text','default')

    removepunc=request.POST.get("removepunc",'off')
    fullcaps = request.POST.get("fullcaps", 'off')
    newlineremover=request.POST.get("newlineremover", 'off')
    extraspaceremover=request.POST.get("extraspaceremover", 'off')
    charcount=request.POST.get("charcount", 'off')

    #check which check box is on
    if removepunc=='on':
        #analyzed=djtext
        punctuations='''~!@#$%^&*()_+=-{}:"<>?[];'/.,*`'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
            # analyze the text
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'chaged to uppercase', 'analyzed_text': analyzed}
            # analyze the text
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed

    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'removed extra space', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed

    if (charcount=="on"):
        analyzed = ""
        count=0
        for char in djtext:
            if char !=" ":
                count+=1
        params = {'purpose': 'counted characters are', 'analyzed_text':count}

    elif (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("please select at least one option")

    return render(request, 'analyze.html', params)



def capfirst(request):
    return HttpResponse("capitalize first <a href='/'> Back</a>")

def newlineremove(request):
    return HttpResponse("new line removed")

def spaceremove(request):
    return HttpResponse("space removed")

def charcount(request):
    return HttpResponse("char count")
