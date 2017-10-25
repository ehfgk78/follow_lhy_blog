from django.shortcuts import render
from post.models import Post


def to_post_list(request):
    return render(
        request,
        "post/post_list.html",
        {
            'posts': Post.objects.all()
        }
    )
