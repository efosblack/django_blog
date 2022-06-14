from django.shortcuts import render

posts = [

    {
        'author': 'eriamiatoe',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2120'
    },
        {
        'author': 'jon snow',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28, 2121'
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')



