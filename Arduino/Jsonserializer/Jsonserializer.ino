
/*
   This Skecth is disigned for posting a json data adquired from a sensor connneted via NodeMCU or Rasberry Pi
   then, Posted it to a DJANGO Webapp running either locally or Hosted.
   This Sketch is built from several tutorial finded surfing the Web.
   See Reference below.
   Designed, and programmed by Ranger Geronimo.
   Created on : 2020-01-15
   Update  on : 2020-03-31
   Current Version:  3.0.1
   This example uses MPU6050, feel free to adacte to another kind of sensor.
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
#include <MPU6050.h>
#include <ArduinoJson.h>  // Must be ArduinoJson Version 6.0 o later

#define SERVER_IP "severIP"

//Network Credential
#define STASSID "wifiName"
#define STAPSK  "wifiPassword"

//variable for Wifi Connect
#define LED 2
#define on  false
#define off true

//global var to hold gathered temp
float temp;
float tempC;
float tempF;

void wifi_connect() {

  pinMode(LED, OUTPUT);
  digitalWrite(LED, off);
  WiFi.mode(WIFI_STA); // set the ESP8266 to be a WiFi-client
  WiFi.begin(STASSID, STAPSK);
  while (WiFi.status() != WL_CONNECTED) {

    Serial.printf("Trying to connet to: ");
    Serial.println(STASSID);
    blink();
  }

  Serial.print("Conneted  to: ");
  Serial.println(STASSID);
  Serial.print("Ip Address: ");
  Serial.println(WiFi.localIP());
}


void blink() {

  digitalWrite(LED, off);
  delay(100);
  digitalWrite(LED, on);
  delay(100);
}

MPU6050 object;

void setup()  {
  // uncomment if your planning use Arduino Serial Monitor
  Serial.begin(115200);
  while (!Serial) continue; // Wait for Serial port.

  while (!object.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
  }
  // Connect to wifi Network
  wifi_connect();

}


void loop() {

  // Allocate a temporary memory for JsonDocument
  const size_t capacity = JSON_ARRAY_SIZE(12) + JSON_OBJECT_SIZE(3) + 50;
  DynamicJsonDocument doc(capacity);

  //Add values in the document
  doc["name"] = "ds18b20";
  doc["kind"] = "temperature";

  // Create the "values" array to hold sensor reading and add to doc object.
  JsonArray Values = doc.createNestedArray("values");

  //  Gather Sensor temperature Values
  for (int pin = 1; pin < 10; pin++) {
    temp = object.readTemperature();
    Values.add(temp);

  }

  //  Start Posting Request
  WiFiClient client;
  HTTPClient http;

  if ((WiFi.status() == WL_CONNECTED)) {

    Serial.printf("[HTTP] begin...\n");

    http.begin(client, "http://" SERVER_IP "/sensor/"); // Begin HTTP Resquest
    http.addHeader("content-Type", "application/json");   //  Specify Type of Header in HTTP Resquest (POST)

    String postData; // String to encode Json document

    serializeJson(doc, postData);

    int post = http.POST(postData);     //Send POST request

    if (post > 0) {
      Serial.printf("[HTTP] POST code: %d\n", post);

      //       file found at server
      if (post == HTTP_CODE_OK) {
        const String& payload = http.getString();
        Serial.print("received payload:\n<<");
        Serial.println(payload); // Response returned for Web App
        Serial.println(">>");
      }

    } else {
      Serial.printf("[HTTP] POST failed, error: %s\n", http.errorToString(post).c_str());
    }

    http.end();  // Close connection to relase resources

  }

  delay(5000); //  Delay before next Hppt Post request

}


/*
   https://techtutorialsx.com/2016/07/21/esp8266-post-requests
   https://techtutorialsx.com/2017/01/07/flask-parsing-json-data
   https://github.com/esp8266/Arduino/tree/master/libraries/ESP8266HTTPClient/examples/PostHttpClient
*/
