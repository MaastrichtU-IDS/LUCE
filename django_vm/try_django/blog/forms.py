from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
	title 	= forms.CharField()
	slug	= forms.SlugField()
	content	= forms.CharField(widget=forms.Textarea)

# Directly combine model and form
class BlogPostModelForm(forms.ModelForm):
	class Meta:
		# Which model to use
		model = BlogPost
		# Which fields should be included
		fields = ['title', 'slug', 'content']

	# Custom form content validation
	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get('title')
		# __iexact checks for both upper & lower case
		# memo: ignore exact case
		qs = BlogPost.objects.filter(title__iexact=title)
		if qs.exists():
			raise forms.ValidationError("This title has already been used. Please try again.")
		return title