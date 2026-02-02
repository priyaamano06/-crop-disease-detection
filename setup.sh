#!/bin/bash

echo "🚀 Setting up Smart Agriculture System..."

# Create directories (already handled, but ensuring)
mkdir -p backend/app/{models,routes,utils}
mkdir -p backend/weights
mkdir -p frontend/src/components
mkdir -p ml_training/{dataset/{train,val,test},scripts,config}
mkdir -p database

# Install backend dependencies
echo "Installing backend dependencies..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Install frontend dependencies
echo "Installing frontend dependencies..."
cd frontend
npm install
cd ..

# Download pre-trained model (YOLOv5s)
echo "Downloading base model..."
cd backend/weights
# Check if wget exists
if command -v wget &> /dev/null; then
    wget https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s.pt
else
    echo "wget not found, skipping model download. Please download manually."
fi
cd ../..

echo "✅ Setup complete!"
