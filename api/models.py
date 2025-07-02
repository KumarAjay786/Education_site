from django.db import models


class AdmissionForm(models.Model):  # ✅ Make sure this class is defined
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    medium = models.CharField(max_length=50)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    msg = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"


class CareerApplication(models.Model):
    SUBJECT_CHOICES = [
        ("Mathematics", "Mathematics"),
        ("Science", "Science"),
        ("English", "English"),
        ("Social Studies", "Social Studies"),
        ("Computer Science", "Computer Science"),
        ("Other", "Other"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject_expertise = models.CharField(
        max_length=50, choices=SUBJECT_CHOICES)
    experience = models.PositiveIntegerField()
    qualification = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class TuitionAdmission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    student_class = models.CharField(max_length=10)
    curriculum = models.CharField(max_length=20)
    school_name = models.CharField(max_length=150)
    subjects = models.JSONField(default=list)  # Store list of subjects as JSON
    time_slot = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
