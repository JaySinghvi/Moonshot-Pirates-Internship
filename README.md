# Disaster Management System

A Django-based web application for coordinating disaster response efforts, managing resources, and tracking task assignments during emergency situations.

## 🚀 Features

- **Disaster Management**: Create, track, and update disaster incidents with real-time status monitoring
- **Resource Allocation**: Manage and allocate resources efficiently across different disaster sites
- **Task Assignment**: Create and assign tasks to response teams with progress tracking
- **User Authentication**: Custom user management system with profile customization
- **Interactive Dashboard**: Visual interface with Google Maps integration for location tracking
- **Communication Hub**: Centralized platform for team coordination
- **Reporting & Analytics**: Track progress and generate reports on disaster response efforts

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/disaster-management-system.git
cd disaster-management-system
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account with email and password.

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## 📁 Project Structure

```
disaster-management-system/
│
├── app/                    # Main application directory
│   ├── migrations/         # Database migrations
│   ├── admin.py           # Admin panel configuration
│   ├── forms.py           # Django forms
│   ├── managers.py        # Custom user manager
│   ├── models.py          # Database models
│   ├── tests.py           # Unit tests
│   ├── urls.py            # URL routing
│   └── views.py           # View controllers
│
├── templates/             # HTML templates
│   ├── registration/      # Auth templates
│   ├── disaster.html      # Disaster listing
│   ├── resource.html      # Resource management
│   ├── sidebar.html       # Navigation sidebar
│   ├── map.html          # Google Maps integration
│   └── home.html         # Dashboard
│
├── static/               # Static files (CSS, JS, images)
├── wafd/                 # Project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
│
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory (optional but recommended for production):

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=your-database-url
```

### Social Authentication (Optional)

The application supports social login via Facebook, Google, and Twitter. Configure the credentials in `wafd/settings.py`:

```python
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': 'your_facebook_client_id',
            'secret': 'your_facebook_secret',
        }
    },
    # Add Google and Twitter configurations
}
```

## 💻 Usage

### Admin Panel
Access the admin panel at `http://127.0.0.1:8000/admin` using your superuser credentials.

### Main Features

1. **Disaster Management**
   - Navigate to Disaster Management from the sidebar
   - Click "Create New Disaster" to add a new incident
   - Track status (Unresolved/Resolved)
   - Add location, details, required resources, and updates

2. **Resource Management**
   - View available resources
   - Track allocation status
   - Monitor quantity and assignment history

3. **Task Assignment**
   - Create new tasks
   - Assign resources to tasks
   - Track completion status (Incomplete/Complete)

4. **User Profile**
   - Custom user profiles with profile pictures
   - Personal information management
   - Address and contact details

## 🗃️ Database Models

### CustomUser
- Email-based authentication
- Profile picture support
- Extended user fields (firstname, lastname, address)

### Disaster
- `disaster_name`: Name of the disaster incident
- `location`: Geographic location
- `status`: Current status (Unresolved/Resolved)
- `details`: Detailed description
- `resources_needed`: Required resources
- `tasks`: Associated tasks
- `updates`: Status updates
- `slug`: URL-friendly identifier

### Resources
- `resource_name`: Name of the resource
- `type`: Resource category
- `allocation_status`: Allocation status (Not Allocated/Allocated)
- `quantity`: Available quantity
- `allocation_history`: Historical allocation data
- `assignment`: Current assignment details

### Tasks
- `task_name`: Task title
- `type`: Task category
- `status`: Completion status
- `description`: Task details
- `assigned_resources`: ManyToMany relationship with Resources
- `updates`: Progress updates

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 🚀 Deployment

### Production Settings

1. Set `DEBUG = False` in `settings.py`
2. Configure a production database (PostgreSQL recommended)
3. Set up proper `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Configure static file serving (WhiteNoise is included)

### Deployment Options

- **Heroku**: Use included Procfile configuration
- **AWS/DigitalOcean**: Deploy using Gunicorn + Nginx
- **Docker**: Create Dockerfile for containerized deployment

## 📦 Dependencies

- Django 5.0.6
- django-allauth 0.63.1 (Social authentication)
- Pillow 10.3.0 (Image processing)
- Markdown 3.6 (Content formatting)
- WhiteNoise 6.6.0 (Static file serving)

See `requirements.txt` for complete list.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Moonshot Pirates Internship Program
- Django Documentation
- Bootstrap for UI components
- Google Maps API for location services

## 🎯 Future Enhancements

- [ ] Real-time notifications system
- [ ] Mobile application
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] API for third-party integrations
- [ ] Volunteer management system
- [ ] Donation tracking module
- [ ] Weather API integration
- [ ] SMS/Email alert system
