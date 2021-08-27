from django.shortcuts import render

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render()


def post_detail(request):
    pass
