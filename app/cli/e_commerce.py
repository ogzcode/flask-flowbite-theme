import click
from app import db
from faker import Faker
from app.models import Product

@click.command("seed-products", help="Seed products into the database.")
def seed_products():
    fake = Faker()
    for _ in range(100):
        product = Product(
            name=fake.name(),
            description=fake.sentence(),
            price=fake.random_int(1, 100),
            stock=fake.random_int(1, 100),
            category=fake.random_element(["Electronics", "Clothing", "Books", "Toys", "Tools"])
        )
        db.session.add(product)
    db.session.commit()
    click.echo("Products seeded.")


@click.command("clear-products", help="Clear all products from the database.")
def clear_products():
    Product.query.delete()
    db.session.commit()
    click.echo("Products cleared.")
