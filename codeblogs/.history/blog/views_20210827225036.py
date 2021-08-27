from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "hike-in-mountains",
        "image": "mountain.jpg",
        "author": "Harsh",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views when hiking mountains",
        "content": '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias est
                        nihil, illum nisi fugiat nemo. Neque repudiandae harum, explicabo
                        reprehenderit, enim obcaecati corrupti facere quis labore accusamus ratione
                        accusantium alias.
                    
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias est
    nihil, illum nisi fugiat nemo. Neque repudiandae harum, explicabo
    reprehenderit, enim obcaecati corrupti facere quis labore accusamus ratione
    accusantium alias.

    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias est
    nihil, illum nisi fugiat nemo. Neque repudiandae harum, explicabo
    reprehenderit, enim obcaecati corrupti facere quis labore accusamus ratione
    accusantium alias.
        '''
    }
]


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html", )
