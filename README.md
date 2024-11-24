
# MarAcademy

MarAcademy is an innovative online learning platform designed to provide free coding courses, career development resources, and scholarship opportunities for high school students. It empowers learners to gain programming skills, track their progress, and access certifications, all in a user-friendly environment.

## Features

- **Personalized Dashboards**: View progress, completed courses, certificates earned, and learning hours.
- **Dynamic Course Management**: Features for course creation, enrollment, and learning activities.
- **Instructor Access**: Role-based permissions for managing courses and students.
- **Interactive Charts**: Visualize progress and time spent per subject.
- **Responsive Design**: Fully optimized for mobile and desktop devices.

---

## Requirements

To set up and run this project, you will need:

- Python 3.11+
- Django 5.1.1
- PostgreSQL (preferred; SQLite for development is supported)
- Git for version control
- A virtual environment tool (e.g., `venv`)

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/maracademy.git
cd maracademy
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3.  Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database

#### For PostgreSQL:
1. Ensure that PostgreSQL is installed and running on your system.
2. Log in to your PostgreSQL database:
   ```sql
   psql -U postgres
   ```

3. Create a new database for the project
4. Update the DATABASES configuration in your project's settings.py file:
   
```python
   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maracademy',
        'USER': 'maradmin',
        'PASSWORD': 'securepassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```
### 8. python manage.py collectstatic
```bash
python manage.py collectstatic
```
### 9. Run the Development Server
```bash
python manage.py runserver
```

Visit ***http://127.0.0.1:8000/*** in your browser to view the app.







