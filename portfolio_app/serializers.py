from rest_framework import serializers
from .models import Project, BlogPost, Skill, ContactMessage

# Serializer for the Project model
class ProjectSerializer(serializers.ModelSerializer):
    # This field will call the get_image_url method to handle the image URL
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        # Make sure this list matches the fields in your front-end
        fields = ['title', 'description', 'image_url', 'live_demo_url', 'github_repo_url', 'tech_stack']
    
    def get_image_url(self, obj):
        # Check if the image field has a value and has a URL
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        # Return a placeholder URL if no image is uploaded
        return 'https://placehold.co/400x300/2D3748/A0AEC0?text=No+Image'

# Serializer for the Blog Post model
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'excerpt', 'publish_date', 'read_more_url']

# Serializer for the Skill model
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'category']
        
# Serializer for the ContactMessage model
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']