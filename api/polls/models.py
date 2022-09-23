from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

class Menu(models.Model):
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    WEDNESDAY = 'WED'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'

    DAYS = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    ]
    name = models.CharField(max_length=60, null=False, blank=False)
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.DO_NOTHING,
        null=True
    )
    
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False, default=0)
    day = models.CharField(max_length=3, choices=DAYS, blank=False, null=False, validators=[MinLengthValidator(3)])
    dishes = models.JSONField()
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now())
    update_at = models.DateTimeField(default=now())

class Votes(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.DO_NOTHING
    )
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.DO_NOTHING
    )
    voted_at = models.DateTimeField(default=now())


