import pandas as pd
from datetime import datetime
import serial  # Certifique-se de ter pyserial instalado: pip install pyserial

# Configurar a porta serial 
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Modifique para a porta correta

data = []

try:
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        values = [float(x) for x in line.split(',')]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data.append([timestamp] + values)

        # Criar frame e salvar periodicamente
        if len(data) % 100 == 0:
            df = pd.DataFrame(data, columns=['Timestamp', 'Irradiancia', 'Temperatura', 'Corrente', 'Tensao'])
            df.to_csv('dados_painel.csv', index=False)
except KeyboardInterrupt:
    # Salvar os dados restantes quando o loop for interrompido
    df = pd.DataFrame(data, columns=['Timestamp', 'Irradiancia', 'Temperatura', 'Corrente', 'Tensao'])
    df.to_csv('dados_painel.csv', index=False)
    print("Programa interrompido e dados salvos.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    ser.close()
