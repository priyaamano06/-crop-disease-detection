import requests
import os

API_URL = "http://localhost:8000"

def test_health():
    """Test if API is running"""
    try:
        response = requests.get(f"{API_URL}/")
        print(f"Health Check: {response.json()}")
    except Exception as e:
        print(f"Health Check Failed: {e}")

def test_disease_detection():
    """Test disease detection endpoint"""
    # Use a sample image
    image_path = "test_images/sample_leaf.jpg"
    
    if not os.path.exists(image_path):
        print("Test image not found! Please place a 'sample_leaf.jpg' in 'test_images' folder to test.")
        return
    
    with open(image_path, 'rb') as f:
        files = {'file': f}
        try:
            response = requests.post(f"{API_URL}/api/detect-disease", files=files)
            print(f"Disease Detection: {response.json()}")
        except Exception as e:
            print(f"Disease Detection Test Failed: {e}")

def test_weather():
    """Test weather endpoint"""
    location = "Mumbai"
    try:
        response = requests.get(f"{API_URL}/api/weather/{location}")
        print(f"Weather Data: {response.json()}")
    except Exception as e:
        print(f"Weather Test Failed: {e}")

if __name__ == "__main__":
    print("Running API Tests...\n")
    test_health()
    print()
    test_disease_detection()
    print()
    test_weather()
