# Guess the word Game

A modern, interactive word guessing game featuring beautiful animations, real-time updates, and comprehensive admin reporting.

## Features

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

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/PRAVEENK44/Guess-the-Word.git
   cd guess-the-word-django
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up database
   ```bash
   python manage.py migrate
   python manage.py seed_words
   ```

5. Create admin user
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server
   ```bash
   python manage.py runserver
   ```

7. Access the application
   - Game: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## How to Play

1. Register/Login with your credentials
2. Start a new game (up to 3 per day)
3. Guess 5-letter words and get color feedback
4. Win by guessing correctly or try again after 5 attempts
5. View your progress in the admin dashboard
