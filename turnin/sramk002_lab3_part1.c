/*	Author: Sidharth Ramkumar (sramk002@ucr.edu)
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #3  Exercise #1
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF;
    DDRB = 0x00; PORTB = 0xFF;
    DDRC = 0xFF; PORTC = 0x00; 

unsigned char tmpA = 0x00;
unsigned char tmpB = 0x00;
    /* Insert your solution below */
    while (1) {
    tmpA = PINA;
    tmpB = PINB;
    
    unsigned char cnt = 0x00;
    unsigned char bitShift = 0x01;  
    unsigned char i = 0x00;
    
    while (i < 0x08){
        if (tmpA & bitShift){
	   cnt = cnt + 1;
	}
 	if (tmpB & bitShift){
	   cnt = cnt + 1;
	}
 	bitShift = bitShift << 1;
	i = i + 1;       
 }

PORTC = cnt;

}
    return 1;
}
