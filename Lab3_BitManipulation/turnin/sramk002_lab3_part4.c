/*	Author: Sidharth Ramkuamar (sramk002@ucr.edu)
 *  Partner(s) Name: N/A
 *	Lab Section: 022
 *	Assignment: Lab #3  Exercise #4
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
    DDRB = 0x00; PORTB = 0x00;
    DDRC = 0xFF; PORTC = 0x00;

    /* Insert your solution below */
    unsigned char upper = 0x00;
    unsigned char lower = 0x00;
    
    unsigned char tmpA = 0x00;	
    while (1) {
	tmpA = PINA;
	upper = tmpA & 0xF0;
	upper = upper >> 4;	

	lower = tmpA & 0x0F;
	lower = lower << 4;

	PORTB = upper;
	PORTC = lower;
    }
    return 1;
}
