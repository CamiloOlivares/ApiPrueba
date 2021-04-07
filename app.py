from flask import Flask,jsonify,request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

from pokemons import pokemons
from pokemons import perfil
from pokemons import horario

@app.route('/ping')
def ping():
    return jsonify({"ok":True,"message":"hola"})

@app.route('/pokemones')
def pokemones():
    return jsonify({"ok":True,"pokemons":pokemons}),200

@app.route('/cambiarPokemon',methods=['POST'])
def cambiarPokemon():
    print(request.get_data())
    # return jsonify({"ok":True,"message":"Pokemon ingresado correctamente","pokemons":pokemons})
    return jsonify({"data":request.form.getlist('tamano')})

@app.route('/returnput',methods=['PUT'])
def returnput():
    return jsonify({"ok":True,"message":"este es un put"}) 

@app.route('/getPerfil',methods=['POST'])
def getperfil():
    return jsonify(perfil[0])

@app.route('/getHorario',methods=['POST'])
def gethorario():
    return jsonify(horario)     
       
if __name__=='__main__':
    app.run(debug=True, port=4000)


