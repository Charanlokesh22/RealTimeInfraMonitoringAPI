Real-Time Infra Monitoring API
A lightweight platform-focused API built using FastAPI to monitor real-time system metrics (CPU usage, memory usage, and response time) of service agents. Includes threshold-based alerting, secure token-based access, and event logging for SRE and DevOps use cases.

Project Overview
This project simulates and tracks the performance metrics of infrastructure components, offering:
1) Real-time monitoring of system metrics
2) Intelligent alerts on threshold breaches
3) Secure access to metrics via JWT and OAuth2
4) Persistent logging of events in MongoDB
5) API endpoints validated using Postman


Features :

1)System Metrics Monitoring: Continuously tracks CPU usage, memory usage, and response time for simulated agents
2)Intelligent Alerting: Sends alerts when thresholds are breached for proactive incident response
3)Secure API: JWT authentication and OAuth2-based token access
4)Event Logging: All alerts and breaches logged in MongoDB with timestamp and severity
5)Postman Validated: API endpoints tested and verified with Postman for functional correctness


Tech Stack:
1)Backend Framework: FastAPI (Python)
2)Database: MongoDB
3)Security: JWT, OAuth2
4)Testing Tools: Postman
5)Others: Python Logging, Pydantic for validation




Setup Instructions :-

Clone the repository
git clone https://github.com/Charanlokesh22/real-time-monitoring-api.git
cd real-time-monitoring-api


Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate


Install dependencies
pip install -r requirements.txt
Configure environment variables


Create a .env file with:

MONGO_URI=your_mongo_connection_string
JWT_SECRET=your_jwt_secret_key


Run the application
uvicorn main:app --reload





