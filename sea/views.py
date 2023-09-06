from django.shortcuts import render
import wikipedia as wk
# Create your views here.
def search(request):
    if request.method=='POST':
        e=request.POST['sear']
        print(e)
        data=wk.summary(e)

        return render(request,'sea/searc.html',{'data':data})
    return render(request,'sea/searc.html')



