# Guess the Word Game

A modern, interactive word guessing game featuring beautiful animations, real-time updates, and comprehensive admin reporting.

## 🎮 Features

### Core Gameplay
- 5-letter word guessing with 5 attempts maximum
- Color-coded feedback: Green (correct position), Orange (wrong position), Gray (not in word)
- Daily limit: 3 games per day per user
- Smart word validation and input handling
- Beautiful animations for letter reveals and victories

### User Management
- Dual user types: Admin and Player roles
- Secure authentication with username/password
- Registration validation: Username (5+ letters), Password (5+ chars with special chars)
- Session management with automatic logout

### Admin Dashboard
- Daily reports: User statistics and success rates
- User performance tracking: Games played, wins/losses
- Date filtering for historical analysis
- Real-time statistics with visual charts

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PRAVEENK44/Guess-the-Word.git
   cd Guess-the-Word
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database**
   ```bash
   python manage.py migrate
   ```

5. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Game: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🎯 How to Play

1. Register/Login with your credentials
2. Start a new game (up to 3 per day)
3. Guess 5-letter words and get color feedback
4. Win by guessing correctly or try again after 5 attempts
5. View your progress in the admin dashboard

## 📁 Project Structure

```
Guess-the-Word/
├── game/                          # Main Django app
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # URL routing
│   ├── admin.py                   # Admin configuration
│   ├── utils.py                   # Utility functions
│   └── migrations/                # Database migrations
├── guess_the_word_django/         # Django project settings
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
├── templates/                     # HTML templates
│   ├── base.html
│   └── game/
│       ├── game_board.html
│       ├── login.html
│       ├── register.html
│       └── admin_dashboard.html
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── Procfile                       # Heroku deployment
└── README.md                      # This file
```

## 🛠️ Technologies Used

- **Backend**: Python 3.8+
- **Framework**: Django
- **Frontend**: Bootstrap 5, JavaScript ES6, CSS3
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Heroku-ready with Procfile

## 🚀 Deployment

### Heroku Deployment
1. Create a Heroku app
2. Set environment variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   ```
3. Deploy:
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   ```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

- **GitHub**: [@PRAVEENK44](https://github.com/PRAVEENK44)
- **Repository**: [Guess-the-Word](https://github.com/PRAVEENK44/Guess-the-Word)

---

⭐ **Star this repository if you found it helpful!**
