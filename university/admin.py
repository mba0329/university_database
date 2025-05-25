from django.contrib import admin
from .models import ResearchGroup, Professor, Course, PhDStudent, ProfessorCourse, CourseResearch

class ProfessorInline(admin.StackedInline):
    model = Professor
    extra = 0

class PhDStudentInline(admin.TabularInline):
    model = PhDStudent
    extra = 0

class ProfessorCourseInline(admin.TabularInline):
    model = ProfessorCourse
    extra = 1

class CourseResearchInline(admin.TabularInline):
    model = CourseResearch
    extra = 1

@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_lead_professor')
    search_fields = ('name',)
    inlines = [PhDStudentInline]

    def get_lead_professor(self, obj):
        return getattr(obj.lead_professor, 'name', None)
    get_lead_professor.short_description = 'Lead Professor'

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'position', 'research_group')
    search_fields = ('name', 'title', 'position')
    list_filter = ('research_group',)
    inlines = [ProfessorCourseInline]
    readonly_fields = ('image_url',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'start_date', 'end_date', 'level')
    search_fields = ('name', 'code')
    list_filter = ('level', 'start_date', 'end_date')
    inlines = [ProfessorCourseInline, CourseResearchInline]
    readonly_fields = ('image_url',)

@admin.register(PhDStudent)
class PhDStudentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'research_group', 'supervisor', 'enrollment_date')
    search_fields = ('name', 'title', 'supervisor__name')
    list_filter = ('research_group', 'supervisor', 'enrollment_date')
    readonly_fields = ('image_url',)

@admin.register(ProfessorCourse)
class ProfessorCourseAdmin(admin.ModelAdmin):
    list_display = ('professor', 'course')
    search_fields = ('professor__name', 'course__name')
    list_filter = ('professor', 'course')

@admin.register(CourseResearch)
class CourseResearchAdmin(admin.ModelAdmin):
    list_display = ('course', 'research_group')
    search_fields = ('course__name', 'research_group__name')
    list_filter = ('course', 'research_group')