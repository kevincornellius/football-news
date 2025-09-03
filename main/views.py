from django.shortcuts import render


def show_main(request):
    context = {
        "npm": "2406428781",
        "name": "Kevin Cornellius Widjaja",
        "class": "PBP E",
    }

    return render(request, "main.html", context)
