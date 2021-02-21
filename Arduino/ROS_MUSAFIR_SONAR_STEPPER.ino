#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif
#include <ros.h>

#define STEPPER_EN  9
#define STEPPER_DR  6
#define STEPPER_CK  7
#define STEPPER_STEPS 20
#define STEPPER_DELAY 1
#include <rosserial_arduino/Adc.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle nh;
rosserial_arduino::Adc adc_msg;
ros::Publisher p("sonar", &adc_msg);

void stepper_cb(const std_msgs::UInt16& step_msg){
  unsigned int a = step_msg.data;
  if(a>10 && a<20){
    digitalWrite(STEPPER_EN, LOW);
    digitalWrite(STEPPER_DR, LOW);
    for(int z=0; z<STEPPER_STEPS; z++){
      digitalWrite(STEPPER_CK, LOW);
      delay(STEPPER_DELAY);
      digitalWrite(STEPPER_CK, HIGH);
      delay(STEPPER_DELAY);      
    }
    digitalWrite(STEPPER_EN, HIGH);
  }else if(a>20 && a<30){
    digitalWrite(STEPPER_EN, LOW);
    digitalWrite(STEPPER_DR, HIGH);
    for(int z=0; z<STEPPER_STEPS; z++){
      digitalWrite(STEPPER_CK, LOW);
      delay(STEPPER_DELAY);
      digitalWrite(STEPPER_CK, HIGH);
      delay(STEPPER_DELAY);      
    }
    digitalWrite(STEPPER_EN, HIGH);
  }else{
    digitalWrite(STEPPER_EN, HIGH);  
  }
}
ros::Subscriber<std_msgs::UInt16> sub("step_signal", stepper_cb);

void setup()
{ 
  pinMode(STEPPER_EN, OUTPUT);
  pinMode(STEPPER_DR, OUTPUT);
  pinMode(STEPPER_CK, OUTPUT);

  digitalWrite(STEPPER_EN, HIGH);
  digitalWrite(STEPPER_DR, HIGH);
  digitalWrite(STEPPER_CK, HIGH);

  nh.initNode();
  nh.advertise(p);
  nh.subscribe(sub);
}

int averageAnalog(int pin){
  int v=0;
  for(int i=0; i<10; i++) v+= analogRead(pin);
  return v/10;
}
long adc_timer;

void loop()
{
  adc_msg.adc0 = averageAnalog(0);
  adc_msg.adc1 = averageAnalog(1);
  adc_msg.adc2 = averageAnalog(2);
  adc_msg.adc3 = averageAnalog(3);
  adc_msg.adc4 = averageAnalog(4);
  adc_msg.adc5 = averageAnalog(5);
  p.publish(&adc_msg);
  nh.spinOnce();
  delay(20);
}
