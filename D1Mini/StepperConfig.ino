#include <Arduino.h>
#include <Stepper.h>

#define STEPS 2038 
Stepper stepper(STEPS, D5, D7, D6, D8);
const float resolution  = 2038;
float steps = 0; // up to 2038 steps
float stepSpeed = 6;
float maxSteps = 1041;

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  stepper.setSpeed(5); 
  stepper.step(-100); 
  delay(1000); 
}
