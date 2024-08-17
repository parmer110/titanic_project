from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Blog Title")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Post Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(upload_to='post_images/', blank=True, verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
