from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensaje de {self.name} - {self.subject}"
        
    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']


class CVDocument(models.Model):
    name = models.CharField(max_length=100, default="CV Leonardo Trejos")
    cv_file = models.FileField(upload_to='cvs/') # El archivo se guardará en /media/cvs/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name        