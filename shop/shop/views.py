from . import app


@app.route('/category')
def category_index():
    pass


@app.route('/category/add')
def category_add():
    pass


@app.route('/category/edit/<int:category_id>')
def category_edit(category_id):
    pass
