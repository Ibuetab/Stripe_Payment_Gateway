#--------------------------------------------------------------------------------------------------------------------------------------
import os
import dotenv
import stripe


#--------------------------------------------------------------------------------------------------------------------------------------
#Configuracion del entorno
dotenv.load_dotenv() #Carga todas las variables de entorno

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

stripe.api_key = STRIPE_SECRET_KEY


#--------------------------------------------------------------------------------------------------------------------------------------
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



#--------------------------------------------------------------------------------------------------------------------------------------
#obtener el id de un cliente
def get_customer_id(email):
    customers = stripe.Customer.list(
        email=email,
        limit=1,
    )
    for customer in customers:
        return customer["id"]

#obtener el nombre de un cliente
def get_customer_name(client_id):
    pass



# Obtener el id de un producto
def get_product_id(name):
    product = stripe.Product.search(
       query = f"name:'{name}'"
       )
    return product["data"][0]["id"]
     

#--------------------------------------------------------------------------------------------------------------------------------------
# Creación de un metodo de pago
def create_payment_method() -> str:
    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={"token":"tok_visa"}
            
        )
        print(f"Metodo de pago creado con ID: {payment_method.id}")
        return payment_method.id

    except stripe.error.StripeError as e:
        print("error:")


#Asociar el método de pago a un cliente
def add_payment_method_to_user(client_id,payment_method_id):
    try:
        payment_method = stripe.PaymentMethod.attach(
            payment_method_id,
            customer=client_id,
        )
        print(f"Método de pago asociado correctamente al cliente con el ID: {payment_method.customer}")
    except stripe.error.StripeError as e:
        print("No se ha podido asociar el método de pago")


#--------------------------------------------------------------------------------------------------------------------------------------
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



