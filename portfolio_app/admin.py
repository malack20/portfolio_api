from django.contrib import admin
from .models import Project, BlogPost, Skill, ContactMessage

# Customizes the admin view for the Project model.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Project model.
    """
    list_display = ('title', 'tech_stack', 'live_demo_url', 'github_repo_url')
    search_fields = ('title', 'tech_stack')


# Customizes the admin view for the BlogPost model.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin configuration for the BlogPost model.
    """
    list_display = ('title', 'publish_date', 'read_more_url')
    list_filter = ('publish_date',)
    search_fields = ('title',)
    date_hierarchy = 'publish_date'


# Customizes the admin view for the Skill model.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Skill model.
    """
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


# Customizes the admin view for the ContactMessage model.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ContactMessage model.
    """
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')
