# SERVICE PROJECT

First frontend model for the Service Project.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open:
http://127.0.0.1:10000

## Structure

- `app.py` - Flask application
- `templates/base.html` - common frontend template
- `templates/index.html` - home page
- `static/css/style.css` - all common styles
- `static/js/main.js` - frontend JavaScript
- `models/user.py` - initial User model placeholder
- `render.yaml` - Render deployment configuration

The search bar is fixed directly below the header. Login, registration, database, services and booking functionality will be connected in the next development steps.
