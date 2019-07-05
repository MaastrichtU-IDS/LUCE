from django import forms

from .models import BlogPost 

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)



class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'image', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        # exclude the current instance from query set to allow same title
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # pk is primary key, same as id
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title