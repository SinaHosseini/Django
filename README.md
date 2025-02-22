# Django Polls Application

This project is a simple Django application that implements a basic polls system, built as part of the Django tutorial.

## Getting Started

Follow the instructions below to set up and run the project locally.

### Installation Steps

1. **Install Django**
   ```bash
   pip install django
   ```

2. **Create a Django Project**
   ```bash
   django-admin startproject mysite djangotutorial
   cd ./djangotutorial
   ```

3. **Create the Polls App**
   ```bash
   python manage.py startapp polls
   ```

4. **Run the Development Server**
   Start the Django development server and verify the project:
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000` to see your project running!

## Guide
1. #### Forgot password
If you forgot your admin password, you can change it with following commands.

1. Active django terminal:
```
python manage.py shell
```

2. Run this commands:
```
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username="john")
>>> u.set_password("new password")
>>> u.save()
```

2. #### Persian date
- Check this documentation

[Django jalali date](https://pypi.org/project/django-jalali-date/)
### Useful Links

- [Django Documentation](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)


Happy coding! 🚀
