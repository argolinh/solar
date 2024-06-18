from flask import Flask, request
import pandas as pd
from datetime import datetime

app = Flask(__name__)
data = []

@app.route('/upload', methods=['GET'])
def upload_data():
    irradiancia = request.args.get('irradiancia')
    temperatura = request.args.get('temperatura')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data.append([timestamp, irradiancia, temperatura])
    
    # Criar DataFrame e salvar periodicamente
    if len(data) % 100 == 0:
        df = pd.DataFrame(data, columns=['Timestamp', 'Irradiancia', 'Temperatura'])
        df.to_csv('dados_painel.csv', index=False)
    
    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)