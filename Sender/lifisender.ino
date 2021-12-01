#define GREEN 8
#define BLUE 9
#define PERIOD 25
int a;
char s;

void setup(){
  Serial.begin(9600);  
  pinMode(15,INPUT);
}

void loop(){
  if (Serial.available()){
      s=Serial.read();
      Serial.println(s);
   }
}

void send_char(char my_byte){
  for(int i = 0; i < 8; i++){
    digitalWrite(GREEN, (my_byte&(0x01 << i))!=0 );
    digitalWrite(BLUE, (my_byte&(0x01 << i))==0 );
    delay(PERIOD);
  }
}