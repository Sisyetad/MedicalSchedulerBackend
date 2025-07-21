from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import get_user_model
from Role.Infrastructure.role_model import RoleModel
from constants.roles import ROLE_HEADOFFICE
from Admin.Infrastructure.headoffice_model import HeadofficeModel

class Command(createsuperuser.Command):
    help = 'Create a superuser with a role'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        # No additional arguments needed, as email, username, and password are handled by default

    def handle(self, *args, **options):
        UserModel = get_user_model()
        
        # Ensure ROLE_HEADOFFICE exists
        try:
            role, created = RoleModel.objects.get_or_create(role_name=ROLE_HEADOFFICE)
            if created:
                self.stdout.write(f"Created role: {ROLE_HEADOFFICE}")
        except Exception as e:
            raise CommandError(f"Error creating role: {str(e)}")

        # Get input manually
        email = self.get_input('Email')
        username = self.get_input('Username')
        password = None
        while password is None:
            password = self.get_input('Password', secret=True)
            password2 = self.get_input('Password (again)', secret=True)
            if password != password2:
                self.stderr.write("Error: Your passwords didn't match.")
                password = None
                continue
            try:
                validate_password(password)
            except DjangoValidationError as e:
                self.stderr.write("Error: " + "; ".join(e.messages))
                password = None
                continue

        # Validate inputs
        if UserModel.objects.filter(email=email).exists():
            raise CommandError(f"Error: Email '{email}' is already taken.")
        if UserModel.objects.filter(username=username).exists():
            raise CommandError(f"Error: Username '{username}' is already taken.")

        # Create superuser
        try:
            user = UserModel._default_manager.db_manager(options.get('database')).create_superuser(
                email=email,
                username=username,
                password=password,
                role=role,
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )

            HeadofficeModel.objects.create(
                email= email,
                headoffice_name= username,
                role= role,
                is_active = True,

            )
            self.stdout.write(self.style.SUCCESS(f"Superuser created successfully: {email}"))
        except Exception as e:
            raise CommandError(f"Error creating superuser: {str(e)}")

    def get_input(self, prompt, secret=False):
        """Helper method to get input safely."""
        from getpass import getpass
        if secret:
            return getpass(prompt + ': ')
        return input(prompt + ': ').strip()