# Django User Authentication System - TODO List
     url: https://3hxsbfsl-8080.inc1.devtunnels.ms/
## 1. Project Setup
- [x] Install Django
- [x] Create new Django project: `auth_project`
- [x] Create `accounts` app
- [x] Configure `settings.py` (INSTALLED_APPS, authentication settings)

## 2. Models
- [x] Use Django's built-in User model (no custom model needed)

## 3. Forms
- [x] Create `UserRegistrationForm` in `accounts/forms.py`
- [x] Create `UserLoginForm` in `accounts/forms.py`

## 4. Views
- [x] Create `register_view` in `accounts/views.py`
- [x] Create `login_view` in `accounts/views.py`
- [x] Create `logout_view` in `accounts/views.py`
- [x] Create `dashboard_view` (protected) in `accounts/views.py`

## 5. URLs
- [x] Create `accounts/urls.py` with URL mappings
- [x] Update main `auth_project/urls.py` to include accounts URLs

## 6. Templates
- [x] Create `templates/base.html`
- [x] Create `templates/register.html`
- [x] Create `templates/login.html`
- [x] Create `templates/dashboard.html`

## 7. Database & Testing
- [x] Run migrations
- [x] Test registration, login, logout, and protected routes
- [x] Verify security features (password hashing, session management)

## 8. Deployment to Render
- [x] Create requirements.txt with dependencies
- [x] Update settings.py for production (env vars, PostgreSQL, whitenoise)
- [x] Create Procfile for gunicorn
- [x] Update .gitignore (already done)
- [ ] Push code to GitHub
- [ ] Create Render account and new Web Service
- [ ] Connect GitHub repo
- [ ] Add PostgreSQL database on Render
- [ ] Set environment variables: DJANGO_SECRET_KEY, DEBUG=False, ALLOWED_HOSTS=your-render-url.onrender.com, DATABASE_URL=postgres-url
- [ ] Deploy and run migrations
- [ ] Test the live app

## 9. Optional Enhancements (Future)
- [ ] Email verification
- [ ] Password reset
- [ ] User roles/permissions
- [ ] Custom user profile
