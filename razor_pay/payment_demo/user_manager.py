from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email_id,password=None):
        if not email_id:
            raise ValueError('The Email field must be set')
        email_id = self.normalize_email(email_id)
        user = self.model(email_id=email_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_id, password=None):
        user = self.create_user(email_id=email_id, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
