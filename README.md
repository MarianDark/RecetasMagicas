# 🧁 Recetas Mágicas

**Recetas Mágicas** es una aplicación web desarrollada con Flask que permite a los usuarios registrados agregar, editar, ver y eliminar recetas por categoría. Es visual, responsive y moderna, con subida de imágenes incluida.

---

## ✨ Funcionalidades principales

- Registro e inicio de sesión de usuarios con Flask-Login
- Crear recetas con título, ingredientes, preparación, categoría e imagen
- Editar y eliminar recetas solo por su autor
- Ver recetas por categoría (Ensaladas, Comidas, Postres)
- Subida de imágenes con vista previa
- Página principal con últimas recetas y botones de categorías
- Diseño responsive y elegante con HTML + CSS

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Flask**
- **Flask-WTF** – Formularios con validación
- **Flask-Login** – Autenticación y sesiones
- **Flask-SQLAlchemy** – ORM para base de datos SQLite
- **Jinja2** – Plantillas HTML dinámicas
- **HTML5 / CSS3** – Frontend visual y adaptado
- **Werkzeug** – Subida de archivos segura

---

## 📁 Estructura del proyecto

```bash
RecetasMagicas/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   └── static/
├── run.py
├── config.py
├── init_db.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación local

1.Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/recetas-magicas.git
cd recetas-magicas
```

2.Crea y activa un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3.Instala las dependencias:

```bash
pip install -r requirements.txt
```

4.Crea la base de datos:

```bash
python init_db.py
```

5.Ejecuta la aplicación:

```bash
python run.py
```

Luego abre en tu navegador: `http://127.0.0.1:5000`

---

## ☁️ Despliegue en Render

1. Crea un repositorio en GitHub y sube tu proyecto.
2. Crea una cuenta en [Render](https://render.com)
3. Selecciona **New Web Service**
4. Conecta tu repositorio y selecciona:
   - Runtime: Python 3
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn run:app`
5. Añade variable de entorno:

``
FLASK_ENV=production
``

---

## 📷 Capturas

![Captura del proyecto](assets/screenshot_1.jpg)

> (Aquí puedes agregar capturas si lo deseas más adelante)

---

## 🧑‍💻 Autor

Desarrollado por **Marían** 🧡  
