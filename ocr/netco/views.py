# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def home(request):
#     return render(request,'index.html')

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'index.html')


# def analyze(request):
#     return render(request, 'analyze.html')


def index(request):
    if request.method == 'POST':
        Upload_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(Upload_file.name,Upload_file)

    return render(request,'index.html',)
    
        

    

    # text1 = request.POST('text')
    # return render(request,'result.html',text1)


    
    


       




    # return HttpResponse("Home")


# def ex1(request):
#     sites = ['''For Entertainment youtube video''',
#              '''For Interaction Facebook''',
#              '''For Insight   Ted Talk''',
#              '''For Internship   Intenship''',
#              ]
#     return HttpResponse((sites))

# def analyze(request):
#     #Get the text
#     djtext = request.POST.get('text','default')
#     print(djtext)

    # Check checkbox values
    file = request.POST.get('file')
    file = request.POST.get('Selectfile')
    
    # removepunc = request.POST.get('removepunc', 'off')
    # fullcaps = request.POST.get('fullcaps', 'off')
    # newlineremover = request.POST.get('newlineremover', 'off')
    # extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    # if removepunc == "on":
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed = ""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char

    #     params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)

    # elif(fullcaps=="on"):
    #     analyzed = ""
    #     for char in djtext:
    #         analyzed = analyzed + char.upper()

    #     params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
    #     # Analyze the text
    #     return render(request, 'analyze.html', params)

    # elif(extraspaceremover=="on"):
    #     analyzed = ""
    #     for index, char in enumerate(djtext):
    #         if not(djtext[index] == " " and djtext[index+1]==" "):
    #             analyzed = analyzed + char

    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    #     # Analyze the text
    #     return render(request, 'analyze.html', params)

    # elif (newlineremover == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         if char != "\n" and char!="\r":
    #             analyzed = analyzed + char
    #         else:
    #             print("no")
    #     print("pre", analyzed)
    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    #     print(params)
    #     # Analyze the text
    #     return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")


