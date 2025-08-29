from django.db import models
from django.utils import timezone

# Model to store project information for the portfolio section.
# This corresponds to the 'Projects' section in your HTML.
class Project(models.Model):
    """
    Represents a project in a portfolio.
    """
    title = models.CharField(max_length=200, help_text="The title of the project.")
    description = models.TextField(help_text="A brief description of the project.")
    tech_stack = models.CharField(max_length=200, help_text="List the technologies used (e.g., 'Django, React, PostgreSQL').")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, help_text="An image to represent the project.")
    live_demo_url = models.URLField(blank=True, null=True, help_text="Optional URL for a live demo.")
    github_repo_url = models.URLField(blank=True, null=True, help_text="Optional URL for the GitHub repository.")

    class Meta:
        # Orders projects by title alphabetically in the admin.
        ordering = ['title']

    def __str__(self):
        """Returns a string representation of the model."""
        return self.title


# Model to store blog post data.
# This corresponds to the 'Recent Blog Posts' section in your HTML.
class BlogPost(models.Model):
    """
    Represents a blog post.
    """
    title = models.CharField(max_length=200, help_text="The title of the blog post.")
    excerpt = models.TextField(help_text="A short summary or excerpt of the post.")
    publish_date = models.DateField(default=timezone.now, help_text="The date the post was published.")
    read_more_url = models.URLField(help_text="The URL to the full blog post.")

    class Meta:
        # Orders blog posts in reverse chronological order.
        ordering = ['-publish_date']

    def __str__(self):
        """Returns a string representation of the model."""
        return self.title


# Model to store skills for the skills section.
# This corresponds to the 'My Skills' section in your HTML.
class Skill(models.Model):
    """
    Represents a skill in a skills list.
    """
    name = models.CharField(max_length=50, help_text="The name of the skill (e.g., 'Python', 'Django').")
    category = models.CharField(max_length=50, help_text="The category of the skill (e.g., 'Backend', 'Frontend').")

    class Meta:
        # Orders skills by category and then name.
        ordering = ['category', 'name']

    def __str__(self):
        """Returns a string representation of the model."""
        return f"{self.name} ({self.category})"


# Model to handle messages from the contact form.
# This corresponds to the 'Contact' form in your HTML.
class ContactMessage(models.Model):
    """
    Represents a message submitted through the contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Orders messages from newest to oldest.
        ordering = ['-created_at']

    def __str__(self):
        """Returns a string representation of the model."""
        return f"Message from {self.name} on {self.created_at.strftime('%Y-%m-%d')}"
