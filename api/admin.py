from django.contrib import admin
from .models import AdmissionForm, ContactMessage, CareerApplication, TuitionAdmission


@admin.register(AdmissionForm)
class AdmissionFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'mobile', 'email',
                    'course', 'district', 'state')
    search_fields = ('name', 'email', 'mobile', 'course', 'district', 'state')
    list_filter = ('course', 'district', 'state')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'created_at')
    search_fields = ('firstname', 'lastname', 'email', 'phone')
    list_filter = ('created_at',)


@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject_expertise',
                    'experience', 'qualification', 'submitted_at')
    search_fields = ('full_name', 'email', 'phone',
                     'subject_expertise', 'qualification')
    list_filter = ('subject_expertise', 'submitted_at')


@admin.register(TuitionAdmission)
class TuitionAdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'student_class',
                    'curriculum', 'school_name', 'time_slot', 'submitted_at')
    search_fields = ('name', 'phone', 'email', 'school_name')
    list_filter = ('student_class', 'curriculum', 'time_slot', 'submitted_at')

# Register your models here.
