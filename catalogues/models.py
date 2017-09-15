from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

# Create your models here.
class School_photo_gallery(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.title

class School_events_calendar(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=300, default="School Events Entries")
    jan = models.CharField(max_length=250, null=True)
    feb = models.CharField(max_length=250, null=True)
    mar = models.CharField(max_length=250, null=True)
    apr = models.CharField(max_length=250, null=True)
    may = models.CharField(max_length=250, null=True)
    jun = models.CharField(max_length=250, null=True)
    jul = models.CharField(max_length=250, null=True)
    aug = models.CharField(max_length=250, null=True)
    sep = models.CharField(max_length=250, null=True)
    octo = models.CharField(max_length=250, null=True)
    nov = models.CharField(max_length=250, null=True)
    dec = models.CharField(max_length=250, null=True)
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.title

class School_bog_chairperson(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_pta_chairperson(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_principal(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_dp_academics(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_dp_admin(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_teachers(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_student_council(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_languages_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_math_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_sciences_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_humanities_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_technicals_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, null=True)
    few_words = models.TextField(null=True)
    photo = models.FileField(upload_to='uploads/', null=True)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_boarding_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_games_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_guiding_and_counseling_hod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_languages_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_math_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_sciences_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_humanities_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_technicals_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, null=True)
    few_words = models.TextField(null=True)
    photo = models.FileField(upload_to='uploads/', null=True)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_boarding_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_games_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_guiding_and_counseling_department(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_drama_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_music_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_sports_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_christian_union_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_muslim_students_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_journalism_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_debate_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_science_engineering_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_peace_club(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_history(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_mission(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
         return self.text

class School_vision(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_site_map(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_library(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_dining_hall(models.Model):
       author = models.ForeignKey('auth.User')
       text = models.TextField()
       photo = models.FileField(upload_to='uploads/')
       created_date = models.DateTimeField(
             default=timezone.now)
       published_date = models.DateTimeField(
              blank=True, null=True)

       def publish(self):
          self.published_date = timezone.now()
          self.save()

       def __str__(self):
           return self.text

class School_form_one_classes(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_form_two_classes(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_form_three_classes(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_form_four_classes(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_transport(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_physics_lab(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_chemistry_lab(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_biology_lab(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_computer_lab(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_fence(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_bakery(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_forest(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_car_park(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_generator(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_beautification(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_general_information(models.Model):
    author = models.ForeignKey('auth.User')
    school_logo = models.FileField(upload_to='uploads/')
    school_twitterlink = models.TextField(validators=[URLValidator()])
    school_facebooklink = models.TextField(validators=[URLValidator()])
    mail_icon = models.FileField(upload_to='uploads/', null=True)
    current_year = models.IntegerField(default=2007)
    school_address = models.TextField()
    school_website = models.TextField(null=True)
    school_emailaddress = models.CharField(max_length=200)
    address_icon = models.FileField(upload_to='uploads/', null=True)
    school_phone_number = models.CharField(max_length=200)
    other_phone_number = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.school_address

class School_anthem (models.Model):
    author = models.ForeignKey('auth.User')
    stanza_one = models.TextField()
    stanza_two = models.TextField()
    stanza_three = models.TextField()
    stanza_four = models.TextField()
    stanza_five = models.TextField()
    stanza_six = models.TextField()
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.stanza_one

class School_core_values (models.Model):
    author = models.ForeignKey('auth.User')
    core_value_one = models.CharField(max_length=300)
    core_value_two = models.CharField(max_length=300)
    core_value_three = models.CharField(max_length=300)
    core_value_four = models.CharField(max_length=300)
    core_value_five = models.CharField(max_length=300)
    core_value_six = models.CharField(max_length=300)
    core_value_seven = models.CharField(max_length=300)
    core_value_eight = models.CharField(max_length=300)
    core_value_nine = models.CharField(max_length=300)
    core_value_ten = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.core_value_one

class School_updates (models.Model):
    author = models.ForeignKey('auth.User')
    news_title = models.CharField(max_length=200)
    news_description = models.TextField()
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.news_title

class School_alumnae(models.Model):
    author = models.ForeignKey('auth.User')
    achievement = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_performance(models.Model):
    author = models.ForeignKey('auth.User')
    kcse_year = models.CharField(max_length=5, default='2007')
    grades_A_plain = models.IntegerField(default=00)
    grades_A_minus = models.IntegerField(default=00)
    grades_B_plus = models.IntegerField(default=00)
    grades_B_plain = models.IntegerField(default=00)
    grades_B_minus = models.IntegerField(default=00)
    grades_C_plus = models.IntegerField(default=00)
    grades_C_plain = models.IntegerField(default=00)
    grades_C_minus = models.IntegerField(default=00)
    grades_D_plus = models.IntegerField(default=00)
    grades_D_plain = models.IntegerField(default=00)
    grades_D_minus = models.IntegerField(default=00)
    grades_E = models.IntegerField(default=00)
    grades_F = models.IntegerField(default=00)
    school_mean_score = models.FloatField(default=00)
    university_qualified = models.IntegerField(default=00)
    total_students = models.IntegerField(default=00)
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
          return self.kcse_year
