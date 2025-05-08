from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from .models import Recipe, Category
from .forms import RecipeForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            ingredients=form.ingredients.data,
            preparation=form.preparation.data,
            category_id=form.category.data
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
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('main.index'))
