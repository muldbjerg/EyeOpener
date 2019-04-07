// SOURCES //
// Wifi: https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266WiFi/examples/WiFiMulti/WiFiMulti.ino#L19
// Neopixel: https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-installation
// HTTP: https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266HTTPClient/examples/BasicHttpClient/BasicHttpClient.ino?fbclid=IwAR0hTAOelyxZTGd1pzfUUWlqTAh0rdpUQ5FBsAEqvnhTdGz-8YAsWpyTCTo
// Stepper: https://www.mschoeffler.de/2017/09/23/tutorial-how-to-drive-the-28byj-48-stepper-motor-with-a-uln2003a-driver-board-and-an-arduino-uno/?fbclid=IwAR1qXiZzCyqgnEUxvtUxFYA07hZXBwNxbWw3C31q1Nt88qV5wGTIQnap3aI

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <ESP8266HTTPClient.h>

#include <WiFiClient.h>
#include <Adafruit_NeoPixel.h>

#include <Stepper.h>

#include <ArduinoJson.h>

// Wifi
char wifi_ssid[] = "Pixel_3570";
char wifi_password[] = "Ninna123";
ESP8266WiFiMulti wifiMulti;

// Http
WiFiClient client;
HTTPClient http;
char url[] = "http://192.168.43.252:9090/api/accumulated/04/7";
char statusUrl[] = "http://192.168.43.252:9090/api/simulator";
String payload;
String diffPayload;
String postPayload;
float totalSteps = 0;
float previousUse = 0;

// Neopixels
const int neopixelPin = D4;
const int numberOfPixels = 40;
Adafruit_NeoPixel strip = Adafruit_NeoPixel(numberOfPixels, neopixelPin, NEO_GRB + NEO_KHZ800);
int warmColor = strip.Color(255,70,10);
int coldColor = strip.Color(255,255,255);
int neutralColor = strip.Color(255, 100, 30);
int hellColor = strip.Color(255, 20, 0);
int color =  neutralColor;

// Stepper
#define STEPS 2038 
Stepper stepper(STEPS, D5, D7, D6, D8);
const float resolution  = 2038;
float steps = 0; // up to 2038 steps
float stepSpeed = 6;
float maxSteps = 1041;

// Millis delay
unsigned long previousMillis = 0;
const long requestInterval = 2000;

// SETUP //
void setup() {
  Serial.begin(115200);

  // Neopixel
  strip.begin();
  strip.setPixelColor(0,color);
  strip.show();

  // Wifi
  WiFi.mode(WIFI_STA);
  wifiMulti.addAP(wifi_ssid, wifi_password);
  connectToWifi();

  // Stepper
  updateStepper();
}

// LOOP //
void loop() {  
  unsigned long currentMillis = millis();
  if (wifiMulti.run() == WL_CONNECTED) {
    if (currentMillis - previousMillis >= requestInterval) {
      previousMillis = currentMillis;
      httpGet();
      httpGetStatus();
      checkStatus();
      //httpPost();
      processData();
    }
  }
  else {
    Serial.println("lost WiFi connection...");
    delay(100);
    connectToWifi();
  }
  delay(1000);
}

// METHODS //
void connectToWifi(){
    int printCounter = 0;
    
    while(wifiMulti.run() != WL_CONNECTED) {
       printCounter ++;
       if(printCounter == 1){
         Serial.println("Connecting to wifi...");
       }
       delay(50);
   }
   if(printCounter > 0){
     Serial.println ("Connected to network " + String(wifi_ssid));
   }    
}

void updateLight(){
  Serial.println("updateLight()");
  strip.fill(color, 0, numberOfPixels);
  strip.show();
}

void updateStepper(){
  Serial.println("updateStepper()");
  Serial.println("stepSpeed: " + String(stepSpeed));
  Serial.println("Steps: " + String(steps));
  stepper.setSpeed(stepSpeed);
  stepper.step(steps);
}

void httpGet(){
  Serial.print("[HTTP] begin...\n");
  if (http.begin(client, url)) {  // HTTP

  Serial.print("[HTTP] GET...\n");
  // start connection and send HTTP header
  int httpCode = http.GET();
  
  // httpCode will be negative on error
  if (httpCode > 0) {
    // HTTP header has been send and Server response header has been handled
    Serial.printf("[HTTP] GET... code: %d\n", httpCode);
     
    // file found at server
    if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
      payload = http.getString();
      Serial.println(payload);
    }
    
  } else {
    Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }
  
  http.end();
      
  } else {
    Serial.printf("[HTTP} Unable to connect\n");
  }
}

void httpGetStatus(){
  Serial.print("[HTTP] begin...\n");
  if (http.begin(client, statusUrl)) {  // HTTP

  Serial.print("[HTTP] GET...\n");
  // start connection and send HTTP header
  int httpCode = http.GET();
  
  // httpCode will be negative on error
  if (httpCode > 0) {
    // HTTP header has been send and Server response header has been handled
    Serial.printf("[HTTP] GET... code: %d\n", httpCode);
     
    // file found at server
    if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
       diffPayload = http.getString();
      
    }
    
  } else {
    Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }
  
  http.end();
      
  } else {
    Serial.printf("[HTTP} Unable to connect\n");
  }
}

void httpPost(){
  Serial.print("[HTTP] begin...\n");
  if (http.begin(client, statusUrl)) {  // HTTP

  Serial.print("[HTTP] POST...\n");
  // start connection and send HTTP header
  http.addHeader("Content-Type", "application/json");
  DynamicJsonDocument doc(1024);

  doc["command"] = "status";
  int httpCode = http.POST("{\"command\":\"run\"}");
  
  // httpCode will be negative on error
  if (httpCode > 0) {
    // HTTP header has been send and Server response header has been handled
    Serial.printf("[HTTP] POST... code: %d\n", httpCode);
     
    // file found at server
    if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
      diffPayload = http.getString();
    }
    
  } else {
    Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }
  
  http.end();
      
  } else {
    Serial.printf("[HTTP} Unable to connect\n");
  }  
}

void processData(){
  DynamicJsonDocument doc(1024);
  deserializeJson(doc, payload);
  
  float use = doc["todaysUse"];
  float balance = doc["balance"];
  int increase = doc["increase"];
  int stepper = doc["stepper"];

  /*if(use < previousUse){
    resetLamp();
    startService();
    
  }*/
  
  if(use == previousUse){
    return;
    
  }else if(!(totalSteps >= maxSteps)){
    steps = stepper;
    totalSteps += steps;
    Serial.println("");
    Serial.println("totalSteps: " + String(totalSteps));
    Serial.println("increase: " + String(increase));
    Serial.println("steps: " + String(steps));
    Serial.println("balance: " + String(balance));
  
    if(balance > 60){
      color = warmColor;
    }
    if(balance <= 60 && balance >= 40){
      color = neutralColor;
    }
    if(balance < 40){
      color = coldColor;
    }
  }else{
    steps = 0;
    color = hellColor;
  }
  previousUse = use;
  updateLight();
  updateStepper();
}

void checkStatus(){
  DynamicJsonDocument doc(1024);
  deserializeJson(doc, diffPayload);
  
  String status = doc["Simulator status"];
  String running = doc["Running"];
  Serial.println("Status: " + status);
  Serial.println("Running: " + running);
  if (status == "active"){
    diffPayload = "";
    status = "";
    resetLamp();
    
    startService();
  }
}

void resetLamp(){
   color = neutralColor;
   updateLight();
   
   stepSpeed = 16;
   steps = totalSteps*-1;
   updateStepper();
   color = neutralColor;
   delay(3000);
}

void startService(){
  
  httpPost();
  stepSpeed = 6;
  steps = 0;
  totalSteps = 0;
}
