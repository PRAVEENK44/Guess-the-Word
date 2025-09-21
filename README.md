# Guess the Word Game - Django Version

A beautiful and interactive word guessing game built with Django, Bootstrap, and deployed on Heroku.

## Features

### 🎮 Game Features
- **Word Guessing**: Guess 5-letter words with color-coded feedback
- **Daily Limits**: Maximum 3 games per day per user
- **Smart Feedback**: 
  - 🟢 Green: Correct letter in correct position
  - 🟠 Orange: Correct letter in wrong position
  - ⚫ Grey: Letter not in the word
- **Multiple Attempts**: Up to 5 guesses per game
- **Responsive Design**: Works perfectly on desktop and mobile

### 👥 User Management
- **User Registration**: Create accounts with username and password
- **Secure Authentication**: Password validation with special characters
- **Role-based Access**: Admin and Player user types
- **Session Management**: Persistent login state

### 📊 Admin Dashboard
- **Daily Reports**: View user statistics and success rates
- **User Performance**: Track individual player progress
- **Real-time Data**: Live updates of game statistics
- **Date Selection**: Filter reports by specific dates

### 🎨 Modern UI/UX
- **Beautiful Design**: Modern, clean interface with smooth animations
- **Responsive Layout**: Optimized for all screen sizes
- **Interactive Elements**: Hover effects and smooth transitions
- **Bootstrap Integration**: Professional styling with Bootstrap 5

## Technology Stack

- **Backend**: Django 3.2.25
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (development) / PostgreSQL (production)
- **Deployment**: Heroku
- **Static Files**: WhiteNoise

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd guess_the_word_django
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Seed the database:
```bash
python manage.py seed_words
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://localhost:8000`

### Default Admin Account
- **Username**: `admin`
- **Password**: `admin123$`

## How to Play

### For Players
1. **Register/Login**: Create an account or login with existing credentials
2. **Start Game**: Click "Start New Game" to begin
3. **Make Guesses**: Enter 5-letter words in uppercase
4. **Get Feedback**: Use color-coded hints to improve your next guess
5. **Win or Lose**: Guess correctly within 5 attempts or try again!

### For Admins
1. **Login**: Use admin credentials to access the dashboard
2. **View Reports**: Check daily statistics and user performance
3. **Monitor Activity**: Track game sessions and success rates
4. **Date Filtering**: Select specific dates to view historical data

## Game Rules

- **Word Length**: All words are exactly 5 letters
- **Case Sensitivity**: All input must be in UPPERCASE
- **Daily Limit**: Maximum 3 games per day per user
- **Guesses**: Up to 5 attempts per game
- **Feedback**: 
  - Green: Correct letter, correct position
  - Orange: Correct letter, wrong position
  - Grey: Letter not in the word

## Password Requirements

- **Minimum Length**: 5 characters
- **Must Include**: 
  - Letters (a-z, A-Z)
  - Numbers (0-9)
  - Special characters ($, %, *, @)

## Username Requirements

- **Minimum Length**: 5 characters
- **Characters**: Letters only (a-z, A-Z)

## Project Structure

```
guess_the_word_django/
├── game/                    # Main app
│   ├── management/         # Management commands
│   │   └── commands/
│   │       └── seed_words.py
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   └── game/
│   ├── admin.py           # Admin configuration
│   ├── models.py          # Database models
│   ├── urls.py            # URL patterns
│   ├── utils.py           # Utility functions
│   └── views.py           # View functions
├── guess_the_word_django/  # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── templates/             # Base templates
│   └── base.html
├── static/               # Static files (CSS, JS, images)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── Procfile            # Heroku deployment
└── README.md          # This file
```

## Deployment to Heroku

1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a Heroku app:
```bash
heroku create your-app-name
```

4. Set environment variables:
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

5. Deploy:
```bash
git add .
git commit -m "Initial commit"
git push heroku main
```

6. Run migrations and seed data:
```bash
heroku run python manage.py migrate
heroku run python manage.py seed_words
```

## API Endpoints

- `POST /api/start-game/` - Start a new game session
- `POST /api/submit-guess/` - Submit a word guess
- `GET /api/session/<id>/` - Get session data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please contact the development team or create an issue in the repository.
