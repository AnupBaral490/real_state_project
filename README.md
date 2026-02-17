# 🏢 Smart Real Estate Management System

A comprehensive Django-based web platform for managing real estate listings, appointments, and inquiries.

## 📋 Features

### 1. **User Authentication & Roles**
- Admin Dashboard
- Agent Management
- Buyer/Customer Accounts
- Role-based access control

### 2. **Property Listing System**
Each property includes:
- 📷 Multiple images gallery support
- 💰 Price and payment type (Sale/Rent)
- 📍 Location information
- 🏘️ Property type (House, Apartment, Land)
- 🛏️ Bedrooms & Bathrooms
- 📐 Area (sq ft)
- 👤 Agent information
- ✅ Status tracking (For Sale/Rent/Sold)

### 3. **Advanced Search & Filters**
- 💵 Price range filtering
- 📍 Location-based search
- 🏠 Property type selection
- 🛏️ Bedroom/bathroom filters
- 🏷️ Sale/Rent status filter

### 4. **Appointment Booking System**
- 📅 Schedule property visits
- ⏳ Booking status tracking (Pending/Approved/Rejected/Completed)
- 💬 Messages from users
- ✉️ Inquiry form submission
- 📌 Mark inquiries as read/unread

### 5. **Professional Admin Dashboard**
- 🎨 Django Jazzmin integration for modern UI
- 📊 Quick statistics
- 🔍 Advanced search and filters
- 🎯 Custom admin actions
- 📱 Fully responsive

## 🚀 Quick Start

### Installation

1. **Clone and navigate to project:**
```bash
cd config
```

2. **Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Run development server:**
```bash
python manage.py runserver
```

7. **Access admin panel:**
Open `http://localhost:8000/admin/` in your browser

## 📁 Project Structure

```
config/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── media/                    # User uploaded files
├── users/                    # User authentication app
│   ├── models.py            # Custom User model with roles
│   ├── admin.py             # User admin configuration
│   └── ...
├── agents/                   # Real estate agents app
│   ├── models.py            # Agent profile model
│   ├── admin.py             # Agent admin configuration
│   └── ...
├── properties/              # Property listings app
│   ├── models.py            # Property & PropertyImage models
│   ├── admin.py             # Property admin configuration
│   └── ...
├── bookings/                # Bookings & inquiries app
│   ├── models.py            # Booking & Inquiry models
│   ├── admin.py             # Booking admin configuration
│   └── ...
└── config/                  # Project settings
    ├── settings.py          # Django configuration
    ├── urls.py              # URL routing
    ├── wsgi.py              # Production server config
    └── asgi.py              # Async server config

```

## 🏗️ Database Models

### User (Custom)
- `username`, `email`, `password`
- `first_name`, `last_name`
- `role` - Admin, Agent, or Buyer
- Django auth fields

### Agent
- `user` - OneToOne relationship with User
- `phone` - Contact number
- `profile_image` - Agent photo
- `bio` - Biography
- `rating` - Agent rating (0-5)
- `created_at` - Registration date

### Property
- `agent` - ForeignKey to Agent
- `title`, `description`
- `price`, `location`
- `property_type` - House/Apartment/Land
- `bedrooms`, `bathrooms`
- `area` - Size in sq ft
- `status` - For Sale/Rent/Sold
- `featured_image`, `created_at`, `updated_at`

### PropertyImage
- `property` - ForeignKey to Property
- `image` - Image file
- `caption`
- `uploaded_at`

### Booking
- `property` - ForeignKey to Property
- `user` - ForeignKey to User
- `requested_date`
- `status` - Pending/Approved/Rejected/Completed
- `message`
- `created_at`, `updated_at`
- **Unique together:** property + user + requested_date

### Inquiry
- `property` - ForeignKey to Property
- `user` - ForeignKey to User
- `email`, `phone`, `message`
- `is_read` - Status flag
- `created_at`

## 🎨 Admin Dashboard Features

### User Admin
- User list with role filter
- Staff member management
- User role assignment

### Agent Admin
- Agent ratings and creation date
- Phone and profile image
- Custom fieldsets for organized display

### Property Admin
- Quick filters by status, type, and agent
- Inline image management (directly edit images in property form)
- Property search by title, location, or description
- Organize fields into logical groups

### Booking Admin
- Status-based filtering
- Bulk actions: Mark as Approved/Rejected
- Search by property or user

### Inquiry Admin
- Track read/unread inquiries
- Review contact information
- Search inquiries

## 🔐 Permissions & Access Control

- **Admin**: Full system access
- **Agent**: View/manage their own listings, view bookings
- **Buyer**: View properties, book visits, submit inquiries

## 📦 Dependencies

- **Django 4.2.7** - Web framework
- **Django Jazzmin 2.13.0** - Admin interface enhancement
- **Pillow 10.0.0** - Image processing
- **Django REST Framework 3.14.0** - API development (optional)
- **Gunicorn 21.2.0** - Production server
- **Python Decouple 3.8** - Environment configuration

## 🚢 Production Deployment

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Collect static files: `python manage.py collectstatic`
5. Use Gunicorn for serving: `gunicorn config.wsgi:application`

## 📝 Next Steps / TODO

- [ ] Implement frontend views (property listing page, detail page)
- [ ] Create property search and filter views
- [ ] Build user authentication pages (login, register)
- [ ] Implement booking/appointment system views
- [ ] Add contact forms and email notifications
- [ ] Create API endpoints (optional with DRF)
- [ ] Add pagination to property listings
- [ ] Implement user profile pages
- [ ] Add property image slider/gallery
- [ ] Create pricing and payment integration

## 💡 Tips for Enhancement

1. **Email Notifications**: Use Django-celery for booking confirmations
2. **Maps Integration**: Add Google Maps or Leaflet for location display
3. **Image Optimization**: Use Pillow/Sorl-thumbnail for image optimization
4. **API Development**: Extend with Django REST Framework for mobile apps
5. **Search Enhancement**: Use Django-haystack with Elasticsearch
6. **Frontend Framework**: Integrate React or Vue for frontend

## 📞 Support & Questions

For issues or questions about the project structure, refer to the Django documentation or check individual app models.

---

**Happy Coding! 🚀**
