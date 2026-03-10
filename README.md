# Assist College AI Chatbot

## Project Overview
Assist College AI is a web-based chatbot designed to help students quickly find information about colleges.  
Users can ask questions like:

- Top colleges in Chennai
- Best engineering colleges
- Colleges in Coimbatore
- Colleges in Madurai

The chatbot reads data from a CSV dataset and responds using keyword matching.

The project is built using Python and Flask and deployed online using Render.

Live Demo:
https://assist-college-ai.onrender.com

---

## Features

- Chatbot interface for students
- College search by city
- Keyword-based response system
- 40 college dataset
- Simple UI interface
- Cloud hosted chatbot

---

## Technologies Used

Python  
Flask  
Pandas  
HTML  
CSS  
JavaScript  
CSV Dataset  
Gunicorn  
GitHub  
Render Cloud Hosting

---

## How the System Works

1. User types a question in the chatbot.
2. The message is sent to the Flask backend.
3. The backend processes the message.
4. Keywords are extracted from the message.
5. The system searches the college dataset.
6. Matching results are returned to the user.

---

## Dataset

The chatbot uses a CSV dataset containing 40 colleges including:

Anna University – Chennai  
Loyola College – Chennai  
Madras Christian College – Chennai  
Stella Maris College – Chennai  
SRM Institute of Science and Technology – Chennai  
Sathyabama Institute of Science and Technology – Chennai  
VIT University – Vellore  
PSG College of Technology – Coimbatore  
Coimbatore Institute of Technology – Coimbatore  
Kumaraguru College of Technology – Coimbatore  
Amrita Vishwa Vidyapeetham – Coimbatore  
Karunya Institute of Technology – Coimbatore  
SNS College of Technology – Coimbatore  
Sri Ramakrishna Engineering College – Coimbatore  
Hindusthan College of Engineering – Coimbatore  
Panimalar Engineering College – Chennai  
Sri Sairam Engineering College – Chennai  
Thiagarajar College of Engineering – Madurai  
PSNA College of Engineering – Dindigul  
Karpagam Institute of Technology – Coimbatore  
Sri Krishna College of Engineering – Coimbatore  
KPR Institute of Engineering – Coimbatore  
Kongu Engineering College – Erode  
Bannari Amman Institute of Technology – Erode  
Sastra University – Thanjavur  
Periyar Maniammai Institute – Thanjavur  
NIT Trichy – Tiruchirappalli  
SRM Trichy Arts and Science College – Trichy  
Bishop Heber College – Trichy  
St. Joseph's College – Trichy  
Fatima College – Madurai  
American College – Madurai  
Lady Doak College – Madurai  
Alagappa University – Karaikudi  
RVS College of Engineering – Coimbatore  
Park College of Engineering – Coimbatore  
Info Institute of Engineering – Coimbatore  
Dr. Mahalingam College of Engineering – Pollachi  
PSG College of Arts and Science – Coimbatore

---

## Deployment

The project is deployed on Render cloud platform.

Steps used for deployment:

1. Upload project to GitHub
2. Connect GitHub repository to Render
3. Configure Python runtime
4. Install dependencies using requirements.txt
5. Start server using Gunicorn
6. Render provides public URL

Live link:
https://assist-college-ai.onrender.com

---

## Future Enhancements

- AI based natural language understanding
- Mobile responsive UI
- Voice assistant integration
- Course based college filtering
- Placement statistics integration
- College ranking system
