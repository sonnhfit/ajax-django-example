from django.db import models


FRESHMAN = 'FR'
SOPHOMORE = 'SO'
JUNIOR = 'JR'
SENIOR = 'SR'
GRADUATE = 'GR'
YEAR_IN_SCHOOL_CHOICES = [
    (FRESHMAN, 'Freshman'),
    (SOPHOMORE, 'Sophomore'),
    (JUNIOR, 'Junior'),
    (SENIOR, 'Senior'),
    (GRADUATE, 'Graduate'),
]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, default='friendly', max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
