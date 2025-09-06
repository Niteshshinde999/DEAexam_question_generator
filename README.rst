# 📚 AWS DEA Exam Question Generator

This project is designed for **AWS Certified Data Engineer – Associate (DEA-C01)** aspirants who want to practice exam-style questions in a mock test environment.  
It provides a Dockerized setup so you can run it anywhere without worrying about dependencies.

---

## ✨ Features
- 💡 **Practice Questions** – Realistic DEA-C01 style questions.
- ⚡ **Easy Setup** – Run with Docker in minutes.
- 🖥 **Web Interface** – Access via browser at `http://localhost:1000`.
- 🛠 **Portable** – Works on Windows, macOS, and Linux.

---

## 🛠 Prerequisites
Make sure you have these installed:
- [Docker](https://docs.docker.com/get-docker/)
- (Optional) [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Niteshshinde999/DEAexam_question_generator.git
cd DEAexam_question_generator 

docker-compose build --no-cache
docker-compose up -d
