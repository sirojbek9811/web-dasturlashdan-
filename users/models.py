from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


from users.managers import CustomUserManager

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Telefon raqam quyidagi formatda bo'lishi kerak: '998 [XX] [XXX XX XX]'. 12 ta belgi"
)


class UserRoles(models.TextChoices):
    ADMIN = 'ADMIN'
    EMPLOYEE = 'EMPLOYEE'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'


class User(AbstractUser):
    username = None
    phone_number = models.CharField(
            _('phone'),
            max_length=12,
            unique=True,
            help_text=_('Required. 12 characters or fewer. Digits only.'),
            validators=[phone_regex],
            error_messages={
                'unique': _("Bu telefon raqamga ega foydalanuvchi oldindan mavjud"),
            },
        )

    role = models.CharField(choices=UserRoles.choices, max_length=12, default=UserRoles.STUDENT)
    speciality = models.CharField(max_length=50, null=True, blank=True)
    show_password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="users/images/", null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True)

    # social media
    twitter = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    @property
    def password_length(self):
        return len(self.show_password)
