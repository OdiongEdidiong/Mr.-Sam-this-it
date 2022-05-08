
from django.shortcuts import render
from django import forms



# Create your views here.
class form(forms.Form):
    soups=(["Nkong","Nkong"],["Afang","Afang"],["Editan","Editan"],["Ikon","Ikon"],["Atama","Atama"],["Okra","Okra"])
    choice=forms.ChoiceField(choices=soups)

def stand(request):
    votes=form()
    if request.method=="POST":
        votes=form(request.POST)
        if votes.is_valid():
            best_soup=votes.cleaned_data.get("choice")
            print(best_soup)
            msg=f"Your best soup is {best_soup}? Great Choice!!"
            return render(request,"polling_unit/vote.html",{"voteform":votes,"msg":msg,"best_soup":best_soup})
    return render(request,"polling_unit/vote.html",{"voteform":votes})