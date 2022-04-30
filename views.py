
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    
    return render(request, "index.html")



def analyse(request):
    removenewline=request.POST.get("remove_newline","off")
    fullcaps= request.POST.get("full_caps","off")
    djtext=request.POST.get("text","default")
    removePunc=request.POST.get("removePunc","off")
    
    if removePunc=="on":
        punctuations= '''!@#$%^^&&*()~{}:';'":"><?/'''

        analysed=''
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        
        params= {"purpose":"Removed pucntuations","analysed_text":analysed}
        djtext=analysed
    
    if removenewline=="on":
        analysed= ""
        for char in djtext:
            if char !="\n" and char !="\r":

                analysed=analysed+char
        params= {"purpose":"changed to Upper case with newline removed","analysed_text":analysed}
        djtext=analysed
    
    if fullcaps=="on":
        analysed= ""
        for char in djtext:
            analysed=analysed+char.upper()
        params= {"purpose":"changed to Upper case","analysed_text":analysed}
        djtext=analysed

    if(removePunc!="on" and removenewline!="on" and fullcaps!="on"):
        return HttpResponse("Please select any on the operation and try again")
    return render(request,"analyze.html",params)
        
    #return HttpResponse("remove Punk")

    