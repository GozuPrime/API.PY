from app import create_app

app=create_app()

# LA IP ES DE TU MAQUINA (192.168.1.X)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)