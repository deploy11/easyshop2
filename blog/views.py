from django.shortcuts import render
from .models import Blog
from django.db.models import Q
from django.views.generic import DetailView
# Create your views here.
def blogView(request):
    if 'q' in request.GET:
        q_s=request.GET.get('q')
        blog = Blog.objects.filter(Q(title__icontains=q_s))
    else:
        blog = Blog.objects.all().order_by('-id')
    return render(request,'blog.html',{'blog':blog})
class detailView(DetailView):
    model = Blog
    template_name = 'detail.html'