#include <wiringPi.h>     //包含wiringPi头文件

int main(void)
{
    int ledpin=3;
    wiringPiSetup();        //wiringPi库初始化
    pinMode(ledpin, OUTPUT);     //设置0口为输出模式
    for(;;)             //循环执行
    {
        digitalWrite(ledpin,  HIGH); //GPIO.0输出高电平
        delay(1000);        //延迟1000ms
        digitalWrite(ledpin,  LOW);  // GPIO.0输出高电平
        delay(1000);        //延迟1000ms
    }
    return 0; 
}
