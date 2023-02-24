from django.contrib.auth.models import BaseUserManager
# from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self,username,email,password = None):

        if not email:
            raise ValueError('User must have a email address')

        if not username:
            raise ValueError('user must have a username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,username,email,password = None):
        user = self.create_user( 
            email = self.normalize_email(email),
            username = username,
            password=password
        )   
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
