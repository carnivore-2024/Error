import mysql.connector
conn = mysql.connector.connect(host="localhost",username="carnivore",password="Carni5721",database="game")
c = conn.cursor()


def add(name,description,price,quantity,category):
    query = "INSERT INTO products1 (name,description,price,quantity,category) VALUES (%s,%s,%s,%s,%s)"
    c.execute(query,(name,description,price,quantity,category))
    print("product added successfuly")
    conn.commit()

def delete(id):
    query = "DELETE FROM products1 WHERE id = %s"
    c.execute(query,(id))
    print("Product deleted successfully")
    conn.commit()
    
def update(name,description,price,quantity,category):
    query = "UPDATE products1 WHERE id = %s"
    c.execute(query,(name,description,price,quantity,category))
    print("Product succesfulyy updated")
    conn.commit()

def all(category):
    query = "SELECT * FROM products1 WHERE category = %s"
    c.execute(query,(category))
    conn.commit()

def one(id):
    query = "SELECT * FROM products1 WHERE id = %s"
    results = c.fetchone()
    c.executemany(query(id),results)
    conn.commit()


def main():
    user = input("Press 1 to add a product\nPress 2 to delete product\nPress 3 to update\nPress 4 to retrieve all products\nPress 5 to view one product: ")
    if user == "1":
        name = input("Enter name of the product: ")
        description = input("Enter desrciption of the product: ")
        price = float(input("Enter price of the product: "))
        quantity = int(input("Enter quantity of the product: "))
        category = input("Enter the category of he product: ")
        add(name,description,price,quantity,category)

    elif user == "2":
        id = int(input("Enter id of the product: "))
        delete(id)

    elif user == "3":
        name = input("Enter name of the product: ")
        description = input("Enter desrciption of the product: ")
        price = float(input("Enter price of the product: "))
        quantity = int(input("Enter quantity of the product: "))
        category = input("Enter the category of he product: ")
        update(name,description,price,quantity,category)

    elif user == "4":
        category = input("Enter category: ")
        all(category)

    elif user == "5":
        id = int(input("Enter id of the product: "))
        one(id)

if __name__ == "__main__":
    main()
    c.close()
    conn.close()