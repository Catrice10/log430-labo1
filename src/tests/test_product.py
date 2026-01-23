from daos.product_dao_mongo import ProductDAOMango
from models.product import Product

dao = ProductDAOMango()

# def test_product_select():
#     product_list = dao.select_all()
#     assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Bouteille', 'Selection', '2,99')
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Ecouteurs', 'Apple', '200')
    assigned_id = dao.insert(product)
    corrected_brand = 'Samsung'
    product.id = assigned_id
    product.brand = corrected_brand
    dao.update(product)
    product_list = dao.select_all()
    brands = [p.brand for p in product_list]
    assert corrected_brand in brands
    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'Souris', 'HP', '50')
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)
    new_dao = ProductDAOMango()
    product_list = new_dao.select_all()
    names = [p.name for p in product_list]
    assert product.name not in names