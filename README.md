# 🐾 **Pawfect-Planner**  

Helping you find the best pet-friendly places and events!  

## 📌 **Overview**  
Pawfect Planner is an intelligent pet-friendly location and event discovery tool designed to help pet owners find the best activities for their pets. This extension integrates:  
✅ **Wikipedia API** – Provides breed-specific details like size, temperament, and origin.  
✅ **Yelp API** – Fetches local pet-related events, including event names, dates, locations, and website links.  
✅ **Weather API** – Suggests pet-friendly places based on real-time weather conditions.  

---

## 🛠 **Installation**  

### **1️⃣ Clone the Repository**  
To download the project, open your terminal and run:  
```bash
git clone https://github.com/Wenjun-Charon/pawfect-planner.git
cd pawfect-planner
```

### **2️⃣ Set Up a Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
Run the following command to install required Python packages:
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**

This project requires API keys for Google Places, OpenWeatherMap, and Yelp.  
•	Set them as environment variables:
```bash
export GOOGLE_PLACES_API_KEY="your_google_api_key"
export OPENWEATHERMAP_API_KEY="your_openweather_api_key"
export YELP_API_KEY="your_yelp_api_key"
```

•	Or create a .env file inside the project directory:
```bash
GOOGLE_PLACES_API_KEY=your_google_api_key
OPENWEATHERMAP_API_KEY=your_openweather_api_key
YELP_API_KEY=your_yelp_api_key
```

---

## 🚀 **Usage**

Run the Main Script

To start the application, run:
```bash
python main.py
```
**Input Information**

The script will prompt for:
	**•	City Name or ZIP Code** 📍 (to fetch local pet-friendly locations & weather).
	**•	Dog Breed** 🐶 (optional, for breed-specific insights from Wikipedia).

**Output Includes:**

✔️ **Weather Report 🌤️
✔️ Pet-Friendly Locations 🏡
✔️ Upcoming Pet Events 🎉
✔️ Breed-Specific Insights** 🐕

---

## 📂 **Project Structure**
```
pawfect-planner/
│── src/
│   ├── fetch_weather.py       # Weather API integration
│   ├── fetch_pet_places.py    # Google Places & Yelp API integration
│   ├── fetch_pet_events.py    # Yelp API event search
│   ├── fetch_wiki_breeds.py   # Wikipedia breed data retrieval
│   ├── main.py                # Main script to run the program
│── requirements.txt           # Python dependencies
│── README.md                  # Project documentation
```

---

## 🔧 Future Improvements

🔹 **UI Enhancements** – Build a web or mobile app version for better user interaction.  
🔹 **Advanced Event Filtering** – Allow users to filter events by category, date range, or distance.  
🔹 **More Data Sources** – Integrate Wikidata for structured breed characteristics.  
🔹 **NLP for Breed Insights** – Extract structured information from Wikipedia breed descriptions.  

---

## 🤝 Contributing

We welcome contributions! Feel free to **submit pull requests** or report issues in the repository.  

---

📜 License

This project is licensed under the **MIT License**.
