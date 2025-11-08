# Masterblog‑API 🌐

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/flask-3.x-lightgrey)
![Code style: PEP8](https://img.shields.io/badge/code%20style-PEP8-yellow)
![Status](https://img.shields.io/badge/status-learning--project-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![Quick Start](https://img.shields.io/badge/⚡-Quick%20Start-orange)](#-quick-start)

*A public learning artifact on building, documenting, and consuming APIs with Flask.*

---

## 📑 Table of Contents  

- [⚠️ Disclaimer](#-disclaimer)  
- [📝 Description](#-description)  
- [✨ Features](#-features)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📦 Key Dependencies](#-key-dependencies)  
- [📁 Project Structure](#-project-structure)  
- [🛠️ Development Setup](#-development-setup)  
  - [🚀 Quick Start](#-quick-start)  
  - [📖 Step‑by‑Step Guide](#-step-by-step-guide)  
- [📖 API Documentation](#-api-documentation)  
- [👥 Contributing](#-contributing)  
- [🏷️ Badges](#-badges)  
- [🔗 See Also](#-see-also)  
  - [📊 Project Evolution Comparison](#-project-evolution-comparison)
- [📄 License](#-license) 

---

## ⚠️ Disclaimer  
This project is part of my ongoing learning journey. It builds upon the earlier **Masterblog** and **Masterblog‑core** projects, extending them into a modular architecture with a REST API and a separate UI server.  

The focus here is on:  
- Designing and documenting REST APIs with **OpenAPI 3.0** and **Swagger UI**.  
- Separating concerns between backend API and frontend UI.  
- Practicing client‑side rendering with JavaScript consuming the API.  
- Continuing to apply software engineering principles (OOP, modularity, PEP8 compliance).  

---

## 📝 Description  
**Masterblog‑API** is a modular web application consisting of two servers that separate backend logic from frontend presentation:  

- **API Server** (`api_server`)  
  - Exposes a REST interface for managing blog posts.  
  - Handles data persistence, validation, and standardized JSON responses.  
  - Includes interactive documentation via Swagger UI.  
  - Built on and reuses backend logic from [masterblog‑core](https://pypi.org/project/masterblog-core/).  

- **UI Server** (`ui_server`)  
  - Serves HTML templates and static assets.  
  - Uses JavaScript to consume the API and render posts dynamically.  
  - Provides a styled interface for interacting with the API, focused on listing posts and enabling add/delete/like actions.  
  - Designed as a lightweight client layer that demonstrates modular separation.  

---

## ✨ Features  

### 🔌 API Server  
- 📋 List all blog posts (`GET /api/posts`)  
- ↕️ Sort posts by title, content, or author (ascending/descending)  
- 🔍 Search posts by title, content, or author (`GET /api/posts/search`)  
- ➕ Add new blog posts (`POST /api/add`)  
- ✏️ Update existing blog posts (`PUT /api/posts/{id}`)  
- ❌ Delete blog posts (`DELETE /api/posts/{id}`)  
- ❤️ Like posts (`POST /api/like/{id}`)  
- 📖 Swagger UI with OpenAPI 3.0 documentation  

### 🎨 UI Server  
- 📋 Renders a list of posts (title, content, author, likes counter)  
- ➕ Provides interactive buttons to add posts  
- ❌ Provides interactive buttons to delete posts  
- ❤️ Provides interactive buttons to like posts  
- 💾 Remembers the chosen API base URL using browser local storage  
- 🎨 Styled interface with heart icon for likes counter

---

## 🛠️ Tech Stack  
- **Language:** Python 3  
- **Framework:** Flask (API + UI servers)  
- **API Docs:** Swagger UI / OpenAPI 3.0  
- **Frontend:** HTML, CSS, JavaScript (client‑side rendering)  
- **Persistence:** JSON file storage (via masterblog‑core)  

---

## 📦 Key Dependencies  
- [Flask](https://flask.palletsprojects.com/) – lightweight web framework  
- [flask‑cors](https://flask-cors.readthedocs.io/) – enable CORS for API requests  
- [flask‑swagger‑ui](https://github.com/swagger-api/swagger-ui) – interactive API docs  
- [masterblog‑core](https://pypi.org/project/masterblog-core/) – backend models and storage  

---

## 📁 Project Structure  

```
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── api_server
│   ├── api_server_app.py        # Flask REST API
│   ├── api_server_config.py     # Config and data paths
│   ├── data/                    # Local JSON storage (untracked)
│   │   ├── blog.json
│   │   └── sequence.json
│   └── static/masterblog.json   # Swagger/OpenAPI spec
└── ui_server
    ├── ui_server_app.py         # Flask UI server
    ├── static/
    │   ├── main.js              # Client-side rendering logic
    │   ├── styles.css           # UI styling
    │   └── pink_heart_apple.png # Heart icon for likes counter
    └── templates/index.html     # HTML template
```

---

## 🛠️ Development Setup  

### 🚀 Quick Start  
```bash
git clone https://github.com/paul-wosch/Masterblog-API.git \
&& cd Masterblog-API \
&& pip install -r requirements.txt
```

Run the API server:  
```bash
python api_server/api_server_app.py
```
Run the UI server:  
```bash
python ui_server/ui_server_app.py
```

Open [http://127.0.0.1:5001](http://127.0.0.1:5001) for the UI.  
Open [http://127.0.0.1:5002](http://127.0.0.1:5002) for the API.  
Swagger docs available at [http://127.0.0.1:5002/api/docs](http://127.0.0.1:5002/api/docs).  

---

### 📖 Step‑by‑Step Guide  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/paul-wosch/Masterblog-API.git
   cd Masterblog-API
   ```

2. **Create virtual environment** (optional)  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run API server**  
   ```bash
   python api_server/api_server_app.py
   ```

5. **Run UI server**  
   ```bash
   python ui_server/ui_server_app.py
   ```

6. **Access the app**  
   - UI: [http://127.0.0.1:5001](http://127.0.0.1:5001)  
   - API: [http://127.0.0.1:5002](http://127.0.0.1:5002)  
   - API docs: [http://127.0.0.1:5002/api/docs](http://127.0.0.1:5002/api/docs)  

---

## 📖 API Documentation  
The API is documented with **Swagger UI**. Key endpoints:  

- `GET /api/posts` → list posts (supports `sort`, `direction`)  
- `POST /api/add` → create a new post  
- `PUT /api/posts/{id}` → update a post  
- `DELETE /api/posts/{id}` → delete a post  
- `GET /api/posts/search` → search posts  
- `POST /api/like/{id}` → like a post  

Error responses:  
- `400 Bad Request` → invalid request or parameters  
- `404 Not Found` → resource not found  

---

## 👥 Contributing & Feedback  
This project is primarily a **learning exercise** and a snapshot of my journey in exploring modular web applications, REST APIs, and client‑side rendering.  

I don’t expect to actively maintain or extend this repository further, since my focus will move on to new areas and real‑world projects. That said, I’d be glad if others:  
- Explore the codebase and learn from it.  
- Use it as a reference for their own experiments.  
- Share thoughts, ideas, or feedback — even if I may not act on them, they’re valuable for reflection.  

Think of this project less as a collaborative product and more as a **public learning artifact**.   

---

## 🏷️ Badges

- **Python** – minimum supported Python version  
- **Code style** – follows PEP8 guidelines  
- **Status** – indicates this is a learning project  
- **License** – MIT license

---

## 🔗 See Also  
The **Masterblog** series evolved across three repositories:  

- [Masterblog](https://github.com/paul-wosch/Masterblog) – original monolithic Flask app with templates and JSON persistence.  
- [Masterblog‑core](https://github.com/paul-wosch/Masterblog-core) – extracted backend logic packaged as a reusable Python library.  
- [Masterblog‑API](https://github.com/paul-wosch/Masterblog-API) – modular architecture with a REST API, Swagger docs, and a separate UI server.  

Together, they illustrate a progression from a simple web app → a reusable library → a modular API‑driven system.  

### 📊 Project Evolution Comparison  

| Aspect              | Masterblog 📝 | Masterblog‑core 📦 | Masterblog‑API 🌐 |
|---------------------|---------------|--------------------|------------------|
| **Purpose**         | Full web app with UI + backend | Reusable backend library | Modular system with REST API + UI server |
| **Architecture**    | Monolithic Flask app | Library (no server/UI) | Split into API server + UI server |
| **UI**              | Jinja2 templates rendered server‑side | None | Client‑side rendering with JavaScript |
| **Backend**         | Blog + Post classes, JSON persistence | Same classes packaged for reuse | Reuses masterblog‑core via API |
| **Persistence**     | JSON files with sequence tracking | JSON files with sequence tracking | JSON files via masterblog‑core |
| **Features**        | CRUD + like posts | CRUD + like posts | CRUD + like posts, search, sort |
| **API**             | None (routes tied to templates) | None | REST API with Swagger/OpenAPI 3.0 docs |
| **Docs**            | README only | README + PyPI metadata | README + Swagger UI interactive docs |
| **Tech Focus**      | Flask, Jinja2, packaging basics | Packaging, distribution, OOP | REST APIs, modularity, Swagger, CORS |
| **Learning Goal**   | Build a full app from scratch | Extract reusable backend logic | Explore modular design, API docs, client‑side rendering |

---

## 📄 License  
This project is licensed under the terms of the [MIT License](./LICENSE).  
See the LICENSE file for full details.