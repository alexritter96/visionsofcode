from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog

# Create your views here.
def index(request):
    posts = Blog.objects.order_by('-posted')[:5]
    context = {'posts': posts}
    return render_to_response('core/index.html', context)


def view_post(request, slug):
    return render_to_response('core/post.html', {
        'posts': get_object_or_404(Blog, slug=slug)
    })

