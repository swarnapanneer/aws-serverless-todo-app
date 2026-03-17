# 🚀 AWS Serverless Todo App

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow?logo=awslambda)
![API Gateway](https://img.shields.io/badge/API-Gateway-blue)
![DynamoDB](https://img.shields.io/badge/Database-DynamoDB-green?logo=amazondynamodb)
![S3](https://img.shields.io/badge/Hosting-S3-red?logo=amazons3)

---

## 📌 Project Overview

This is a **Full Stack Serverless Todo Application** built using AWS services.  
The application allows users to **Create, Read, Update, and Delete (CRUD)** tasks in real-time.

---

## 🏗️ Architecture


User (Browser)

↓
S3 (Static Website Hosting)

↓
API Gateway (REST API)

↓
AWS Lambda (Backend Logic)

↓
DynamoDB (Database)

---

## 🛠️ Tech Stack

- AWS Lambda  
- API Gateway (REST API)  
- DynamoDB  
- S3 (Static Website Hosting)  
- HTML, Javascript, Python  

---

## ✨ Features

- ✅ Add new tasks  
- ✅ View all tasks  
- ✅ Delete tasks  
- ✅ Update task status (via API)  
- ✅ Serverless architecture (no servers managed)  

## 📸 Screenshots

### 🖥️ Todo UI
<img width="1366" height="768" alt="todo5" src="https://github.com/user-attachments/assets/163cfe4d-703c-450d-83e0-0834b9a4b311" />


### 🗄️ DynamoDB Table
<img width="1366" height="768" alt="todo4" src="https://github.com/user-attachments/assets/9e6d2312-96bf-4b40-8af1-e232e1c93d15" />


### ⚙️ Lambda Function
<img width="1366" height="768" alt="todo2" src="https://github.com/user-attachments/assets/0865e471-1ab0-4446-b75e-e0e8f3d1570c" />
---

## 🚀 API Endpoints

### ➤ Create Task (POST)

```json
{
  "httpMethod": "POST",
  "body": "{\"title\":\"Learn AWS\"}"
}
➤ Get Tasks (GET)
{
  "httpMethod": "GET"
}
➤ Update Task (PUT)
{
  "httpMethod": "PUT",
  "body": "{\"taskId\":\"your-task-id\",\"completed\":true}"
}
➤ Delete Task (DELETE)
{
  "httpMethod": "DELETE",
  "body": "{\"taskId\":\"your-task-id\"}"
}

---

⚙️ Setup Instructions

1️⃣ Clone Repository
git clone https://github.com/your-username/aws-serverless-todo-app.git
cd aws-serverless-todo-app

2️⃣ Deploy Backend

Create DynamoDB table → todotable

Create Lambda function

Connect with API Gateway

Enable CORS

Deploy API

3️⃣ Deploy Frontend

Upload index.html to S3

Enable static website hosting

Add bucket policy for public access

🧪 Testing

✔ Tested using Lambda test events
✔ Verified CRUD operations

📊 Project Validation

Data stored and retrieved from DynamoDB

API responses validated

Frontend integrated with backend

💡 Learning Outcomes

Hands-on experience with AWS serverless services

Built REST API using API Gateway

Integrated frontend with backend

Debugged CORS and permission issues

---

---

## 📬 Contact

- GitHub: https://github.com/swarnapanneer/aws-serverless-todo-app 
- LinkedIn: www.linkedin.com/in/swarna-panneer-a493362a4

---

