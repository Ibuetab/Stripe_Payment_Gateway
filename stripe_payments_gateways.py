import os
import dotenv
import stripe


#Configuracion del entorno
dotenv.load_dotenv() #Carga todas las variables de entorno

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

stripe.api_key = STRIPE_SECRET_KEY


#Creación de un cliente
def create_user(name,email):
    try:
        client = stripe.Customer.create(
            name=name,
            email=email,
            
        )
        
        print(f"cliente creado correctamente con el ID: {client.id} Nombre de usuario: {client.name} Email: {client.email}")
        return client.id #Devuelve el id del cliente creado
    
    except stripe.error.StripeError as e:
        print("No se ha podido crear el cliente")


#Creación de un producto
def create_product(name,description):

    try:
        product = stripe.Product.create(
            name=name,
            description=description
        )
        print(f"Producto creado correctamente con el ID {product.id}")

    except stripe.error.StripeError as e:
        print("No se ha podido crear el producto")






#obtener el id de un cliente
def get_customer_id(email):
    customers = stripe.Customer.list(
        email=email,
        limit=1,
    )
    for customer in customers:
        return customer["id"]




# Obtener el id de un producto
def get_product_id():
    products = stripe.Product.list(
       
        limit=3,
    )
    for product in products:
        return product["id"]
     



""" 
# Obtener el precio de un producto 
def get_products_price(product_id):
    stripe.Price.list(
        product = product_id,
        limit=1
    )
    price_id = price["data"][0]["id"],
    amount = price["data"][0]["unit_amount"],
    #currency= price["data"][0]["currency"],


    return price_id, amount



# Crear un metodo de pago
def create_payment_method() -> str:
    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={"token":"tok_visa"}
            

        )
        print(f"Metodo de pago creado con ID: {payment_method.id}")
        print(payment_method)
        return payment_method.id

    except stripe.error.StripeError as e:
        print("error:")

        


#Crear un pago

def create_payment(client_id:str,payment_method_id:str,amount:int, currency:str):

    try:
        payment = stripe.PaymentIntent.create(
                amount= 5 *100,
                currency="usd", #dolar americano
                payment_method=payment_method_id,
                payment_method_types=["card"],
                customer=client_id,
                

                confirm=True
    )
        
    
    except stripe.error.CardError as e:
        print("Error en la creacion del pago")
        print(e)
    except stripe.error.StripeError as e:
        print("Error en la creacion del pago")
        print(e)





def add_payment_method_to_user(client_id,payment_method_id):
    stripe.PaymentMethod.attach(
        payment_method_id,
        customer=client_id,
    )





#payment_method_id = create_payment_method()
#create_payment(payment_method_id)

#client_id=create_user("assaa","asaasas@gmail.com")
#payment_method_id = create_payment_method()
#add_payment_method_to_user(client_id, payment_method_id)

#product_id = get_product()
#price_id, amount, currency = get_products_price(product_id)


"""

#create_user("bbb","bbb@gmail.com")
#create_product("Producto 2","Descripcion del producto 2") 
product_id=get_product_id()
#customer_id = get_customer_id("bbb@gmail.com")
print(product_id)
