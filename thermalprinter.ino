#include "Adafruit_Thermal.h"
#include "SoftwareSerial.h"

#define TX_PIN 6 //6 // Arduino transmit  YELLOW WIRE  labeled RX on printer
#define RX_PIN 5 //5 // Arduino receive   GREEN WIRE   labeled TX on printer

SoftwareSerial mySerial(RX_PIN, TX_PIN); // Declare SoftwareSerial obj first
Adafruit_Thermal printer(&mySerial);     // Pass addr to printer constructor


void setup() {
  // NOTE: SOME PRINTERS NEED 9600 BAUD instead of 19200, check test page.
  mySerial.begin(9600);  // Initialize SoftwareSerial
  printer.begin();        // Init printer (same regardless of serial type)
  print_report();
}

void loop() {
}

void print_report() {
  printer.setSize('L');
  printer.justify('C');
  printer.println(F("TECHOOL LAB"));
  printer.println(F("ROORKEE, INDIA"));
  printer.setSize('M');
  printer.println(F("www.techooltech.com"));
  printer.println(F("+91-952000887"));
  printer.justify('L');
  printer.println(F("Contact For :"));
  printer.println(F("-STEM Education"));
  printer.println(F("-IoT Solution"));
  printer.println(F("-Automation Solution"));
  printer.println(F("STEM Modules :"));
  printer.println(F("-Robotics & Coding"));
  printer.println(F("-Machine Learning"));
  printer.println(F("-IoT"));
  printer.println(F("-Mobile App Development"));
  printer.println(F("-Game Development"));
  printer.println(F("-3D Technology"));
  printer.println(F("-One Day Workshop"));
  printer.feed(3);
  printer.sleep();      // Tell printer to sleep
  delay(3000L);         // Sleep for 3 seconds
  printer.wake();       // MUST wake() before printing again, even if reset
  printer.setDefault(); // Restore printer to defaults
}
