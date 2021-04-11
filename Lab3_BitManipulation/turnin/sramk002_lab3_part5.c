/*      Author: Sidharth Ramkuamar (sramk002@ucr.edu)
 *       *  Partner(s) Name: N/A
 *        *     Lab Sectiion: 022
 *         *    Assignment: Lab #3  Exercise #5
 *          *   Exercise Description: [optional - include for your own benefit]
 *           *
 *            * I acknowledge all content contained herein, excluding template or example
 *             *        code, is my own original work.
 *              */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRB = 0xFE; PORTB = 0x01; //outputs
    DDRD = 0x00; PORTD = 0xFF; //inputs

    /* Insert your solution below */
    unsigned char tmpB = 0x01;
    unsigned short tmpD = 0x00;

    while (1) {
        tmpB = PINB & 0x01;
        tmpD = PIND << 1;
        tmpD = tmpD +  (PINB & 0x01);

        if (tmpD >= 0x46){
           tmpB = 0x02; //airbag enabled
        } else if ((tmpD > 0x05) && (tmpD < 0x46)){
           tmpB = 0x04; //airbag disabled
        } else {
           tmpB = 0x00; //no passenger
     }
    PORTB = tmpB;
    }
    return 1;
}
