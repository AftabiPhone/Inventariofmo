def url(f,args=[]): return URL(r=request,f=f,args=args)
def button(text,action,args=[]):
    return SPAN('[',A(text,_href=URL(r=request,f=action,args=args)),']')
