#include <EnableInterrupt.h>

#define SERIAL_PORT_SPEED 57600
#define RC_NUM_CHANNELS  6

#define RC_CH1  0
#define RC_CH2  1
#define RC_CH3  2
#define RC_CH4  3
#define RC_CH5  4
#define RC_CH6  5

#define RC_CH1_INPUT  7
#define RC_CH2_INPUT  8
#define RC_CH3_INPUT  9
#define RC_CH4_INPUT  10
#define RC_CH3_INPUT  11
#define RC_CH4_INPUT  12

uint16_t rc_values[RC_NUM_CHANNELS];
uint32_t rc_start[RC_NUM_CHANNELS];
volatile uint16_t rc_shared[RC_NUM_CHANNELS];

#define MOTOR_1_PWM   2
#define MOTOR_1_D1    24
#define MOTOR_1_D2    26

#define MOTOR_2_PWM   3
#define MOTOR_2_D1    28
#define MOTOR_2_D2    30

#define STEPPER_CK   4
#define STEPPER_DI   5
#define STEPPER_EN   6

void rc_read_values() {
  noInterrupts();
  memcpy(rc_values, (const void *)rc_shared, sizeof(rc_shared));
  interrupts();
}

void calc_input(uint8_t channel, uint8_t input_pin) {
  if (digitalRead(input_pin) == HIGH) {
    rc_start[channel] = micros();
  } else {
    uint16_t rc_compare = (uint16_t)(micros() - rc_start[channel]);
    rc_shared[channel] = rc_compare;
  }
}

void calc_ch1() { calc_input(RC_CH1, RC_CH1_INPUT); }
void calc_ch2() { calc_input(RC_CH2, RC_CH2_INPUT); }
void calc_ch3() { calc_input(RC_CH3, RC_CH3_INPUT); }
void calc_ch4() { calc_input(RC_CH4, RC_CH4_INPUT); }
void calc_ch5() { calc_input(RC_CH5, RC_CH5_INPUT); }
void calc_ch6() { calc_input(RC_CH6, RC_CH6_INPUT); }

void setup() {
  Serial.begin(SERIAL_PORT_SPEED);

  pinMode(RC_CH1_INPUT, INPUT);
  pinMode(RC_CH2_INPUT, INPUT);
  pinMode(RC_CH3_INPUT, INPUT);
  pinMode(RC_CH4_INPUT, INPUT);
  pinMode(RC_CH5_INPUT, INPUT);
  pinMode(RC_CH6_INPUT, INPUT);

  pinMode(MOTOR_1_PWM, OUTPUT);
  pinMode(MOTOR_1_D1, OUTPUT);
  pinMode(MOTOR_1_D2, OUTPUT);
  
  pinMode(MOTOR_2_PWM, OUTPUT);
  pinMode(MOTOR_2_D1, OUTPUT);
  pinMode(MOTOR_2_D2, OUTPUT);

  pinMode(STEPPER_CK, OUTPUT);
  pinMode(STEPPER_DI, OUTPUT);
  pinMode(STEPPER_EN, OUTPUT);

  enableInterrupt(RC_CH1_INPUT, calc_ch1, CHANGE);
  enableInterrupt(RC_CH2_INPUT, calc_ch2, CHANGE);
  enableInterrupt(RC_CH3_INPUT, calc_ch3, CHANGE);
  enableInterrupt(RC_CH4_INPUT, calc_ch4, CHANGE);
  enableInterrupt(RC_CH5_INPUT, calc_ch4, CHANGE);
  enableInterrupt(RC_CH6_INPUT, calc_ch4, CHANGE);
}

void loop() {
  rc_read_values();
  Serial.print("CH1:"); Serial.print(rc_values[RC_CH1]); Serial.print("\t");
  Serial.print("CH2:"); Serial.print(rc_values[RC_CH2]); Serial.print("\t");
  Serial.print("CH3:"); Serial.print(rc_values[RC_CH3]); Serial.print("\t");
  Serial.print("CH4:"); Serial.print(rc_values[RC_CH4]); Serial.print("\t");
  Serial.print("CH5:"); Serial.print(rc_values[RC_CH5]); Serial.print("\t");
  Serial.print("CH6:"); Serial.println(rc_values[RC_CH6]);
  delay(100);
}
