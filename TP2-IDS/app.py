
from flask import Flask, render_template
app = Flask(__name__)

info_evento =  {
1: {    "nombre": "Rally MTB 2025",  
        "organizador": "Club Social y Deportivo Unidos por el Deporte", 
        "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km ...", 
        "fecha": "24 de Octubre de 2025", 
        "horario": "8am", 
        "lugar": "Tandil, Buenos Aires", 
        "tipo_carrera": "MTB rural", 
        "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "1000"}, 
                            2: {"nombre": "Larga" ,"valor": "4000"}},      
        "Auspiciantes": ["ausp1","auspN"] }
}

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registration")
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="5002", debug=True)
