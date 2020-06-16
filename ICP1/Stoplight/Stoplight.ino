
int switchState = 0;
int stopper = 0;

void setup() {
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(2, INPUT);
  
}

void loop(){
  switchState = digitalRead(2);
  if(switchState == LOW){
  // the button is not pressed
  digitalWrite(3, HIGH); //green LED
  digitalWrite(4, LOW); //Red LED
  digitalWrite(5, LOW); //red LED

  //Resets lights
  stopper = 0;
  
  }

  else{
    //allows cycle through lights one time until reset
    if(stopper == 0) { 
    stopper = 1;   
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);

    delay(1000); // wait for a quarter seconds
    digitalWrite(4, LOW);
    }
    digitalWrite(5, HIGH);
    delay(5000);
 
  }
  

}
