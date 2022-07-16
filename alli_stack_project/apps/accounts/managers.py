from django.contrib.auth.base_user import BaseUserManager


class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and Save a User with email and password

        """
        if not email:
            raise ValueError('Users must have an email address')
        # normalize email address, check if it is valid
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and Save a SuperUser with email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super user must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')
        user = self.create_user(email, password, **extra_fields)
        return user
