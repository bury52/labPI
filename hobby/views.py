from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.shortcuts import render


def home(request):
    context = {
        "hobby_name": "Oglądanie startów rakiet",
        "description": "Lubię oglądać starty rakiet. zarówno na żywo, "
                       "jak i transmisje online. Fascynuje mnie moment "
                       "odpalenia silników i wznoszenia się rakiety.",
    }
    return render(request, "hobby/home.html", context)


def about(request):
    context = {
        "about_text": "Startami rakiet interesuję się od kilku lat. "
                      "Śledzę transmisje agencji kosmicznych (NASA, SpaceX, ESA) "
                      "oraz prywatnych firm. Najbardziej lubię nocne starty, "
                      "kiedy widać smugę i blask silników na niebie.",
    }
    return render(request, "hobby/about.html", context)


def gallery(request):
    context = {
        "items": [
            "Start Falcona 9 z misją Starlink",
            "Nocny start rakiety Ariane 6",
            "Start Sojuza z załogą na pokładzie",
            "Historyczny start Saturna V (archiwum)",
        ],
    }
    return render(request, "hobby/gallery.html", context)