from app import create_app, db
from app.models import Category

app = create_app()

with app.app_context():
    db.create_all()

    if not Category.query.first():
        db.session.add_all([
            Category(name='Ensaladas'),
            Category(name='Comidas'),
            Category(name='Postres')
        ])
        db.session.commit()
        print("✅ Categorías creadas.")

    print("✅ Base de datos creada con éxito.")
