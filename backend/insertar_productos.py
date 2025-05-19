from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database("inventario")
productos_collection = db["productos"]

# Productos de prueba
productos = [
    {
        "nombre": "Croquetas para Perros Adultos",
        "descripcion": "Alimento balanceado para perros de razas medianas y grandes.",
        "precio": 45000,
        "stock": 20
    },
    {
        "nombre": "Arena para Gatos 10kg",
        "descripcion": "Arena aglomerante ultra absorbente sin aroma.",
        "precio": 30000,
        "stock": 50
    },
    {
        "nombre": "Juguete de Cuerda para Perros",
        "descripcion": "Resistente juguete masticable para razas medianas.",
        "precio": 12000,
        "stock": 15
    }
]

productos_collection.insert_many(productos)
print("✅ Productos insertados correctamente")