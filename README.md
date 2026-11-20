# Aeroport — backend (Django REST API)

REST API for an airport services system: flights, airlines, passengers, tickets, baggage, staff, and the
shops and service points inside the terminal. JWT authentication, search and filtering, and an admin panel.
The React client lives in [aeroport-frontend](https://github.com/ilhomjonshoyimov10-cyber/aeroport-frontend).

> 🇺🇿 **O'zbekcha:** Aeroport xizmatlari uchun REST API: parvozlar, aviakompaniyalar, yo'lovchilar, chiptalar,
> bagaj, xodimlar, terminal ichidagi do'kon va xizmat nuqtalari. JWT autentifikatsiya, qidiruv va filtrlar,
> Jazzmin admin panel.

## Stack

Python · Django 6 · Django REST Framework · SimpleJWT · django-filter · django-cors-headers · Jazzmin admin · SQLite · Gunicorn

## Data model

| Model | Purpose |
|---|---|
| `Aviakompaniya` | Airline |
| `Parvoz` | Flight, linked to an airline; status: scheduled, delayed, cancelled, departed, landed |
| `Yolovchi` | Passenger |
| `Chipta` | Ticket |
| `Bagaj` | Baggage |
| `Xodim` | Staff member |
| `Kategoriya` | Category of a service point |
| `XizmatKorsatishNuqtasi` | Service point in the terminal (location, opening hours, photo) |
| `Mahsulot` | Product sold at a service point (price, availability, photo) |

## API

| Endpoint | Description |
|---|---|
| `POST /api/register/` | Create a user (username, email, password) |
| `POST /api/token/` · `POST /api/token/refresh/` | Obtain and refresh JWT tokens |
| `/api/parvozlar/` | Flights (CRUD) |
| `/api/aviakompaniyalar/` | Airlines |
| `/api/yolovchilar/` | Passengers |
| `/api/chiptalar/` | Tickets |
| `/api/bagajlar/` | Baggage |
| `/api/xodimlar/` | Staff |
| `/api/kategoriyalar/` · `/api/xizmatlar/` · `/api/mahsulotlar/` | Categories, service points, products; `?search=` and filters |
| `/admin/` | Jazzmin admin panel |

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver                          # http://127.0.0.1:8000/api/
```

## Production notes

The backend is configured for Render (`aeroport-backend.onrender.com` in `ALLOWED_HOSTS`). Before using it
with real users, read `SECRET_KEY` and `DEBUG` from environment variables, set `DEBUG = False`, and move
from the committed SQLite file to PostgreSQL.
