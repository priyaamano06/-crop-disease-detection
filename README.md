# 🌾 Smart Agriculture System

AI-Powered Crop Disease Detection and Farming Assistant

## Features

- ✅ Accurate crop disease detection using deep learning
- ✅ Optimized anchor boxes using K-Means clustering
- ✅ Real-time weather integration
- ✅ Disease severity analysis
- ✅ Treatment recommendations
- ✅ Farmer-friendly interface (Greenish Theme 🌿)

## Tech Stack

### Frontend
- React.js
- HTML5/CSS3 (Greenish Theme)
- Axios

### Backend
- Python 3.9+
- FastAPI
- PyTorch
- OpenCV

### ML/AI
- YOLOv5
- K-Means Clustering
- Transfer Learning

### Database
- PostgreSQL

## Installation

### Prerequisites
- Python 3.9+
- Node.js 18+
- Docker (optional)

### Quick Start

1. **Clone the repository** (if not already done)
   
2. **Setup Environment**
   - Copy `.env.example` to `.env`
   - Update `OPENWEATHER_API_KEY` with your key.

3. **Run with Docker** (Recommended)
   ```bash
   docker-compose up --build
   ```

4. **Access the Application**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:8000](http://localhost:8000)
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Manual Run

**Backend:**
```bash
cd backend
python -m venv venv
# Activate venv (Windows: venv\Scripts\activate, Unix: source venv/bin/activate)
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```
