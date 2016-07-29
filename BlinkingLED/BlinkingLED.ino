//THIS IS A COMMENT! :-D
// Example 01: Blinking LED 
int LED = 13; // LED connected to digital pin 13
 //

// Setup is called every time the Arduino starts up or resets 
void setup() {
pinMode(LED, OUTPUT); // sets the digital pin as
//output
}

//Loop is called and run forever
void loop() {
digitalWrite(LED, 1); // 1 means on (HIGH means same)
digitalWrite(LED, 0); // 0 means off (LOW means same)
}
