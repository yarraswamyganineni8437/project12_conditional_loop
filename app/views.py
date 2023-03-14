from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':1000,'b':200,'c':25}
    return render(request,'conditional_htmlpages.html',context=d)

def loop(request):
    d={'name':'Bangaram'}
    return render(request,'loop_statements.html',context=d)

