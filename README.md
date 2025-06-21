# 🎲 Luckydice - Django Web Game

Luckydice is a web-based multiplayer dice game built using Django, HTML/CSS, JavaScript, and integrated with secure payment gateways. The application offers real-time gameplay, transaction tracking, and a smooth user experience — all designed for entertainment and engagement.

---

## 🚀 Features

- 🎮 Dice-based game logic with interactive UI
- 🔐 Razorpay payment integration for wallet-based transactions
- 👥 User registration, login, and profile management
- 💳 Wallet system with secure add-cash functionality
- ✅ Optimized UX with AJAX and JavaScript enhancements
- 🔄 CI/CD pipeline for automated testing and deployment
- 🧪 Unit testing to ensure backend reliability and smooth gameplay

---

## 🛠️ Tech Stack

| Layer        | Technologies                          |
|--------------|----------------------------------------|
| Backend      | Python, Django                         |
| Frontend     | HTML5, CSS3, JavaScript                |
| Payments     | Razorpay API                           |
| Database     | SQLite (Development) / MySQL (Optional for Production) |
| DevOps       | Git, GitHub, CI/CD (GitHub Actions/Manual) |

---

## 🧪 Testing & CI/CD

- Unit tests written using Django's testing framework
- GitHub integrated CI/CD flow for code reliability and fast iteration
- Manual deployment to a live server (Bluehost) with proper static file handling

---

## 📷 Screenshots

> *(Add screenshots of your UI/game interface here — optional but powerful)*

---

## 🧾 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (optional but recommended)

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/abhishek944-hash/luckydicemain.git
cd luckydicemain

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
