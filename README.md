# Sales Tracker CLI & API

A simple but powerful sales tracking system built in Python.  
This project evolves in **4 stages**, showcasing practical software engineering and DevOps skills.

---

## 🚀 Project Overview

The Sales Tracker project progresses through four levels:

### **A. CLI Tool (Local Script)**
A command-line application where you can:
- Add sales  
- List sales  
- View total sales  
- Store everything in a CSV file  

### **B. Deployment on AWS EC2**
The CLI tool is:
- Installed on an Ubuntu EC2 server  
- Automated with cron to capture scheduled data  
- Stored on persistent storage  

### **C. REST API Version**
The sales tracker becomes a web service using **FastAPI**:
- Create, retrieve, and summarize sales through API endpoints  
- Can be used by mobile apps, dashboards, or automation tools  

### **D. DevOps Implementation**
The project is containerized and automated:
- Dockerfile  
- Docker Compose  
- CI/CD pipeline (GitHub Actions)  
- Optional Nginx reverse proxy  
- Optional systemd service for API auto-restart  

---

## 🧰 Tech Stack

**Core:** Python  
**Storage:** CSV (CLI) → SQLite or PostgreSQL (API stages)  
**Server:** Ubuntu on AWS EC2  
**DevOps:** Git, GitHub, Cron, Docker, CI/CD  

---

## 📦 How to Use the CLI Version

### **Install Dependencies**
```
pip install -r requirements.txt
```

### **Run the CLI**
Add a sale:
```
python3 sales.py add --amount 1500
```

List all sales:
```
python3 sales.py list
```

View total sales:
```
python3 sales.py total
```

---

## 📁 Folder Structure

```
sales-tracker/
│
├── sales.py               # Main CLI script
├── sales.csv              # Auto-generated store
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── api/                   # Will contain API version in Stage C
```

---

## ☁️ Stage B – EC2 Deployment

You can deploy the tool using:

```
git clone <repo>
cd sales-tracker
python3 sales.py
```

### **Automating with Cron**
Example of a cron job:
```
0 18 * * * /usr/bin/python3 /home/ubuntu/sales-tracker/sales.py total >> daily_report.txt
```

---

## 🌐 Stage C – API Version (Coming Soon)

A FastAPI-based API will expose:
- `POST /sales`  
- `GET /sales`  
- `GET /sales/total`  
- `GET /sales/report?date=`  

---

## 🚀 Stage D – DevOps Enhancements (Coming Soon)

The final version will include:
- Dockerfile + Docker Compose  
- GitHub Actions CI/CD  
- Deployment pipeline  
- Logging & monitoring  
- Optional Nginx reverse proxy

---

## 📜 License

MIT License – free to use and modify.

---

## 🤝 Contributions

Open to suggestions and improvements.
