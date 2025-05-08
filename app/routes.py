from flask import Blueprint, render_template, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from .models import Recipe, Category
from .forms import RecipeForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    recipes = Recipe.query.all()
    categories = Category.query.all()  # ⬅️ Esto permite mostrar los botones
    return render_template('index.html', recipes=recipes, categories=categories)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    
    filename = None
    if form.validate_on_submit():
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            img_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.image.data.save(img_path)

        recipe = Recipe(
            title=form.title.data,
            ingredients=form.ingredients.data,
            preparation=form.preparation.data,
            category_id=form.category.data,
            image=filename,
            user_id=current_user.id
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_recipe.html', form=form)

@bp.route('/category/<int:cat_id>')
def category(cat_id):
    cat = Category.query.get_or_404(cat_id)
    return render_template('category.html', category=cat)

@bp.route('/delete/<int:recipe_id>')
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        return "❌ No tienes permiso para eliminar esta receta", 403
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('main.index'))
