from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project, BlogPost, Skill, ContactMessage
import json

def home_view(request):
    return render(request, 'index.html')

def projects_api_view(request):
    projects = Project.objects.all() # Fetch full objects to access .url attribute
    project_list = []
    for project in projects:
        project_data = {
            'title': project.title,
            'description': project.description,
            'tech_stack': project.tech_stack,
            'live_demo_url': project.live_demo_url,
            'github_repo_url': project.github_repo_url,
        }
        
        # Safely check if an image is present before trying to get its URL
        if project.image and hasattr(project.image, 'url'):
            project_data['image'] = request.build_absolute_uri(project.image.url)
        else:
            project_data['image'] = 'https://placehold.co/400x300/2D3748/A0AEC0?text=No+Image'

        project_list.append(project_data)
        
    return JsonResponse(project_list, safe=False)

def blog_posts_api_view(request):
    blog_posts = BlogPost.objects.all().values(
        'title', 'excerpt', 'publish_date', 'read_more_url'
    )
    for post in blog_posts:
        post['publish_date'] = post['publish_date'].strftime('%Y-%m-%d')
    return JsonResponse(list(blog_posts), safe=False)

def skills_api_view(request):
    skills = Skill.objects.all().values(
        'name', 'category'
    )
    return JsonResponse(list(skills), safe=False)

@csrf_exempt
def contact_form_api(request):
    """
    Handles POST requests from the contact form and saves messages.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not all([name, email, message]):
                return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)

            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON format.'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
