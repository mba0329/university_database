from django.db import models

class ResearchGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    research_group = models.OneToOneField(
        ResearchGroup, related_name='lead_professor', on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    credits = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    format = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    professors = models.ManyToManyField(Professor, related_name='courses', through='ProfessorCourse')
    research_groups = models.ManyToManyField(ResearchGroup, related_name='courses', through='CourseResearch')

    def __str__(self):
        return self.name

class PhDStudent(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE, related_name='phd_students')
    supervisor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='phd_students')
    enrollment_date = models.DateField()
    image_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "PhD student"
        verbose_name_plural = "PhD students"

    def __str__(self):
        return f"{self.title} {self.name}"

class ProfessorCourse(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('professor', 'course')

class CourseResearch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('course', 'research_group')
        verbose_name = "Course research"
        verbose_name_plural = "Course researches"