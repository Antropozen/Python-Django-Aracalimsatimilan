from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea, Select


class Setting(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    keywords = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=200)
    phone= models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True,max_length=200)
    smtpemail = models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=5)
    smtpport = models.CharField(blank=True,max_length=200)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutus = RichTextUploadingField(blank=True,)
    contact = RichTextUploadingField(blank=True,)
    references = RichTextUploadingField(blank=True,)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True, max_length=250)
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name':TextInput(attrs={'class':'form-control','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message','rows':'8'}),
        }



class FAQ(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=150)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question