from flask import Flask

app = Flask(__name__)

# Usamos el mismo HTML para mantener consistencia
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Flask</title>
    <style>
        body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: sans-serif; transition: 0.3s; }
        input, button { padding: 10px; margin: 10px; }
    </style>
</head>
<body>
    <input type="text" id="caja" placeholder="Escribe y presiona Enter">
    <button id="btn">Cambiar Colores</button>
    <script>
        document.getElementById('caja').onkeydown = (e) => { if(e.key === 'Enter') alert(e.target.value); };
        let s = 0;
        document.getElementById('btn').onclick = () => {
            s = (s + 1) % 3;
            const c = [['white','black'], ['black','white'], ['skyblue','red']];
            document.body.style.backgroundColor = c[s][0];
            document.body.style.color = c[s][1];
        };
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_content

if __name__ == '__main__':
    print("Servidor Python en http://localhost:5000")
    app.run(port=5000)