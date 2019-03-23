#include <Adafruit_Sensor.h>            //Header files
#include <DHT.h>
#include <DHT_U.h>
#include <stdarg.h>
#include <Arduino.h>

#ifndef ARDPRINTF                       //Definitions for ardprintf
#define ARDPRINTF
#define ARDBUFFER 16

#define DHTPIN1     A4                  //DHT sensor 1 at pin A4
#define DHTPIN2     A5                  //DHT sensor 2 at pin A5
#define DHTTYPE     DHT11
DHT S1(DHTPIN1, DHTTYPE);
DHT S2(DHTPIN2, DHTTYPE);

String element;                         //To manipulate heating/cooling elements and motors
int ceo = 0, heo = 0;                   //To manipulate status of elements
float gas;                              //To manipulate sensor data
float temp1, temp2, tmax;
float tset = 30;
float tol = 1;
float humidity1, humidity2;

void setup() 
{
    Serial.begin(9600);
    pinMode(3,OUTPUT);                  //Stepper at pin 3
    pinMode(4,OUTPUT);                  //Stepper at pin 4
    pinMode(A0,INPUT);                  //Smoke sensor at pin A0
    pinMode(22,OUTPUT);                 //Cooling element at pin 22
    pinMode(23,OUTPUT);                 //Heating element at pin 23
    pinMode(30,OUTPUT);                 //Temperature sensor 1 LED at pin 30
    pinMode(31,OUTPUT);                 //Temperature sensor 2 LED at pin 31
    pinMode(32,OUTPUT);                 //Humidity sensor 1 LED at pin 32
    pinMode(33,OUTPUT);                 //Humidity sensor 2 LED at pin 33
    pinMode(34,OUTPUT);                 //Gas sensor LED at pin 34
    pinMode(35,OUTPUT);                 //Motor Up LED at pin 35
    pinMode(36,OUTPUT);                 //Motor Down LED at pin 36
    pinMode(37,OUTPUT);                 //Heating element LED at pin 37
    pinMode(38,OUTPUT);                 //Cooling element LED at pin 38
    pinMode(50,OUTPUT);                 //Buzzer at pin 50
}

void loop() 
{
    gas = analogRead(A0);                   //Manipulating gas sensor
    if (gas>0)
    {
        digitalWrite(34,HIGH);
    }
    else
    {
        digitalWrite(34,LOW);
    }
    if(gas>400)
    {
        digitalWrite(50,HIGH);
    }
    else
    {
        digitalWrite(50,LOW);
    }

    temp1 = S1.readTemperature();             //Manipulating temperature sensors
    temp2 = S2.readTemperature();
    if (temp1>0)
    {
        digitalWrite(30,HIGH);
    }
    else
    {
        digitalWrite(30,LOW);
    }
    if (temp2>0)
    {
        digitalWrite(31,HIGH);
    }
    else
    {
        digitalWrite(31,LOW);
    }
    tmax = max(temp1,temp2);

    humidity1 = S1.readHumidity();            //Manipulating humidity sensors
    humidity2 = S2.readHumidity();
    if (humidity1>0)
    {
        digitalWrite(32,HIGH);
    }
    else
    {
        digitalWrite(32,LOW);
    }

    if (humidity2>0)
    {
        digitalWrite(33,HIGH);
    }
    else
    {
        digitalWrite(33,LOW);
    }

    ardprintf("%f %f %f %f %f %f", gas, temp1, temp2, tmax, humidity1, humidity2);

    if (Serial.available())
    {
        element = Serial.readString();
    }

    if (element == "CEON")                   //Manipulating heating/cooling element
    {
        digitalWrite(22,HIGH);
        digitalWrite(38,HIGH);
        ceo = 1;
    }
    else if (element == "CEOFF")
    {
        digitalWrite(22,LOW);
        digitalWrite(38,LOW);
        ceo = 0;
    }
    else if (element == "HEON")
    {
        digitalWrite(23,HIGH);
        digitalWrite(37,HIGH);
        heo = 1;
    }
    else if (element == "HEOFF")
    {
        digitalWrite(23,LOW);
        digitalWrite(37,LOW);
        heo = 0;
    }

    if (abs(tmax-tset) <= tol)
    {
        digitalWrite(22,LOW);
        digitalWrite(23,LOW);
        digitalWrite(37,LOW);
        digitalWrite(38,LOW);
    }
    else if ((tmax<tset) && (heo == 0))
    {
        digitalWrite(22,LOW);
        digitalWrite(23,HIGH);
        digitalWrite(37,HIGH);
        digitalWrite(38,LOW);
    }
    else if (ceo == 0)
    {
        digitalWrite(22,HIGH);
        digitalWrite(23,LOW);
        digitalWrite(37,LOW);
        digitalWrite(38,HIGH);
    }

    else if (element == "UPHigh")            //Manipulating motors
    {
        digitalWrite(4,HIGH);
        for(int x = 0; x < 4500; x++)
        {
            digitalWrite(3,HIGH);
            delayMicroseconds(500);
            digitalWrite(3,LOW);
            delayMicroseconds(500);
            digitalWrite(35,HIGH);
        }
        digitalWrite(35,LOW);
    }
    else if (element == "UPMedium")
    {
        digitalWrite(4,HIGH);
        for(int x = 0; x < 3000; x++)
        {
            digitalWrite(3,HIGH);
            delayMicroseconds(500);
            digitalWrite(3,LOW);
            delayMicroseconds(500);
            digitalWrite(35,HIGH);
        }
        digitalWrite(35,LOW);
    }
    else if (element == "UPLow")
    {
        digitalWrite(4,HIGH);
        for(int x = 0; x < 1500; x++)
        {
            digitalWrite(3,HIGH);
            delayMicroseconds(500);
            digitalWrite(3,LOW);
            delayMicroseconds(500);
            digitalWrite(35,HIGH);
        }
        digitalWrite(35,LOW);
    }
    else if (element == "DOWNHigh")
    {
        digitalWrite(4,LOW);
        for(int x = 0; x < 4500; x++)
        {
            digitalWrite(3,HIGH);
            delayMicroseconds(500);
            digitalWrite(3,LOW);
            delayMicroseconds(500);
            digitalWrite(36,HIGH);
        }
        digitalWrite(36,LOW);
    }
    else if (element == "DOWNMedium")
    {
        digitalWrite(4,LOW);
        for(int x = 0; x < 3000; x++)
        {
            digitalWrite(3,HIGH);
            delayMicroseconds(500);
            digitalWrite(3,LOW);
            delayMicroseconds(500);
            digitalWrite(36,HIGH);
        }
        digitalWrite(36,LOW);
    }
    else if (element == "DOWNLow")
    {
        digitalWrite(4,LOW);
        for(int x = 0; x < 1500; x++)
        {
            digitalWrite(3,HIGH);
            delayMicroseconds(500);
            digitalWrite(3,LOW);
            delayMicroseconds(500);
            digitalWrite(36,HIGH);
        }
    digitalWrite(36,LOW);
    }

    delay(500);
}

int ardprintf(char *str, ...)
{
    int i, count = 0, j = 0, flag = 0;
    char temp[ARDBUFFER+1];
    for(i = 0; str[i] != '\0';i++)
        if(str[i] == '%')
            count++;
    va_list argv;
    va_start(argv, count);
    for(i = 0,j = 0; str[i] != '\0';i++)
    {
        if(str[i] == '%')
        {
            temp[j] = '\0';
            Serial.print(temp);
            j = 0;
            temp[0] = '\0';
            switch(str[++i])
            {
                case 'd': Serial.print(va_arg(argv, int));
                          break;
                case 'l': Serial.print(va_arg(argv, long));
                          break;
                case 'f': Serial.print(va_arg(argv, double));
                          break;
                case 'c': Serial.print((char)va_arg(argv, int));
                          break;
                case 's': Serial.print(va_arg(argv, char *));
                          break;
                default:  ;
            };
        }
        else
        {
            temp[j] = str[i];
            j = (j+1)%ARDBUFFER;
            if(j == 0)
            {
                temp[ARDBUFFER] = '\0';
                Serial.print(temp);
                temp[0] = '\0';
            }
        }
    };
    Serial.println();
    return count + 1;
}
#undef ARDBUFFER
#endif
