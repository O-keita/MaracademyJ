from django.contrib import admin
from .models import Course, Module, Lesson, Assignment,AssignmentRequirement, AssignmentResources

class ModuleInline(admin.TabularInline):
    model = Module

class LessonInline(admin.TabularInline):
    model = Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at', 'show_enrolled_users')
    fields = ['title', 'description', 'instructor', 'image']
    filter_horizontal = ('enrolled_users',)  # Allows many-to-many field editing in admin form
    inlines = [ModuleInline]

    def show_enrolled_users(self, obj):
        return ", ".join([user.username for user in obj.enrolled_users.all()])
    show_enrolled_users.short_description = 'Enrolled Users'



@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    fields = ['title', 'description', 'image']  # Include image in the form
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'video_url', 'video_file')
    fieldsets = (
        (None, {'fields': ('module', 'title', 'description', 'content')}),
        ('Media', {'fields': ('video_url', 'video_file', 'image')}),
    )


admin.site.register(Assignment)
admin.site.register(AssignmentRequirement)
admin.site.register(AssignmentResources)