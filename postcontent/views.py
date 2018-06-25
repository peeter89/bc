from django.shortcuts import render, get_object_or_404
from .models import Author, Hashtag, Post
from datetime import datetime
from django.views import generic
from django.db.models import Count, Max, Min

# Create your views here.


def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	number_carouselp_post = 5
	num_posts = Post.objects.filter(date_publish__lte=datetime.now()).count()
	num_authors = Author.objects.all().count()
	num_hashtags = Hashtag.objects.all().count()
	carousel_post = 0
	if num_posts >= number_carouselp_post:
		carousel_post = Post.objects.all().order_by('?')[:number_carouselp_post]
		
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_posts':num_posts, 'num_authors': num_authors ,'num_hashtags':num_hashtags, 'carousel_post':carousel_post},
	)


def styleguide(request):

	return render(
		request,
		'styleguide.html',
		context={}
		)


#Author View
class AuthorListView(generic.ListView):
	model = Author
	context_object_name = 'author_list'   # your own name for the list as a template variable
	template_name = 'content/author-list.html'  # Specify your own template name/location
	paginate_by = 10


	def get_queryset(self):
		return Author.objects.all() # Get 5 books containing the title war

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get the context
		context = super(AuthorListView, self).get_context_data(**kwargs)
		context['title'] = "List of Authors"
		return context



class AuthorDetailView(generic.DetailView):
	model = Author
	

	def get_context_data(self,**kwargs):
		# Call the base implementation first to get the context
		context = super(AuthorDetailView, self).get_context_data(**kwargs)
		# Create any data and add it to the context
		return context



class HashtagDetailView(generic.DetailView):
	model = Hashtag
	template_name = 'content/hashtag_detail.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get the context
		context = super(HashtagDetailView, self).get_context_data(**kwargs)
		return context

#Post View
class PostListView(generic.ListView):
	model = Post
	context_object_name = 'post_list'   # your own name for the list as a template variable
	template_name = 'content/post-list.html'  # Specify your own template name/location
	paginate_by = 10

	def get_queryset(self):
		return Post.objects.filter(date_publish__lte=datetime.now())

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get the context
		context = super(PostListView, self).get_context_data(**kwargs)
		context['title'] = "List of Post"
		context['hashtag_list'] = Hashtag.objects.filter(post__date_publish__lte=datetime.now()).distinct().annotate(p_count=Count('post')).order_by('-p_count', 'name')
		return context

class PostDetailView(generic.DetailView):
	model = Post

	def get_queryset(self):
		return Post.objects.filter(date_publish__lte=datetime.now())