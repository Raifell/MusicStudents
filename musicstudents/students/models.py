from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Student(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.PositiveIntegerField('Age', validators=[MinValueValidator(15), MaxValueValidator(50)])
    course = models.CharField('Course', max_length=50)
    instrument = models.CharField('Instrument', max_length=50)
    grade = models.PositiveIntegerField('Grade', validators=[MinValueValidator(1), MaxValueValidator(12)])
    payment = models.BooleanField('Payment', default=False)
    slug = models.SlugField('Slug', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.surname, self.course)

    def get_absolute_url(self):
        return reverse('students_page', kwargs={'student_slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('{}-{}-{}-{}'.format(self.name, self.surname, self.course, self.instrument))
        super(Student, self).save(force_insert, force_update, using, update_fields)
