//Created by Siddharth Kumar Sah
//visit www.siddharthsah.com for more.


char incomingByte; //this is to select a variable for the incoming value of the serial
int x=0;
#define X_STEP_PIN         54  //pin selection
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN           2

#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN          18
#define Z_MAX_PIN          19

#define E_STEP_PIN         26
#define E_DIR_PIN          28
#define E_ENABLE_PIN       24

#define Q_STEP_PIN         36
#define Q_DIR_PIN          34
#define Q_ENABLE_PIN       30

#define SDPOWER            -1
#define SDSS               53
#define LED_PIN            13

#define FAN_PIN            9

#define PS_ON_PIN          12
#define KILL_PIN           -1

#define HEATER_0_PIN       10
#define HEATER_1_PIN       8
#define TEMP_0_PIN          13   // ANALOG NUMBERING
#define TEMP_1_PIN          14   // ANALOG NUMBERING

void setup() {   //outputs 

  pinMode(LED_PIN  , OUTPUT);
  
  pinMode(X_STEP_PIN  , OUTPUT);
  pinMode(X_DIR_PIN    , OUTPUT);
  pinMode(X_ENABLE_PIN    , OUTPUT);
  
  pinMode(Y_STEP_PIN  , OUTPUT);
  pinMode(Y_DIR_PIN    , OUTPUT);
  pinMode(Y_ENABLE_PIN    , OUTPUT);
  
  pinMode(Z_STEP_PIN  , OUTPUT);
  pinMode(Z_DIR_PIN    , OUTPUT);
  pinMode(Z_ENABLE_PIN    , OUTPUT);
  
  pinMode(E_STEP_PIN  , OUTPUT);
  pinMode(E_DIR_PIN    , OUTPUT);
  pinMode(E_ENABLE_PIN    , OUTPUT);
  
  pinMode(Q_STEP_PIN  , OUTPUT);
  pinMode(Q_DIR_PIN    , OUTPUT);
  pinMode(Q_ENABLE_PIN    , OUTPUT);
  
   digitalWrite(X_ENABLE_PIN    , LOW);  //set pins to start with low 
   digitalWrite(Y_ENABLE_PIN    , LOW);
   digitalWrite(Z_ENABLE_PIN    , LOW);
   digitalWrite(E_ENABLE_PIN    , LOW);
   digitalWrite(Q_ENABLE_PIN    , LOW);
   Serial.begin(9600);      //Serial starts at 9600 bauds
   Serial.write("Imaging tool 1.0 by Luis Oliver 2017");
}

void loop () {

  if (Serial.available() > 0) {    //seek serial
    
    incomingByte = Serial.read();   //incoming serial
     Serial.print("I received: ");
     Serial.println(incomingByte, DEC);  
    
    if(incomingByte == 'L') {
      Serial.print("I sent L ");
     for (x=0; x<133; x++){  //microsteps, for loop for moving the motors
     digitalWrite(Y_DIR_PIN    , HIGH);
     digitalWrite(Y_STEP_PIN    , HIGH);
    
      digitalWrite(Y_STEP_PIN    , LOW);
      delay(5);
     }
    }
    if(incomingByte == 'R') {
      Serial.print("I sent R ");
       for (x=0; x<133; x++){
      digitalWrite(Y_DIR_PIN    , LOW);
      digitalWrite(Y_STEP_PIN    , HIGH);
     
      digitalWrite(Y_STEP_PIN, LOW);
      delay(5);
    }
    }
    if(incomingByte == 'Q') {
      Serial.print("I sent Q ");
     for (x=0; x<500; x++){
     digitalWrite(X_DIR_PIN    , HIGH);
     digitalWrite(X_STEP_PIN    , HIGH);
     
      digitalWrite(X_STEP_PIN    , LOW);
      delay(1);
     }
    }
    if(incomingByte == 'W') {
      Serial.print("I sent W ");
       for (x=0; x<500; x++){
      digitalWrite(X_DIR_PIN    , LOW);
      digitalWrite(X_STEP_PIN    , HIGH);
      digitalWrite(X_STEP_PIN, LOW);
      delay(1);
    }
    }
    if(incomingByte == 'A') {
      Serial.print("I sent A");
     for (x=0; x<150; x++){
     digitalWrite(Q_DIR_PIN    , HIGH);
     digitalWrite(Q_STEP_PIN    , HIGH);
      digitalWrite(Q_STEP_PIN    , LOW);
      delay(2);
     }
    }
    if(incomingByte == 'S') {
      Serial.print("I sent S ");
       for (x=0; x<150; x++){
      digitalWrite(Q_DIR_PIN    , LOW);
      digitalWrite(Q_STEP_PIN    , HIGH);
      digitalWrite(Q_STEP_PIN, LOW);
      delay(2);
    }
    }  //start code part for Z&X for E_***_PIN 
    if(incomingByte == 'Z') {
      Serial.print("I sent Z ");
     for (x=0; x<500; x++){                    
     digitalWrite(E_DIR_PIN    , HIGH);
     digitalWrite(E_STEP_PIN    , HIGH);
      digitalWrite(E_STEP_PIN    , LOW);
      delay(1);
     }
    }
    if(incomingByte == 'X') {
      Serial.print("I sent X ");
       for (x=0; x<500; x++){
      digitalWrite(E_DIR_PIN    , LOW);
      digitalWrite(E_STEP_PIN    , HIGH);
      digitalWrite(E_STEP_PIN, LOW);
      delay(1);
    } //end code part for Z&X for E_***_PIN 

    }  //start code part for N&M for Z_***_PIN 
    if(incomingByte == 'N') {
      Serial.print("I sent N ");
     for (x=0; x<250; x++){                    
     digitalWrite(Z_DIR_PIN    , HIGH);
     digitalWrite(Z_STEP_PIN    , HIGH);
      digitalWrite(Z_STEP_PIN    , LOW);
      delay(1);
     }
    }
    if(incomingByte == 'M') {
      Serial.print("I sent M ");
       for (x=0; x<250; x++){
      digitalWrite(Z_DIR_PIN    , LOW);
      digitalWrite(Z_STEP_PIN    , HIGH);
      digitalWrite(Z_STEP_PIN, LOW);
      delay(1);
    } //end code part for N&M for Z_***_PIN 
    
    }
    delay(10);
  }  
}
 
  
