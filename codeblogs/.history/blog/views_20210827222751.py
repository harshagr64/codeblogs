from django.shortcuts import render


posts = [
    {
        "slug": "hike-in-mountains",
        "image": "mountain.jp"
    }
]

def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request):
    pass
