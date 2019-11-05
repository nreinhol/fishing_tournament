from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from blog.models import Post


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)
