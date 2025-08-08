 Real-Time Infra Monitoring API (SRE/Platform Focus)

Description
Built a real-time monitoring API to track CPU, memory, and response time from simulated service agents.  
Triggered intelligent alerts when thresholds were breached and logged all events securely in MongoDB.  
Secured backend endpoints using JWT authentication and implemented OAuth2 for controlled access flow.

Tech Stack
FastAPI  
MongoDB  
Python  
JWT  
OAuth2  
Postman  

Features
- Real-time metrics monitoring (CPU, RAM, response time)
- Threshold-based alerts
- Event logging in MongoDB
- Secure endpoints using JWT & OAuth2
- Tested with Postman


Installation
1. Clone the repository  
   git clone https://github.com/yourname/repo-name.git

2. Navigate to the project directory  
   cd repo-name

3. Create a virtual environment  
   python -m venv venv

4. Activate the environment  
   - Windows: venv\Scripts\activate 
   - Mac/Linux: source venv/bin/activate

5. Install dependencies  
   pip install -r requirements.txt

6. Run the FastAPI app  
   uvicorn main:app --reload

 API Testing :
Use Postman to test the following endpoints:
- `POST /token` – Get access token
- `GET /metrics/cpu` – View current CPU usage
- `GET /metrics/memory` – View memory usage
- `GET /metrics/response-time` – Get response time of simulated agents
