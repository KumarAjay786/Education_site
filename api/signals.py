from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import AdmissionForm, ContactMessage, CareerApplication, TuitionAdmission

# --- AdmissionForm Signal ---


@receiver(post_save, sender=AdmissionForm)
def admission_form_post_save(sender, instance, created, **kwargs):
    if created:
        # Admin notification
        admin_html = f"""
        <p><strong>New Admission Form Submitted</strong></p>
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Name</strong></td><td>{instance.name}</td></tr>
            <tr><td><strong>Email</strong></td><td>{instance.email}</td></tr>
            <tr><td><strong>Mobile</strong></td><td>{instance.mobile}</td></tr>
            <tr><td><strong>Course</strong></td><td>{instance.course}</td></tr>
            <tr><td><strong>Message</strong></td><td>{instance.message}</td></tr>
        </table>
        """
        send_mail(
            subject="New Admission Form Submitted",
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            html_message=admin_html,
            fail_silently=True,
        )
        # User confirmation
        try:
            send_mail(
                subject="Thank you for your application",
                message="Thank you for submitting your admission form. We will contact you soon.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error sending user email: {e}")

# --- ContactMessage Signal ---


@receiver(post_save, sender=ContactMessage)
def contact_message_post_save(sender, instance, created, **kwargs):
    if created:
        admin_html = f"""
        <p><strong>New Contact Message Received</strong></p>
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Name</strong></td><td>{instance.firstname}</td></tr>
            <tr><td><strong>Email</strong></td><td>{instance.email}</td></tr>
            <tr><td><strong>Mobile</strong></td><td>{instance.phone}</td></tr>
            
            <tr><td><strong>Message</strong></td><td>{instance.msg}</td></tr>
        </table>
        """
        send_mail(
            subject="New Contact Message Received",
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            html_message=admin_html,
            fail_silently=True,
        )
        try:
            send_mail(
                subject="Thank you for contacting us",
                message="Thank you for reaching out. We have received your message and will respond soon.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error sending user email: {e}")

# --- CareerApplication Signal ---


@receiver(post_save, sender=CareerApplication)
def career_application_post_save(sender, instance, created, **kwargs):
    if created:
        admin_html = f"""
        <p><strong>New Career Application Received</strong></p>
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Name</strong></td><td>{instance.name}</td></tr>
            <tr><td><strong>Email</strong></td><td>{instance.email}</td></tr>
            <tr><td><strong>Mobile</strong></td><td>{instance.mobile}</td></tr>
            <tr><td><strong>Position</strong></td><td>{instance.position}</td></tr>
            <tr><td><strong>Message</strong></td><td>{instance.message}</td></tr>
        </table>
        """
        send_mail(
            subject="New Career Application Received",
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            html_message=admin_html,
            fail_silently=True,
        )
        try:
            send_mail(
                subject="Thank you for your application",
                message="Thank you for applying for a position with us. We will review your application and contact you if shortlisted.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error sending user email: {e}")

# --- TuitionAdmission Signal ---


@receiver(post_save, sender=TuitionAdmission)
def tuition_admission_post_save(sender, instance, created, **kwargs):
    if created:
        admin_html = f"""
        <p><strong>New Tuition Admission Form Submitted</strong></p>
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Name</strong></td><td>{instance.name}</td></tr>
            <tr><td><strong>Email</strong></td><td>{instance.email}</td></tr>
            <tr><td><strong>Mobile</strong></td><td>{instance.mobile}</td></tr>
            <tr><td><strong>Class</strong></td><td>{instance.student_class}</td></tr>
            <tr><td><strong>Message</strong></td><td>{instance.message}</td></tr>
        </table>
        """
        send_mail(
            subject="New Tuition Admission Form Submitted",
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            html_message=admin_html,
            fail_silently=True,
        )
        try:
            send_mail(
                subject="Thank you for your application",
                message="Thank you for submitting your tuition admission form. We will contact you soon.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error sending user email: {e}")
