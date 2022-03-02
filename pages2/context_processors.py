from .models import Home



def sections_to_base(request):
    if Home.objects.get(user=request.user):    
        home = Home.objects.get(user=request.user)    
    return {'home': home}