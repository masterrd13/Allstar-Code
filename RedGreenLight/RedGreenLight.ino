/*
Adopted code from https://www.arduino.cc/en/Tutorial/Blink

Modified to include more lights.
Watch video at https://www.youtube.com/watch?v=THPjbVEGNR8
*/

//Setting up pins being used (Good idea to use variables instead of hard coding them)
int greenLED = 9;
int redLED = 5;

void setup() {
  // initialize each pin as an output for electricity.
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);

}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(greenLED, 1);   // turn the LED on (HIGH is means the same as 1)
  digitalWrite(redLED, 0);   // turn the LED off (LOW is means the same as 0)
  delay(1000);              // wait for a second (1000 miliseconds)
  
  digitalWrite(greenLED, 0);
  digitalWrite(redLED, 1);  
  delay(1000); 
}
