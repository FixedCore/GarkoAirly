#include <DigiUSB.h>
#include <Adafruit_NeoPixel.h>

uint8_t index, i = 0;
int input[4];
uint8_t c[3];
inline uint8_t toNum(const int* data)
{
  return (data[0] - '0') * 100 + (data[1] - '0') * 10 + (data[2] - '0');
}

Adafruit_NeoPixel eyes = Adafruit_NeoPixel(2, 0, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  eyes.begin();
  DigiUSB.begin();
  while (true)
  {
    if (DigiUSB.available())
    {
      input[index] = DigiUSB.read();
      DigiUSB.write(input[index]);
      if (++index == 4)
      {
        c[i] = toNum(input);
        i = (i + 1) % 3;
        index = 0;
        eyes.fill(eyes.Color(c[0], c[1], c[2]), 0, 2);
      }
    }
    eyes.show();
    DigiUSB.delay(15);
  }
}


void loop() {

}