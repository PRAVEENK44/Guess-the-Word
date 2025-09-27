# 🎮 Guess the Word - Django Game

A modern, interactive word guessing game built with Django, featuring beautiful animations, real-time updates, and comprehensive admin reporting.

## ✨ Features

### 🎯 **Core Gameplay**
- **5-letter word guessing** with 5 attempts maximum
- **Color-coded feedback**: Green (correct position), Orange (wrong position), Gray (not in word)
- **Daily limit**: 3 games per day per user
- **Smart word validation** and input handling
- **Beautiful animations** for letter reveals and victories

### 👥 **User Management**
- **Dual user types**: Admin and Player roles
- **Secure authentication** with username/password
- **Registration validation**: Username (5+ letters), Password (5+ chars with special chars)
- **Session management** with automatic logout

### 📊 **Admin Dashboard**
- **Daily reports**: User statistics and success rates
- **User performance tracking**: Games played, wins/losses
- **Date filtering** for historical analysis
- **Real-time statistics** with visual charts

### 🎨 **Modern UI/UX**
- **Responsive design** with Bootstrap 5
- **Glass-morphism effects** and gradient backgrounds
- **Smooth animations** and transitions
- **Toast notifications** instead of browser alerts
- **Confetti celebrations** on victories
- **Loading states** and progress indicators

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/guess-the-word-django.git
   cd guess-the-word-django
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
   python manage.py seed_words
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

## 🎮 How to Play

1. **Register/Login** with your credentials
2. **Start a new game** (up to 3 per day)
3. **Guess 5-letter words** and get color feedback
4. **Win by guessing correctly** or try again after 5 attempts
5. **View your progress** in the admin dashboard

## 🛠️ Project Structure

```
guess_the_word_django/
├── game/                          # Main Django app
│   ├── management/
│   │   └── commands/
│   │       ├── seed_words.py      # Database seeding
│   │       └── cleanup_words.py   # Word cleanup
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # URL routing
│   └── utils.py                   # Game utilities
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   └── game/
│       ├── game_board.html        # Main game interface
│       ├── login.html             # Login page
│       ├── register.html          # Registration page
│       └── admin_dashboard.html   # Admin reports
├── static/                        # Static files
├── requirements.txt               # Python dependencies
├── Procfile                       # Heroku deployment
└── README.md                      # This file
```

## 🗄️ Database Models

### **CustomUser**
- Extended Django User with role field
- Roles: 'admin' or 'player'

### **GameWord**
- Stores 5-letter words for the game
- 500+ words seeded by default

### **GameSession**
- Tracks individual game sessions
- Stores guesses, completion status, win/loss

### **GameGuess**
- Individual guesses within a session
- Stores word, feedback, and correctness

## 🎨 Design System

### **Color Palette**
- **Primary**: Blue gradients (`#667eea` → `#764ba2`)
- **Accent**: Coral gradients (`#ff6b6b` → `#ee5a24`)
- **Success**: Green (`#00b894`)
- **Warning**: Orange (`#fdcb6e`)
- **Error**: Red (`#ff6b6b`)

### **Typography**
- **Headings**: Gradient text effects
- **Body**: Clean, readable fonts
- **Icons**: Bootstrap Icons

## 📱 Responsive Design

- **Mobile-first** approach
- **Bootstrap 5** grid system
- **Touch-friendly** interface
- **Adaptive layouts** for all screen sizes

## 🔧 Management Commands

### **Seed Database**
```bash
python manage.py seed_words
```
- Adds 500+ five-letter words
- Creates default admin user

### **Cleanup Words**
```bash
python manage.py cleanup_words
```
- Removes any 4-letter words
- Ensures data integrity

## 🚀 Deployment

### **Heroku**
1. Create Heroku app
2. Set environment variables
3. Deploy with Git

### **Environment Variables**
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
```

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Check code quality
flake8 .
black .
```

## 📈 Performance Features

- **Database optimization** with proper indexing
- **Static file serving** with WhiteNoise
- **Session management** for user state
- **Real-time updates** without page refresh
- **Efficient queries** for admin reports

## 🔒 Security Features

- **CSRF protection** on all forms
- **User authentication** and authorization
- **Input validation** and sanitization
- **Secure session handling**
- **Role-based access control**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django framework
- Bootstrap for UI components
- Bootstrap Icons for icons
- All contributors and testers

---

**Made with ❤️ and Django**
