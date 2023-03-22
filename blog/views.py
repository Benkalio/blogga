from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views import generic 
from django.views.generic.edit import CreateView


# Create your views here.
class BlogView(generic.DetailView): 
  model = Post
  template_name = 'blog.html'

# HOMEPAGE DOES NOT REQUIRE MODEL BECAUSE IT IS NOT GETTING DATA FROM THE database
# THAT'S WHY WE USE TEMPLATE_VIEW
class AboutView(generic.TemplateView):
  template_name = 'about.html'
  
  
class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-date_created')
  template_name = 'index.html'
  

class PostCreateView(CreateView):
    template_name = 'blog/create.html'
    model = Post
    fields = ['title', 'content']
    
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)