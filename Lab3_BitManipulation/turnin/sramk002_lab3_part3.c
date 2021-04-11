/*	Author: Sidharth Ramkumar (sramk002@ucr.edu)
 *	 *  Partner(s) Name: none
 *	  *	Lab Section: 022
 *	   *	Assignment: Lab #3  Exercise #3
 *	    *	Exercise Description: [optional - include for your own benefit]
 *	     *
 *	      *	I acknowledge all content contained herein, excluding template or example
 *	       *	code, is my own original work.
 *	        */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF;
    DDRC = 0xFF; PORTC = 0x00; 

unsigned char tmpA = 0x00;
unsigned char tmpC = 0x00;
unsigned char keyIN = 0x00;
unsigned char seated = 0x00;
unsigned char seatbelt = 0x00;

    /* Insert your solution below */
    while (1) {
    tmpA = PINA;

   /*Sensors on/off*/

   keyIN = tmpA & 0x10;
   seated = tmpA & 0x20;
   seatbelt = tmpA & 0x40;    
    
   tmpA = tmpA  & 0x0F;

    switch (tmpA){
	case 0x00: 
	tmpC = 0x00;
	break;
	
	case 0x01:
	case 0x02:
	tmpC = 0x20;
	break;

	case 0x03:
	case 0x04: 
	tmpC = 0x30;
 	break;

	case 0x05: 
	case 0x06: 
	tmpC = 0x38;
	break;

	case 0x07:
	case 0x08:
	case 0x09: 
	tmpC = 0x3C;
	break;

	case 0x0A:
	case 0x0B:
	case 0x0C: 
	tmpC = 0x3E; 
	break;

	case 0x0D:
	case 0x0E: 
	case 0x0F:
	tmpC = 0x3F;
     	break;
	
	default: 
	tmpC = 0x00; 
	break;
    }

/*Low fuel light*/
if (tmpA <= 0x04){
   tmpC = tmpC | 0x40;
}

/*Belt not fastened*/
if (keyIN && seated && (!seatbelt)){
	tmpC = tmpC + 0x80;

}

PORTC = tmpC;
}
    return 1;
}
