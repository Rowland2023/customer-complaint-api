📘 README.md
markdown
# 🛠️ Customer Complaint Prioritization API

This Python Flask API helps customer support teams process complaints based on urgency, category severity, and customer type. It implements smart escalation handling using timestamps and VIP status and returns the next ticket in priority order using custom sorting logic.

---

## 🚀 Features

- 🔁 Prioritizes complaints using:
  - VIP status
  - Complaint category (with custom priority ranking)
  - Submission time (escalation threshold: 2 hours)
- 📥 Submit new complaints via POST
- 🔍 Retrieve next complaint for resolution via GET
- 🧠 Sorted using custom logic with `datetime`, `timedelta`, and lexical rules

---

## 🧰 Tech Stack

- Python 3
- Flask
- RESTful API architecture
- Native Python data structures

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Rowland2023/customer-complaint-api.git
cd customer-complaint-api

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
📤 Sample API Requests
Add a Complaint
http
POST /add_complaint
Content-Type: application/json

{
  "customer_type": "VIP",
  "category": "Payment Issue",
  "timestamp": "2023-07-01T10:00:00"
}
Get Next Complaint
http
GET /next_complaint
🔮 Future Improvements
Swagger UI documentation

Docker containerization

Persistent storage with SQLite or PostgreSQL

Automated testing with pytest

Role-based authentication

🧠 Author
Developed by Rowland2023 Licensed under the MIT License


---

## 📄 CV / Portfolio Description

> **Customer Complaint Prioritization API**  
> Built a RESTful backend service using Python and Flask to automate the prioritization of customer complaints. Implements escalation logic based on submission timestamps, complaint category, and VIP status. Includes input validation, error handling, and queue sorting using Python data structures. Designed for scalability and future deployment.

---

### 📦 requirements.txt

```txt
Flask==2.3.2
🧹 .gitignore
txt
__pycache__/
*.pyc
.env
*.log



