from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
import os
from entrybox.models import formdata



# Create your views here.

def formtest(request):
    
    if request.method == "POST":
        print(request.POST)
        entry = request.POST

        ltxt = str(list(dict(entry).values())).split('src="')[1]
        print('ici ltxt ========>', ltxt)
        imgurllist = []
        '''for t in ltxt:
            s = t#.split('.')
            print('ici s =========>',s)
            if len(s) > 1:
                print(s[0])
                imgurllist.append(s[0])'''
        
        imgurllist.append(ltxt.split('">')[0])

        print('ici imgurllist ===========>',imgurllist)

        base64imagelist = []
        
        for m in imgurllist:
            import base64

            with open(''.join([os.getcwd(),m]), "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                print('ici encoded string ===========>',encoded_string)
                base64imagelist.append(str(encoded_string.decode("utf-8")))

        print(base64imagelist)
        print(len(base64imagelist))


        outputtxt = str(list((dict(entry).values()))[0][0])
        print(outputtxt)
        for i , j in enumerate(imgurllist):
             print('ici j', j)
             outputtxt = outputtxt.replace(j , ''.join(['data:image/png;base64,',str(base64imagelist[i])]   ) )


        print(outputtxt)

        fichier = open('output.txt','w')
        fichier.write(outputtxt)

        o = formdata.objects.create(formdata =outputtxt)
        o.save()
        

            
    
        
        form = SomeForm()

    else:
        form = SomeForm()


    return render(request, "testform.html", {"form": form})
