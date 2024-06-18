void setup() {
    Serial.bengin(9600);
    // configurar os pinos dos sensores
    pinMode (A0, INPUT); //ex pino de sensor de irradiancia 
    pinMode (A1, INPUT); //ex pino de sensor de temperaura
}

void loop() {
    int irradiancia = analogRead(A0);
    int temperatura = analogRead(A1);
    //tecnico resposavel se necessario converta os valores
    float irradiancia_val = irradiancia * (5.0 / 1023.0); //conversao
    float temperatura_val = temperatura * (5.0 / 1023.0); //conversao

        //enviar valores via serial 
        Serial.print(irradiancia_val);
        Serial.print(",");
        Serial.printIn(Temperatura_val)
        
        delay(1000); //aguardar um segundo antes de ler novamente
}