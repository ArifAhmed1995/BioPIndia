//Created by Siddharth Kumar Sah
//visit www.siddharthsah.com for more.
int x=0;
int i;
byte ib1;
byte ib2;
int incoming_signal;
int stepper_delay=5000;
char buffer[] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};// 8

int x_stepper_iter;
int y_stepper_iter;
int z_stepper_iter;

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

void setup()
{   //outputs
  pinMode(LED_PIN  , OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
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

void loop ()
{
  if (Serial.available() > 0)
  {
    Serial.readBytes(buffer, 2);
    incoming_signal = atoi(buffer);

    // 01 - Fan On
    if(incoming_signal == 1)
    {
      digitalWrite(FAN_PIN, HIGH);
    }// 02 - Fan Off
    else if(incoming_signal == 2)
    {
      digitalWrite(FAN_PIN, LOW);
    }

    // 03 - Y forward/DIR_PIN : HIGH
    if(incoming_signal == 3)
    {
        Serial.readBytes(buffer, 8);   
        y_stepper_iter = atoi(buffer);
       for (x=0; x<y_stepper_iter; x++)
       {  //microsteps, for loop for moving the motors
          digitalWrite(LED_BUILTIN, LOW);
          digitalWrite(Y_DIR_PIN    , HIGH);
          digitalWrite(Y_STEP_PIN    , HIGH);
          digitalWrite(Y_STEP_PIN    , LOW);
          delayMicroseconds(stepper_delay);
          digitalWrite(LED_BUILTIN, HIGH);
       }
    }// 04 - Y backward/ DIR_PIN : LOW
    else if(incoming_signal == 4)
    {
        Serial.readBytes(buffer, 8);   
        y_stepper_iter = atoi(buffer);
       for (x=0; x<y_stepper_iter; x++)
       {  //microsteps, for loop for moving the motors
          digitalWrite(Y_DIR_PIN    , LOW);
          digitalWrite(Y_STEP_PIN    , HIGH);
          digitalWrite(Y_STEP_PIN    , LOW);
          delayMicroseconds(stepper_delay);
       }
    }// 05 - X forward/ DIR_PIN : HIGH
    else if(incoming_signal == 5)
    {
        Serial.readBytes(buffer, 8);   
        x_stepper_iter = atoi(buffer);

        for (x=0; x<x_stepper_iter; x++)
        {
            digitalWrite(X_DIR_PIN    , HIGH);
            digitalWrite(X_STEP_PIN    , HIGH);
            digitalWrite(X_STEP_PIN    , LOW);
            delayMicroseconds(stepper_delay/5);
        }
    }// 06 - X backward/ DIR_PIN : LOW
    else if(incoming_signal == 6)
    {
        Serial.readBytes(buffer, 8);   
        x_stepper_iter = atoi(buffer);
       
        for (x=0; x<x_stepper_iter; x++)
        {
            digitalWrite(X_DIR_PIN    , LOW);
            digitalWrite(X_STEP_PIN    , HIGH);
            digitalWrite(X_STEP_PIN    , LOW);
            delayMicroseconds(stepper_delay/5);
        }
    }// 07 - Z forward/ DIR_PIN : HIGH
    else if(incoming_signal == 7)
    {
        Serial.readBytes(buffer, 8);   
        z_stepper_iter = atoi(buffer);

       for (x=0; x<z_stepper_iter; x++)
       {
          digitalWrite(Z_DIR_PIN    , HIGH);
          digitalWrite(Z_STEP_PIN    , HIGH);
          digitalWrite(Z_STEP_PIN, LOW);
          delayMicroseconds(stepper_delay/5);
       }
    }// 08 - Z backward/ DIR_PIN : LOW
    else if(incoming_signal == 8)
    {
        Serial.readBytes(buffer, 8);   
        z_stepper_iter = atoi(buffer);

       for (x=0; x<z_stepper_iter; x++)
       {
          digitalWrite(Z_DIR_PIN    , LOW);
          digitalWrite(Z_STEP_PIN    , HIGH);
          digitalWrite(Z_STEP_PIN, LOW);
          delayMicroseconds(stepper_delay/5);
       }
    }// 09 - Change delayMicroseconds Time(Increase FeedRate)
    else if(incoming_signal == 9)
    {
        Serial.readBytes(buffer, 8);
        stepper_delay = atoi(buffer);
    }
    delayMicroseconds(stepper_delay * 2);
  }
}
