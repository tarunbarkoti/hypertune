# AI Model Fine-Tuning Platform

An **AI Fine-Tuning Platform** that provides an **end-to-end automated pipeline** for fine-tuning pre-trained models. Built with **Flask**, **Tailwind CSS**, and **Spheron Network**, this platform offers a seamless and scalable experience for optimizing AI models with user-defined configurations.

Originally developed during **Frosthack**, a hackathon conducted by **IIT Mandi** as part of the annual techfest **Xpecto'25**, the platform has since been enhanced **post-hackathon** to improve performance, usability, and reliability.

---

## Key Features

### **1. AI Model Selection**
- Choose from **LLaMA 3, Mistral, and SmolLM** models.
- Supports **custom dataset uploads** for training.

### **2. Dataset Management & Preprocessing**
- Upload datasets in **JSON, CSV, and JSONL** formats.
- Automated **data validation and cleaning** for efficiency.

### **3. Fine‑Tuning Configuration**
- Adjust **learning rate, batch size, epochs, and other hyperparameters**.
- Supports **Spheron’s decentralized GPU network** for high-speed tuning (see [Spheron Network](https://www.spheron.network/)).

### **4. Real-Time Model Tracking & Evaluation**
- Monitor **loss, accuracy, and improvement metrics** live.
- Compare multiple model versions with **benchmarking tools**.

### **5. One‑Click Model Deployment**
- Deploy fine-tuned models instantly to **inference endpoints**.
- Generate **API keys for easy integration** into applications.

### **6. Secure Authentication & Dashboard**
- User **login, registration, and secure access control**.
- Intuitive dashboard for tracking **fine‑tuning progress**.

---

## Technology Stack

### **Frontend (UI/UX)**
- **HTML, Tailwind CSS, JavaScript, Bootstrap** – Modern, responsive design.

### **Backend & API**
- **Flask (Python)** – API development and request handling.
- **Flask‑Login, Flask‑Bcrypt** – User authentication & security.
- **Spheron Network** – Decentralized GPU acceleration

### **Machine Learning & AI**
- **PyTorch, TensorFlow, Hugging Face** – Model fine‑tuning.
- Models supported: **LLaMA 3, Mistral, SmolLM**.
- **Custom hyperparameter tuning** with dynamic parameter adjustments.

---

## Installation Guide

### **1. Clone the Repository**
```bash
git clone https://github.com/tarunbarkoti/hypertune
cd hypertune
```

### **2. Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Flask App**
```bash
python app.py
```

### **5. Access the Web App**
Open your browser and navigate to:  
**http://127.0.0.1:5000/**

---

## Contribution & Collaboration

We welcome contributions from developers, AI enthusiasts, and researchers! To contribute:

1. **Fork the repository**
2. **Create a feature branch**
3. **Commit changes and submit a pull request**

Feel free to reach out for collaboration opportunities.

---

## License

This project is **open-source** under the **MIT License**.

---

## Authors & Contributors

- **Lead Developers:** Tarun Barkoti & Naman Sachdeva 
- **Contributors:** Aniket Prashar & Chaitanya Dalal

