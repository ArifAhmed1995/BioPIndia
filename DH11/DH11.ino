#include <dht.h>

/*
Retrieve DHT data (temp, humidity)
A.LINA
*/

/*-----( Declare objects )-----*/
dht DHT_sensor;

/*-----( Declare Constants, Pin Numbers )-----*/
#define DHT_PIN 2
#define SAMPLING_RATE 1000 //ms

/*--(start setup )---*/
void setup()
  {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
    }
  Serial.println("DHT SENSOR");
  Serial.println();
  }
/*--(end setup )---*/

/*--(start loop )---*/
void loop()
  {
  Serial.println("\n");

  int chk = DHT_sensor.read11(DHT_PIN);

  if(chk==0)
    {
    String str = "DHT:";
    long   val;

    str += "H ";
    val = (long)(DHT_sensor.humidity*1024+0.5);
    str += val;
    str += " T ";
    val = (long)(DHT_sensor.temperature*1024+0.5);
    str += val;

    Serial.println(str);
    Serial.flush();
    delay(20);
    }
  else
    {
    Serial.println("DHT_Error");
    }

  delay(SAMPLING_RATE);
  }
