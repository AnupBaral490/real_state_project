# 🎨 Frontend Setup Guide

This guide will help you set up and run the modern frontend for the Real Estate Management System.

## 📋 What's Included

The frontend includes:
- **Responsive Design** - Mobile-first Bootstrap 5 frontend
- **Professional UI** - Modern cards, gradients, and animations
- **User Authentication** - Login/Register pages with role selection
- **Property Listing** - Advanced search and filtering
- **Property Details** - Full property information with image gallery
- **Booking System** - Schedule property visits
- **User Profiles** - Dashboard for different user roles
- **Agent Listings** - View all agents and their properties
- **Admin Integration** - Jazzmin-enhanced admin panel

## 🚀 Quick Start

### 1. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 2. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. **Create Superuser** (if not already done)

```bash
python manage.py createsuperuser
```

### 4. **Collect Static Files**

```bash
python manage.py collectstatic --noinput
```

### 5. **Run Development Server**

```bash
python manage.py runserver
```

The application will be available at: **http://localhost:8000**

## 📍 Key URLs

### Public Pages
- **Home** - `/` - Landing page with featured properties
- **Properties** - `/properties/` - Search and browse all properties
- **Property Detail** - `/properties/<id>/` - View property details
- **Agents** - `/agents/all/` - View all agents
- **Agent Detail** - `/agents/<id>/` - View agent's properties

### Authentication
- **Register** - `/users/register/` - Create new account
- **Login** - `/users/login/` - Sign in to account
- **Logout** - `/users/logout/` - Sign out
- **Profile** - `/users/profile/` - User dashboard

### User Features
- **My Bookings** - `/bookings/my-bookings/` - View your property visit bookings
- **Booking Detail** - `/bookings/booking/<id>/` - View booking details

### Agent Features
- **Agent Bookings** - `/bookings/agent-bookings/` - View bookings for your properties
- **Agent Inquiries** - `/bookings/agent-inquiries/` - View inquiries about your properties

### Admin
- **Admin Panel** - `/admin/` - Django admin interface with Jazzmin enhancement

## 🎯 Features Overview

### Home Page
- Hero section with search functionality
- Statistics dashboard (total properties, agents)
- Featured properties carousel
- Call-to-action section

### Property Listing
- **Advanced Filters:**
  - Search by keyword
  - Price range
  - Property type
  - Bedrooms
  - Status (Sale/Rent/Sold)
  - Location
- Sorting options
- Pagination
- Responsive grid layout

### Property Detail Page
- Full property description
- Image gallery with thumbnails
- Agent information and contact
- Booking request form
- Inquiry form
- Property specifications (beds, baths, area)

### User Authentication
- Role-based registration (Admin/Agent/Buyer)
- Secure login/logout
- Password validation
- Form validation

### User Profiles
- **Buyer Dashboard:**
  - View my bookings
  - Quick links to browse properties
- **Agent Dashboard:**
  - View my properties
  - View booking requests
  - View inquiries

### Booking System
- Schedule property visit
- Request approval from agent
- View booking status
- Cancel bookings

### Inquiry System
- Send messages to agents
- Track inquiry status

## 🎨 Customization

### Change Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #667eea;      /* Change primary blue */
    --secondary-color: #764ba2;    /* Change secondary purple */
}
```

### Change Theme
Modify Bootstrap variables or replace the CSS framework in `templates/base/base.html`

### Add Logo
Update the navbar brand in `templates/base/navbar.html`:
```html
<a class="navbar-brand" href="...">
    <img src="/path/to/logo.png" alt="Logo">
    Logo Text
</a>
```

## 📱 Responsive Breakpoints

- **Mobile** - < 576px
- **Tablet** - 576px - 768px
- **Desktop** - 768px - 992px
- **LG Desktop** - 992px - 1200px
- **XL Desktop** - > 1200px

## 🔧 Template Structure

```
templates/
├── base/
│   ├── base.html          # Main template wrapper
│   ├── navbar.html        # Navigation bar
│   └── footer.html        # Footer
├── properties/
│   ├── home.html          # Homepage
│   ├── property_list.html # Property listing page
│   ├── property_detail.html # Property detail page
│   └── agent_properties.html
├── users/
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   └── profile.html       # User profile
├── agents/
│   ├── agents_list.html   # All agents
│   └── agent_detail.html  # Agent details
└── bookings/
    └── my_bookings.html   # User bookings
```

## 🎯 Static Files

```
static/
├── css/
│   └── style.css          # Main stylesheet
│       - 600+ lines of custom CSS
│       - Responsive design
│       - Animations & transitions
│       - Utility classes
└── js/
    └── main.js            # Main JavaScript
        - Bootstrap initialization
        - Form validation
        - Image preview
        - Utility functions
```

### CSS Features
- Gradient backgrounds
- Card hover animations
- Responsive grid
- Custom scrollbar
- Smooth transitions
- Mobile-optimized

### JavaScript Features
- Bootstrap tooltip/modal initialization
- Form validation
- Auto-dismiss alerts
- Utility functions (formatting dates, currency)
- Lazy loading images
- Smooth scrolling

## 🍎 Bootstrap Components Used

- Navbar with dropdown menus
- Cards and grid system
- Forms and inputs
- Buttons and badges
- Alerts and modals
- Pagination
- Dropdown menus
- Progress bars (optional)

## 🔒 Security Features

- CSRF protection on all forms
- Secure password validation
- User authentication required for certain pages
- Permission checks for booking/inquiry operations
- SQL injection prevention via ORM

## 📊 Admin Customization

The admin interface uses Django Jazzmin for a modern look:
- Custom navigation panels
- Search functionality
- Inline editing
- Quick filters
- Customizable dashboard

Access at `/admin/` after creating a superuser account.

## 🚢 Production Deployment

### Before Deployment

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for secrets:
   ```python
   from decouple import config
   SECRET_KEY = config('SECRET_KEY')
   ```
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
5. Configure database (PostgreSQL recommended)
6. Use Gunicorn or uWSGI as application server

### Example Gunicorn Command

```bash
gunicorn config.wsgi:application --workers 4 --bind 0.0.0.0:8000
```

## 🐛 Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Images Not Displaying
- Check `MEDIA_ROOT` and `MEDIA_URL` in settings
- Ensure directory exists and is writable

### Form Submission Not Working
- Verify CSRF token in template
- Check form method is POST
- Review Django logs for errors

### Templates Not Found
- Verify `templates/` directory exists
- Check `TEMPLATES['DIRS']` in settings.py
- Restart development server

## 📚 Resources

- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Jazzmin Admin](https://github.com/farridav/django-jazzmin)

## 💡 Next Steps

1. **Add Email Notifications** - When bookings are approved/rejected
2. **Payment Integration** - For property rentals/sales
3. **Image Optimization** - Use django-imagekit for thumbnails
4. **API Development** - Build REST API with Django REST Framework
5. **Mobile App** - Use API to build iOS/Android apps
6. **Search Enhancement** - Add Elasticsearch integration
7. **Map Integration** - Add Google Maps or Leaflet
8. **Social Login** - Add OAuth providers (Google, Facebook)

## 📞 Support

For issues or questions:
1. Check Django logs: `python manage.py runserver`
2. Review browser console for JavaScript errors
3. Check database migrations: `python manage.py showmigrations`
4. Verify template paths and static file locations

---

**Happy Building! 🎉**
