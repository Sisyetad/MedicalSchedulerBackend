# 🏥 Django Hospital Management System

A secure and scalable hospital management system built with Django. This project supports core healthcare workflows like employee management, patient handling, diagnosis tracking, authentication with logging, and Role-Based Access Control (RBAC).

---

## ⚙️ Features

### 👨‍⚕️ 1. Employee & Role Management
- 🏢 Multi-branch support (head office & sub-branches)
- 👥 Role-based users: `Admin`, `Branch Manager`, `Doctor`, `Receptionist`, `Patient`
- 📋 Staff registration and branch assignment
- 🔐 Permission control via RBAC

### 🧍 2. Patient Management
- 📝 Secure patient registration
- 📁 Centralized patient records
- 👁️ View/edit access controlled by role

### 🧪 3. Diagnosis & Medical Records
- 🩺 Doctors add/manage diagnoses
- 🔒 Secure storage of sensitive data and diagnosis of the patient
- 🧾 Medical history tied to patient profiles

### 🔐 4. Authentication & Security
- 🔑 Django-based secure login
- 🚫 Unauthorized access prevention
- 📊 User login & action logs (auditing)
- 🛡️ Data protection with fine-grained access rules

### 🧑‍💼 5. RBAC (Role-Based Access Control)
- 🎯 Permissions defined per role
- 🔍 Restrict views/actions based on roles
- ⚙️ Admins manage users and role settings

---

## 🧰 Tech Stack

| Layer          | Technology                                  |
|----------------|---------------------------------------------|
| 🧠 Backend      | Django, Django REST Framework               |
| 🗄️ Database     | PostgreSQL / SQLite                         |
| 🔐 Auth         | Django auth system + Custom RBAC            |
| 📘 Logging      | Django logs or custom user activity log     |

---

## 📁 Project Structure
medicalSchedulerbackend/
###### ├── 🧑 Admin/ 
###### ├── 👩‍⚕️ Branch/ 
###### ├── 👩‍⚕️ Doctor/
###### ├── 🧬 Diagnosis/ 
###### ├── 👨‍🦽 Patient/ 
###### ├── 🧍‍♂️🧍‍♀️ Queue/ 
###### ├── 👩‍⚕️ Receptionist/ 
###### ├── 👥 Role/ 
###### ├── 🧪 manage.py
###### └── 📄 README.md




---

## 🚀 Getting Started

### 🔽 1. Clone the repo

```bash
git clone git@github.com:Sisyetad/MedicalSchedulerBackend.git
cd MedicalSchedulerBackend
```
### 🧪 2. Set up environment.
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 📦 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 🔧 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 👤 5. Create superuser
```bash
python manage.py createsuperuser
```
### 🏃 6. Run the server
```bash
python manage.py runserver
```

## 🔒 Security Notes
#### ⚠️ Set DEBUG = False in production 

#### 🔐 Use HTTPS in deployed environments

#### 🔁 Rotate secrets & secure your DB

#### ✅ RBAC is enforced across the system
