from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Usuarios import Usuario
from admins import admin
from Canciones import Song
app = Flask(__name__)
CORS(app)

Usuarios = []
Admins = []
Canciones = []
contCanciones = 0
Admins.append(admin('Usuario','Maestro','admin','admin'))
Usuarios.append(Usuario('Usuario','normal','user','1234'))
@app.route('/',methods=['GET'])
def rutaIncial():
    return("Hola Jeje")

@app.route('/Users',methods=['GET'])
def mostrarUsers():
    global Usuarios
    Datos = []
    for user in Usuarios:
        Dato = {
            'nombre': user.getNombre(),
            'apellido': user.getApellido(),
            'username': user.getUsername(),
            'password': user.getPassword()
        }
        Datos.append(Dato)
    res = jsonify(Datos)
    return(res)

@app.route('/Users/<string:nombre>', methods=['GET'])
def mostrarUser(nombre):
    global Usuarios
    for user in Usuarios:
        if user.getUsername() == nombre:
            Dato = {
                'nombre': user.getNombre(),
                'apellido': user.getApellido(),
                'username': user.getUsername(),
                'password': user.getPassword()
            }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/UsersAdmin',methods=['GET'])
def mostrarUsersAdmin():
    global Admins
    Datos = []
    for a in Admins:
        Dato = {
            'nombre': a.getNombre(),
            'apellido': a.getApellido(),
            'username': a.getUsername(),
            'password': a.getPassword()
        }
        Datos.append(Dato)
    res = jsonify(Datos)
    return(res)

@app.route('/Users/<string:nombre>', methods=['PUT'])
def modificarUsuario(nombre):
    global Usuarios
    for i in range(len(Usuarios)):
        if nombre == Usuarios[i].getUsername():
            Usuarios[i].setNombre(request.json['nombre'])
            Usuarios[i].setApellido(request.json['apellido'])
            Usuarios[i].setUsername(request.json['username'])
            Usuarios[i].setPassword(request.json['password'])
            Dato = {
                'message':'Success'
            }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/Users/<string:nombre>', methods=['DELETE'])
def EliminarUsuario(nombre):
    global Usuarios
    for i in range(len(Usuarios)):
        if nombre == Usuarios[i].getUsername():
            del Usuarios[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})

@app.route('/login', methods=['POST'])
def loguear():
    global Usuarios
    nombreUsuario = request.json['usuario']
    contra = request.json['password']
    for user in Usuarios:
        if user.getUsername() == nombreUsuario and user.getPassword() == contra:
            Dato = {
                'message':'Success',
                'usuario': user.getUsername()
            }
            break
        else:
            Dato = {
                'message': 'Failed',
                'usuario': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/loginAdmin', methods=['POST'])
def loguearAdmin():
    global Admins
    nombreUsuario = request.json['usuario']
    contra = request.json['password']
    for adm in Admins:
        if adm.getUsername() == nombreUsuario and adm.getPassword() == contra:
            Dato = {
                'message':'Success',
                'usuario': adm.getUsername()
            }
            break
        else:
            Dato = {
                'message': 'Failed',
                'usuario': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)
    
@app.route('/Register', methods=['POST'])
def registrar():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['username']
    password = request.json['password']
    confirmPass = request.json['confirmPass']
    encontrado = False
    for user in Usuarios:
        if user.getUsername() == username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })
    else:
        if nombre!= "" and apellido != "" and username != "" and password != "":
            if password == confirmPass:
                nuevo = Usuario(nombre,apellido,username,password)
                Usuarios.append(nuevo)
                return jsonify({
                    'message':'Success',
                    'reason':'Se agrego el usuario'
                    })
            else:
                return jsonify({
                    'message':'FailPass',
                    'reason':'Contraseñas no iguales'
                })
        else:
            return jsonify({
                'message':'FailField',
                'reason':'Llene los campos'
            })

@app.route('/RegisterAdmin', methods=['POST'])
def registrarAdmin():
    global Admins
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['username']
    password = request.json['password']
    confirmPass = request.json['confirmPass']
    encontrado = False
    for a in Admins:
        if a.getUsername() == username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })
    else:
        if nombre!= "" and apellido != "" and username != "" and password != "":
            if password == confirmPass:
                nuevo = admin(nombre,apellido,username,password)
                Admins.append(nuevo)
                return jsonify({
                    'message':'Success',
                    'reason':'Se agrego el usuario'
                    })
            else:
                return jsonify({
                    'message':'FailPass',
                    'reason':'Contraseñas no iguales'
                })
        else:
            return jsonify({
                'message':'FailField',
                'reason':'Llene los campos'
            })

@app.route('/Cancion', methods=['POST'])
def guardarCancion():
    global Canciones, contCanciones
    id = contCanciones
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    nuevo = Song(id, nombre, artista, album, fecha, imagen, spotify, youtube)
    Canciones.append(nuevo)
    contCanciones += 1
    return jsonify({
            'message':'Success',
            'reason':'Cancion Agregada'
            })

@app.route('/Cancion/<int:id>', methods=['PUT'])
def modificarCancion(id):
    global Canciones
    for i in range(len(Canciones)):
        if id == Canciones[i].getId():
            Canciones[i].setId(request.json['id'])
            Canciones[i].setNombre(request.json['nombre'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha'])
            Canciones[i].setImagen(request.json['imagen'])
            Canciones[i].setSpotify(request.json['spotify'])
            Canciones[i].setYoutube(request.json['youtube'])
            Dato = {
                'message':'Success'
            }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/Cancion', methods=['GET'])
def obtenerCanciones():
    global Canciones, contCanciones
    Datos = []
    for cancion in Canciones:
        Dato = {
            'id': cancion.getId(),
            'nombre': cancion.getNombre(),
            'artista': cancion.getArtista(),
            'album': cancion.getAlbum(),
            'fecha': cancion.getFecha(),
            'imagen': cancion.getImagen(),
            'spotify': cancion.getSpotify(),
            'youtube': cancion.getYoutube()     
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Cancion/<int:id>', methods=['DELETE'])
def EliminarCancion(id):
    global Canciones
    for i in range(len(Canciones)):
        if id == Canciones[i].getId():
            del Canciones[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})

if __name__ =="__main__":
    app.run(port=3000, debug=True)

