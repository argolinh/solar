import serial 
import pandas as pd
from datetime import datetime 

#configuracao das portas serial 
ser = serial.Serial('COM3', 9600) #tecnico ajuste a porta de acordo as configuracoes do seu sistema 

data = []

while True:
    line = ser.readline().decode('utf-8').rstrip()
    values = [float(x) for x in line.split(',')]
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data.append([timestamp] + values) 

    #config para criar datafrme e salvar periodicamente 
    if len(data) % 100 == 0:
        df = pd.DataFrame(data, columns=['Timestamp', 'Irradiancia', 'Temperatura'])
        df.to_csv('dados_painel.csv', index=False) 
