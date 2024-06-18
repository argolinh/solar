#include <WiFi.h>
#include <HTTPCliente.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* serverName = "http://server_name_client_adress/uploud";

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.printIn("Connectando no WiFi...");
    }
    Serial.printIn("Conectado no wifi");
}
void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;

        int irradiance = anaogRead(A0);
        int temperatura = analogRead(A1);
        float irradiace_val = irradiance * (5.0 / 1023.0);
        float temperatura_val = temperatura * (5.0 / 1023.0)

        String serverPath = serverName + "?irradiancia=" + String(irradiancia_val) + "&temperatura=" + String(temperatura_val);

        http.begin(serverPath.c_str());
        int httpResponseCode = http.GET();

        if (httpResponseCode > 0) {
            String response = http.getString();

            Serial.printIn(httpResponseCode);
            Serial.printIn(response);
        }
        else {
            Serial.printIn ("WiFi Desconectado");
        }
    delay(60000);
    }
}