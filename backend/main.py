from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

# Cargar variables de entorno desde .env
load_dotenv()

app = FastAPI()

# CORS para permitir solicitudes del frontend Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajusta esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["inventario"]
productos_collection = db["productos"]

# Ruta de prueba
@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

# Ruta para obtener productos
@app.get("/productos")
def obtener_productos():
    productos = list(productos_collection.find({}, {"_id": 0}))  # sin _id para evitar errores
    return productos