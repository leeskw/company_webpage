from django.contrib import admin

from .models import (Author, Blog, ContactFormLog, FrequentlyAskedQuestions,
                     GeneralInfo, Service, Testimonial)


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    
    list_display = [
      'company_name',
      'location',
      'email',
      'phone',
      'open_hours',
    ]
    
    # # show to disable add permission
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # # show to disable update permission
    # def has_change_permission(self, request, obj=None):
    #     return False
    
    # # show to delete delete permission
    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # show you can set field to disable update
    readonly_fields = [
      'email',
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
      'title', 
      'description',
    ]
    
    search_fields = [
      'title', 
      'description',      
    ]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
      'user_name', 
      'user_job_title',  
      'display_rating_count'
    ]

    @admin.display(description='Rating')
    def display_rating_count(self, obj):
        return '*' * obj.rating_count

    # display_rating_count.short_description = 'Rating' 


@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
    list_display = [
      'question', 
      'answer'
    ]
    
@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = [
      'email',
      'is_success', 
      'is_error', 
      'action_time'  
    ]
    
    # show to disable add permission
    def has_add_permission(self, request, obj=None):
        return False
    
    # show to disable update permission
    def has_change_permission(self, request, obj=None):
        return False
    
    # show to delete delete permission
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
      'first_name', 
      'last_name'
    ]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
      'author', 
      'category', 
      'title',
      'blog_image', 
      'created_at'
    ]
