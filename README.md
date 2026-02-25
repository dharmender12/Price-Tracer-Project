# 🛒 Price Tracer Project

A Python-based **web scraping tool** that tracks product prices from e-commerce websites.  
This project was created as part of ** Web Scraping** assignment.

---

## 📌 Project Overview

The Price Tracer Project automates the process of monitoring product prices from different websites.  
It fetches the latest price details, processes the data, and helps users decide when to buy products at the best price.

**Key Highlights:**
- Implements core Python web scraping techniques.
- Uses `requests`, `BeautifulSoup`, and other libraries.
- Organizes data cleanly for future processing or analysis.
- Modular design for easy extension (e.g., adding more websites or products).
- 
---

## 🧰 Features

- 🔍 Scrapes product details (name, price, availability).
- 🕒 Tracks price changes over time.
- 💾 Stores scraped data in structured formats (CSV/JSON).
- 🛠 Configurable target URLs for flexible scraping.
- 🚀 Simple command-line usage.

---

## 📂 Project Structure

```
price-tracer-project/
│
├── data/                   # Contains scraped data (CSV/JSON files)
├── src/                    # Source code
│   ├── scraper.py          # Core web scraping logic
│   ├── parser.py           # Parsing & cleaning HTML content
│   └── tracker.py          # Tracks and compares price changes
│
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation (this file)
└── main.py                 # Entry point to run the project
```

---

## 🛠️ Technologies Used

- **Python 3.x**
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
- (Optional) [pandas](https://pandas.pydata.org/) for data handling

---

## 🚀 Getting Started

### Prerequisites
Make sure Python is installed (3.8+ recommended).

Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Project
```bash
python main.py
```

You can customize target URLs or product details inside the code/configuration files before running.

---

## 📄 Assignment Instructions (for submission)

1. Compress the entire `price-tracer-project` folder into a `.zip` file.
2. Upload the zip file to Google Drive.
3. Enable sharing access.
4. Submit the shareable link as required.

---

## 👨‍💻 Author

- **Dharmender**  
  (Part of Python Course – Module 17 Web Scraping Assignment)

---

## 📜 Note
This project is for educational purposes as part of the Python course assignment.
