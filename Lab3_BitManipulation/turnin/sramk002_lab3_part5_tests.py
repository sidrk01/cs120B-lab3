Last login: Sun Apr 11 14:16:37 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Sidharths-Air:~ sidharth_ramkumar$ ssh sramk002@bolt.cs.ucr.edu
sramk002@bolt.cs.ucr.edu's password: 
Last login: Sun Apr 11 14:16:44 2021 from cpe-23-243-46-90.socal.res.rr.com
~
sramk002@bolt $ ssh wch136-24.cs.ucr.edu
sramk002@wch136-24.cs.ucr.edu's password: 
Last login: Sun Apr 11 14:05:12 2021 from bolt.cs.ucr.edu

READ THIS!!!
============

* FILES ON THIS COMPUTER ARE DELETED WHEN YOU LOG OUT!

 > The "home directory" on this computer is in RAM.  It is EXTREMELY fast, but
   it is NOT your centrally stored CS home directory and it disappears when you
   log out!  Copy out any files you want to keep before you log out!!!

* HOW TO ACCESS YOUR CS HOME DIRECTORY AND FILES

 > IF you need to access your CS home directory and files (check with your TA
   for course-specific instructions), you can do so by connecting to server
   bolt.cs.ucr.edu using SSH for a command-line login session or SCP if you
   just need to copy files.

~
sramk002@wch136-24 $ /usr/csshare/pkgs/cs120b-avrtools/createProject.sh
Creating a new AVR project. Input the following or hit enter for the [default].
Project name: Lab2_introToAVR
Partners name [none]: 
Microcontroller [atmega1284]: 
Clock Frequency [8000000]: 
Creating project...
Creating project directory structure...
Creating project templates for source, tests, and Makefile...
Project created, to continue working: 

	1) Change working directory into project directory
	2) Initialize the directory to a GitHub repo: 
		$git init
	3) Add the files to the GitHub repo: 
		$git add .
	4) Make a first commit: 
		$git commit -m "Initializing repository"
	5) Create a project at github.com
	6) In terminal, add the URL to your project: 
		$git remote add origin <remote repository URL>
	7) Verify the remote repository: 
		$git remote -v
	8) Push the changes to GitHub: 
		$git push -u origin master
~
sramk002@wch136-24 $ ls
header           Lab3_BitManipulation  README.md  test    VirtualBox VMs
Lab2_introToAVR  Makefile              source     turnin
~
sramk002@wch136-24 $ cd Lab2_introToAVR/
~/Lab2_introToAVR
sramk002@wch136-24 $ ls
build  header  Makefile  source  test  turnin
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ cd test 
~/Lab2_introToAVR/test
sramk002@wch136-24 $ vim tests.py
~/Lab2_introToAVR/test
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 386 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x146: file source/main.c, line 24.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x01;
==================================================
Running test 1: PINA: 0x00 => PORTB: 0x00 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x01;
passed
==================================================
Running test 2: PINA: 0x01 => PORTB: 0x01
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x01;
passed
==================================================
Running test 3: PINA: 0x02 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x01;
passed
==================================================
Running test 4: PINA: 0x03 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x01;
passed
==================================================
Passed 4 / 4 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ exit 
logout
Connection to wch136-24.cs.ucr.edu closed.
~
sramk002@bolt $ exit 
logout

Connection to bolt.cs.ucr.edu closed.
Sidharths-Air:~ sidharth_ramkumar$ ls
Applications	Downloads	Pictures	practice.m	testbackup
CLionProjects	Library		Public		prelab2.m	untitled.m
Desktop		Movies		hw5.m		samplecomplex.m
Documents	Music		hw5p2.m		test.db
Sidharths-Air:~ sidharth_ramkumar$ cd Documents
Sidharths-Air:Documents sidharth_ramkumar$ git clone 
fatal: You must specify a repository to clone.

usage: git clone [<options>] [--] <repo> [<dir>]

    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --progress            force progress reporting
    -n, --no-checkout     don't create a checkout
    --bare                create a bare repository
    --mirror              create a mirror repository (implies bare)
    -l, --local           to clone from a local repository
    --no-hardlinks        don't use local hardlinks, always copy
    -s, --shared          setup as shared repository
    --recursive ...       alias of --recurse-submodules
    --recurse-submodules[=<pathspec>]
                          initialize submodules in the clone
    -j, --jobs <n>        number of submodules cloned in parallel
    --template <template-directory>
                          directory from which templates will be used
    --reference <repo>    reference repository
    --reference-if-able <repo>
                          reference repository
    --dissociate          use --reference only while cloning
    -o, --origin <name>   use <name> instead of 'origin' to track upstream
    -b, --branch <branch>
                          checkout <branch> instead of the remote's HEAD
    -u, --upload-pack <path>
                          path to git-upload-pack on the remote
    --depth <depth>       create a shallow clone of that depth
    --shallow-since <time>
                          create a shallow clone since a specific time
    --shallow-exclude <revision>
                          deepen history of shallow clone, excluding rev
    --single-branch       clone only one branch, HEAD or --branch
    --no-tags             don't clone any tags, and make later fetches not to follow them
    --shallow-submodules  any cloned submodules will be shallow
    --separate-git-dir <gitdir>
                          separate git dir from working tree
    -c, --config <key=value>
                          set config inside the new repository
    --server-option <server-specific>
                          option to transmit
    -4, --ipv4            use IPv4 addresses only
    -6, --ipv6            use IPv6 addresses only
    --filter <args>       object filtering
    --remote-submodules   any cloned submodules will use their remote-tracking branch

Sidharths-Air:Documents sidharth_ramkumar$ /*Author: Sidharth Ramkumar (sramk002@ucr.edu)
-bash: syntax error near unexpected token `('
Sidharths-Air:Documents sidharth_ramkumar$  * *  Partner(s) Name: none 
-bash: syntax error near unexpected token `('
Sidharths-Air:Documents sidharth_ramkumar$  *  *Lab Section: 022
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$  *   *Assignment: Lab #2  Exercise #2
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$  *    *Exercise Description: [optional - include for your own benefit]
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$  *     *
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$  *      *I acknowledge all content contained herein, excluding template or example
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$  *       *code, is my own original work.
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$  *        */
-bash: CS012: command not found
Sidharths-Air:Documents sidharth_ramkumar$ #include <avr/io.h>
Sidharths-Air:Documents sidharth_ramkumar$ #ifdef _SIMULATE_
Sidharths-Air:Documents sidharth_ramkumar$ #include "simAVRHeader.h"
Sidharths-Air:Documents sidharth_ramkumar$ #endif
Sidharths-Air:Documents sidharth_ramkumar$ 
Sidharths-Air:Documents sidharth_ramkumar$ int main(void) {
-bash: syntax error near unexpected token `('
Sidharths-Air:Documents sidharth_ramkumar$     /* Insert DDR and PORT initializations */   
-bash: /Applications: is a directory
    DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
    DDRC = 0xFF; PORTC = 0x00; //Configure port C's 8 pins as outputs, intializie to 0s
unsigned char taken = 0x00;
unsigned char cntavail = 0x00; //Temporary variable to assign the value to C 

unsigned char tmpA = 0x00; //Temporary variable to hold A
    /* Insert your solution below */
    while (1) {
tmpA = PINA;
   taken = 0x00;
   
unsigned char i = 0x01;

while (i <= 0x04){
    if (tmpA & i){
    taken = taken + 1;	
	}
i = i * 0x02;	
}
	cntavail = 0x04 - taken;
	
if (cntavail == 0x00 ){
	cntavail = cntavail |  0x80;	
}

PORTC = cntavail;
    }
    return 1;
}Sidharths-Air:Documents sidharth_ramkumar$     DDRA = 0x00; PORTA = 0xFF; // Cofigure port A's 8 pins as inputs
>     DDRC = 0xFF; PORTC = 0x00; //Configure port C's 8 pins as outputs, intializie to 0s
-bash: DDRA: command not found
-bash: PORTA: command not found
-bash: //: is a directory
Sidharths-Air:Documents sidharth_ramkumar$ unsigned char taken = 0x00;
-bash: unsigned: command not found
Sidharths-Air:Documents sidharth_ramkumar$ unsigned char cntavail = 0x00; //Temporary variable to assign the value to C 
-bash: unsigned: command not found
-bash: //Temporary: No such file or directory
Sidharths-Air:Documents sidharth_ramkumar$ 
Sidharths-Air:Documents sidharth_ramkumar$ unsigned char tmpA = 0x00; //Temporary variable to hold A
-bash: unsigned: command not found
-bash: //Temporary: No such file or directory
Sidharths-Air:Documents sidharth_ramkumar$     /* Insert your solution below */
-bash: /Applications: is a directory
Sidharths-Air:Documents sidharth_ramkumar$     while (1) {
-bash: syntax error near unexpected token `{'
Sidharths-Air:Documents sidharth_ramkumar$ tmpA = PINA;
-bash: tmpA: command not found
Sidharths-Air:Documents sidharth_ramkumar$    taken = 0x00;
-bash: taken: command not found
Sidharths-Air:Documents sidharth_ramkumar$    
Sidharths-Air:Documents sidharth_ramkumar$ unsigned char i = 0x01;
-bash: unsigned: command not found
Sidharths-Air:Documents sidharth_ramkumar$ 
Sidharths-Air:Documents sidharth_ramkumar$ while (i <= 0x04){
-bash: syntax error near unexpected token `{'
Sidharths-Air:Documents sidharth_ramkumar$     if (tmpA & i){
-bash: syntax error near unexpected token `{'
Sidharths-Air:Documents sidharth_ramkumar$     taken = taken + 1;
-bash: taken: command not found
Sidharths-Air:Documents sidharth_ramkumar$ }
-bash: syntax error near unexpected token `}'
Sidharths-Air:Documents sidharth_ramkumar$ i = i * 0x02;
-bash: i: command not found
Sidharths-Air:Documents sidharth_ramkumar$ }
-bash: syntax error near unexpected token `}'
Sidharths-Air:Documents sidharth_ramkumar$ cntavail = 0x04 - taken;
-bash: cntavail: command not found
Sidharths-Air:Documents sidharth_ramkumar$ 
Sidharths-Air:Documents sidharth_ramkumar$ if (cntavail == 0x00 ){
-bash: syntax error near unexpected token `{'
Sidharths-Air:Documents sidharth_ramkumar$ cntavail = cntavail |  0x80;
-bash: cntavail: command not found
-bash: 0x80: command not found
Sidharths-Air:Documents sidharth_ramkumar$ }
-bash: syntax error near unexpected token `}'
Sidharths-Air:Documents sidharth_ramkumar$ 
Sidharths-Air:Documents sidharth_ramkumar$ PORTC = cntavail;
-bash: PORTC: command not found
Sidharths-Air:Documents sidharth_ramkumar$     }
-bash: syntax error near unexpected token `}'
Sidharths-Air:Documents sidharth_ramkumar$     return 1;
-bash: return: can only `return' from a function or sourced script
Sidharths-Air:Documents sidharth_ramkumar$  git clone https://github.com/sidrk01/cs120b-lab2.git
fatal: destination path 'cs120b-lab2' already exists and is not an empty directory.
Sidharths-Air:Documents sidharth_ramkumar$ rm -rf cs120b-lab2
Sidharths-Air:Documents sidharth_ramkumar$ git clone https://github.com/sidrk01/cs120b-lab2.git
Cloning into 'cs120b-lab2'...
remote: Enumerating objects: 79, done.
remote: Counting objects: 100% (79/79), done.
remote: Compressing objects: 100% (52/52), done.
remote: Total 79 (delta 36), reused 49 (delta 18), pack-reused 0
Unpacking objects: 100% (79/79), done.
Sidharths-Air:Documents sidharth_ramkumar$ ssh sramk002@bolt.cs.ucr.edu
sramk002@bolt.cs.ucr.edu's password: 
Permission denied, please try again.
sramk002@bolt.cs.ucr.edu's password: 
Last failed login: Sun Apr 11 14:34:28 PDT 2021 from cpe-23-243-46-90.socal.res.rr.com on ssh:notty
There was 1 failed login attempt since the last successful login.
Last login: Sun Apr 11 14:17:58 2021 from cpe-23-243-46-90.socal.res.rr.com
~
sramk002@bolt $ ssh wch136-24.cs.ucr.edu
sramk002@wch136-24.cs.ucr.edu's password: 
Last login: Sun Apr 11 14:18:07 2021 from bolt.cs.ucr.edu

READ THIS!!!
============

* FILES ON THIS COMPUTER ARE DELETED WHEN YOU LOG OUT!

 > The "home directory" on this computer is in RAM.  It is EXTREMELY fast, but
   it is NOT your centrally stored CS home directory and it disappears when you
   log out!  Copy out any files you want to keep before you log out!!!

* HOW TO ACCESS YOUR CS HOME DIRECTORY AND FILES

 > IF you need to access your CS home directory and files (check with your TA
   for course-specific instructions), you can do so by connecting to server
   bolt.cs.ucr.edu using SSH for a command-line login session or SCP if you
   just need to copy files.

~
sramk002@wch136-24 $ ls
header           Lab3_BitManipulation  README.md  test    VirtualBox VMs
Lab2_introToAVR  Makefile              source     turnin
~
sramk002@wch136-24 $ cd Lab2_introToAVR/
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ cd test
~/Lab2_introToAVR/test
sramk002@wch136-24 $ vim tests.py
~/Lab2_introToAVR/test
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 400 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x14a: file source/main.c, line 26.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:26
26	tmpA = PINA;
==================================================
Running test 1: PINA: 0x00 => PORTC: 0x04 
Breakpoint 1, main () at source/main.c:26
26	tmpA = PINA;
passed
==================================================
Running test 2: PINA: 0x01 => PORTC: 0x03
Breakpoint 1, main () at source/main.c:26
26	tmpA = PINA;
failed.
	Expected PORTC := 0x3 but got 0x4
==================================================
Running test 3: PINA: 0x03 => PORTC: 0x02
Breakpoint 1, main () at source/main.c:26
26	tmpA = PINA;
failed.
	Expected PORTC := 0x2 but got 0x4
==================================================
Running test 4: PINA: 0x0E => PORTC: 0x01
Breakpoint 1, main () at source/main.c:26
26	tmpA = PINA;
failed.
	Expected PORTC := 0x1 but got 0x4
==================================================
Passed 1 / 4 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 400 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x146: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25	tmpA = PINA;
==================================================
Running test 1: PINA: 0x00 => PORTC: 0x04 
Breakpoint 1, main () at source/main.c:25
25	tmpA = PINA;
passed
==================================================
Running test 2: PINA: 0x01 => PORTC: 0x03
Breakpoint 1, main () at source/main.c:25
25	tmpA = PINA;
passed
==================================================
Running test 3: PINA: 0x03 => PORTC: 0x02
Breakpoint 1, main () at source/main.c:25
25	tmpA = PINA;
passed
==================================================
Running test 4: PINA: 0x0E => PORTC: 0x01
Breakpoint 1, main () at source/main.c:25
25	tmpA = PINA;
passed
==================================================
Passed 4 / 4 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ cd test
~/Lab2_introToAVR/test
sramk002@wch136-24 $ vim tests.py
~/Lab2_introToAVR/test
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 592 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x172: file source/main.c, line 30.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
==================================================
Running test 1: PINA: 15, PINB: 15, PINC: 15 => PORTD: 0b00101100
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x2c but got 0xb4
==================================================
Running test 2: PINA: 20, PINB: 50, PINC: 110 => PORTD: 0b10110111
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
passed
==================================================
Running test 3: PINA: 10, PINB: 20, PINC: 91 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x7a but got 0xf2
==================================================
Running test 4: PINA: 91, PINB: 20, PINC: 10 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x7a but got 0xf2
==================================================
Running test 5: PINA: 40, PINB: 50, PINC: 60 => PORTD: 0b10010101
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
passed
==================================================
Running test 6: PINA: 0, PINB: 0, PINC: 0 => PORTD: 0b00000000
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
passed
==================================================
Passed 3 / 6 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 576 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x172: file source/main.c, line 30.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
==================================================
Running test 1: PINA: 15, PINB: 15, PINC: 15 => PORTD: 0b00101100
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x2c but got 0x8
==================================================
Running test 2: PINA: 20, PINB: 50, PINC: 110 => PORTD: 0b10110111
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0xb7 but got 0x2f
==================================================
Running test 3: PINA: 10, PINB: 20, PINC: 91 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x7a but got 0x1e
==================================================
Running test 4: PINA: 91, PINB: 20, PINC: 10 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x7a but got 0x1e
==================================================
Running test 5: PINA: 40, PINB: 50, PINC: 60 => PORTD: 0b10010101
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x95 but got 0x25
==================================================
Running test 6: PINA: 0, PINB: 0, PINC: 0 => PORTD: 0b00000000
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
passed
==================================================
Passed 1 / 6 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 578 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x172: file source/main.c, line 30.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
==================================================
Running test 1: PINA: 15, PINB: 15, PINC: 15 => PORTD: 0b00101100
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x2c but got 0x8
==================================================
Running test 2: PINA: 20, PINB: 50, PINC: 110 => PORTD: 0b10110111
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0xb7 but got 0x2f
==================================================
Running test 3: PINA: 10, PINB: 20, PINC: 91 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x7a but got 0x1e
==================================================
Running test 4: PINA: 91, PINB: 20, PINC: 10 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x7a but got 0x1e
==================================================
Running test 5: PINA: 40, PINB: 50, PINC: 60 => PORTD: 0b10010101
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
failed.
	Expected PORTD := 0x95 but got 0x25
==================================================
Running test 6: PINA: 0, PINB: 0, PINC: 0 => PORTD: 0b00000000
Breakpoint 1, main () at source/main.c:30
30	   tmpA = PINA;
passed
==================================================
Passed 1 / 6 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd sourc 
-bash: cd: sourc: No such file or directory
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 604 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x164: file source/main.c, line 24.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
==================================================
Running test 1: PINA: 15, PINB: 15, PINC: 15 => PORTD: 0b00101100
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x2c but got 0xb4
==================================================
Running test 2: PINA: 20, PINB: 50, PINC: 110 => PORTD: 0b10110111
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
passed
==================================================
Running test 3: PINA: 10, PINB: 20, PINC: 91 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x7a but got 0xf2
==================================================
Running test 4: PINA: 91, PINB: 20, PINC: 10 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x7a but got 0xf2
==================================================
Running test 5: PINA: 40, PINB: 50, PINC: 60 => PORTD: 0b10010101
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
passed
==================================================
Running test 6: PINA: 0, PINB: 0, PINC: 0 => PORTD: 0b00000000
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
passed
==================================================
Passed 3 / 6 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 594 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x164: file source/main.c, line 24.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
==================================================
Running test 1: PINA: 15, PINB: 15, PINC: 15 => PORTD: 0b00101100
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x2c but got 0x8
==================================================
Running test 2: PINA: 20, PINB: 50, PINC: 110 => PORTD: 0b10110111
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0xb7 but got 0x2f
==================================================
Running test 3: PINA: 10, PINB: 20, PINC: 91 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x7a but got 0x1e
==================================================
Running test 4: PINA: 91, PINB: 20, PINC: 10 => PORTD: 0b01111010
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x7a but got 0x1e
==================================================
Running test 5: PINA: 40, PINB: 50, PINC: 60 => PORTD: 0b10010101
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
failed.
	Expected PORTD := 0x95 but got 0x25
==================================================
Running test 6: PINA: 0, PINB: 0, PINC: 0 => PORTD: 0b00000000
Breakpoint 1, main () at source/main.c:24
24		tmpD = 0x00;
passed
==================================================
Passed 1 / 6 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd test
-bash: cd: test: No such file or directory
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim tests.py
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ cd test
~/Lab2_introToAVR/test
sramk002@wch136-24 $ vim tests.py
~/Lab2_introToAVR/test
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ cd source 
~/Lab2_introToAVR/source
sramk002@wch136-24 $ vim main.c
~/Lab2_introToAVR/source
sramk002@wch136-24 $ cd ..
~/Lab2_introToAVR
sramk002@wch136-24 $ cd test
~/Lab2_introToAVR/test
sramk002@wch136-24 $ vim tests.py
~/Lab2_introToAVR/test
sramk002@wch136-24 $ exit
logout
Connection to wch136-24.cs.ucr.edu closed.
~
sramk002@bolt $ exit
logout

Connection to bolt.cs.ucr.edu closed.
Sidharths-Air:Documents sidharth_ramkumar$ ls
CS012			MATLAB			Winter 2021 Materials
CS014			Math:CS011		Zoom
CS061			PHYS040B Labs		cs120B-lab3
Fall 2020 Materials	PreviewAgreement.pdf	cs120b-lab2
JavaPrograms		Resume			lib
LTspice			Winter 2020 Finals	~$01B Final Notes.docx
Sidharths-Air:Documents sidharth_ramkumar$ cd Documents
-bash: cd: Documents: No such file or directory
Sidharths-Air:Documents sidharth_ramkumar$ rm -rf cs120-lab2
Sidharths-Air:Documents sidharth_ramkumar$ git clone https://github.com/sidrk01/cs120b-lab2.git
fatal: destination path 'cs120b-lab2' already exists and is not an empty directory.
Sidharths-Air:Documents sidharth_ramkumar$ rm -rf cs120b-lab2
Sidharths-Air:Documents sidharth_ramkumar$ git clone https://github.com/sidrk01/cs120b-lab2.git
Cloning into 'cs120b-lab2'...
remote: Enumerating objects: 95, done.
remote: Counting objects: 100% (95/95), done.
remote: Compressing objects: 100% (67/67), done.
remote: Total 95 (delta 47), reused 48 (delta 18), pack-reused 0
Unpacking objects: 100% (95/95), done.
Sidharths-Air:Documents sidharth_ramkumar$ ssh sramk002@bolt.cs.ucr.edu
sramk002@bolt.cs.ucr.edu's password: 
Last login: Sun Apr 11 14:34:32 2021 from cpe-23-243-46-90.socal.res.rr.com
~
sramk002@bolt $ ssh wch136-24.cs.ucr.edu
sramk002@wch136-24.cs.ucr.edu's password: 
Last login: Sun Apr 11 14:34:39 2021 from bolt.cs.ucr.edu

READ THIS!!!
============

* FILES ON THIS COMPUTER ARE DELETED WHEN YOU LOG OUT!

 > The "home directory" on this computer is in RAM.  It is EXTREMELY fast, but
   it is NOT your centrally stored CS home directory and it disappears when you
   log out!  Copy out any files you want to keep before you log out!!!

* HOW TO ACCESS YOUR CS HOME DIRECTORY AND FILES

 > IF you need to access your CS home directory and files (check with your TA
   for course-specific instructions), you can do so by connecting to server
   bolt.cs.ucr.edu using SSH for a command-line login session or SCP if you
   just need to copy files.

~
sramk002@wch136-24 $ /usr/csshare/pkgs/cs120b-avrtools/createProject.sh
Creating a new AVR project. Input the following or hit enter for the [default].
Project name: 
Partners name [none]: 
Microcontroller [atmega1284]: 
Clock Frequency [8000000]: 
Creating project...
Creating project directory structure...
Creating project templates for source, tests, and Makefile...
Project created, to continue working: 

	1) Change working directory into project directory
	2) Initialize the directory to a GitHub repo: 
		$git init
	3) Add the files to the GitHub repo: 
		$git add .
	4) Make a first commit: 
		$git commit -m "Initializing repository"
	5) Create a project at github.com
	6) In terminal, add the URL to your project: 
		$git remote add origin <remote repository URL>
	7) Verify the remote repository: 
		$git remote -v
	8) Push the changes to GitHub: 
		$git push -u origin master
~
sramk002@wch136-24 $ cd
~
sramk002@wch136-24 $ cd 
~
sramk002@wch136-24 $ ls
header                Makefile                        source  VirtualBox VMs
Lab2_introToAVR       Project name: Lab2_introToAVR?  test
Lab3_BitManipulation  README.md                       turnin
~
sramk002@wch136-24 $ cd Lab3_BitManipulation/
~/Lab3_BitManipulation
sramk002@wch136-24 $ ls
build  header  Makefile  source  test  turnin
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd test
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ vim tests.py
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 496 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x162: file source/main.c, line 24.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA;
==================================================
Running test 1: PINA: 0x01 => PORTC: 0x60
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA;
passed
==================================================
Running test 2: PINA: 0x03 => PORTC: 0x70 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA;
passed
==================================================
Running test 3: PINA: 0x05 => PORTC: 0x38
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA;
passed
==================================================
Running test 4: PINA: 0x0A => PORTC: 0x3E 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA;
passed
==================================================
Running test 5: PINA: 0x83 => PORTC: 0x70 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA;
failed.
	Expected PORTC := 0x70 but got 0x0
==================================================
Passed 4 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd .. 
~
sramk002@wch136-24 $ cd Lab3_BitManipulation/
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd .. 
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 498 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x162: file source/main.c, line 24.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x0F;
==================================================
Running test 1: PINA: 0x01 => PORTC: 0x60
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x0F;
passed
==================================================
Running test 2: PINA: 0x03 => PORTC: 0x70 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x0F;
passed
==================================================
Running test 3: PINA: 0x05 => PORTC: 0x38
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x0F;
passed
==================================================
Running test 4: PINA: 0x0A => PORTC: 0x3E 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x0F;
passed
==================================================
Running test 5: PINA: 0x83 => PORTC: 0x70 
Breakpoint 1, main () at source/main.c:24
24	    tmpA = PINA & 0x0F;
passed
==================================================
Passed 5 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd .. 
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd test
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ vim tests.py
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 402 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x144: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
==================================================
Running test 1: PINB: 0x00 PIND: 0x00 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 2: PINB: 0x00 PIND: 0xFF => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 3: PINB: 0x01 PIND: 0x01  => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 4: PINB: 0x01 PIND: 0x05  => PORTB: 0x04
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 5: PINB: 0x01 PIND: 0xF2 => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Passed 5 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd test
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ vim tests.py
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 402 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x144: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
==================================================
Running test 1: PINB: 0x00 PIND: 0x00 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 2: PINB: 0x00 PIND: 0xFF => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 3: PINB: 0x01 PIND: 0x01  => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 4: PINB: 0x01 PIND: 0x05  => PORTB: 0x04
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 5: PINB: 0x00 PIND: 0x80 => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
failed.
	Expected PORTB := 0x2 but got 0x0
==================================================
Passed 4 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 400 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x144: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
==================================================
Running test 1: PINB: 0x00 PIND: 0x00 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 2: PINB: 0x00 PIND: 0xFF => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 3: PINB: 0x01 PIND: 0x01  => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 4: PINB: 0x01 PIND: 0x05  => PORTB: 0x04
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
passed
==================================================
Running test 5: PINB: 0x00 PIND: 0x80 => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25		tmpD = PIND << 1;
failed.
	Expected PORTB := 0x2 but got 0x0
==================================================
Passed 4 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 410 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x144: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB;
==================================================
Running test 1: PINB: 0x00 PIND: 0x00 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB;
passed
==================================================
Running test 2: PINB: 0x00 PIND: 0xFF => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB;
passed
==================================================
Running test 3: PINB: 0x01 PIND: 0x01  => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB;
passed
==================================================
Running test 4: PINB: 0x01 PIND: 0x05  => PORTB: 0x04
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB;
passed
==================================================
Running test 5: PINB: 0x00 PIND: 0x80 => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB;
failed.
	Expected PORTB := 0x2 but got 0x0
==================================================
Passed 4 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 412 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x144: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
==================================================
Running test 1: PINB: 0x00 PIND: 0x00 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 2: PINB: 0x00 PIND: 0xFF => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 3: PINB: 0x01 PIND: 0x01  => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 4: PINB: 0x01 PIND: 0x05  => PORTB: 0x04
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 5: PINB: 0x00 PIND: 0x80 => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
failed.
	Expected PORTB := 0x2 but got 0x0
==================================================
Passed 4 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ make pytest
simavr -g -mmcu=atmega1284 -f 8000000 build/objects/main.elf &
avr-gdb -se=build/objects/main.elf -batch -x test/tests.py -x test/testRunner.py -ex runTests
Loaded 450 .text at address 0x0
Loaded 14 .data
avr_gdb_init listening on port 1234
gdb_network_handler connection opened
0x00000000 in __vectors ()
Breakpoint 1 at 0x14a: file source/main.c, line 25.
Note: automatically using hardware breakpoints for read-only addresses.

Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
==================================================
Running test 1: PINB: 0x00 PIND: 0x00 => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 2: PINB: 0x00 PIND: 0xFF => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 3: PINB: 0x01 PIND: 0x01  => PORTB: 0x00
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 4: PINB: 0x01 PIND: 0x05  => PORTB: 0x04
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Running test 5: PINB: 0x00 PIND: 0x80 => PORTB: 0x02
Breakpoint 1, main () at source/main.c:25
25	        tmpB = PINB & 0x01;
passed
==================================================
Passed 5 / 5 tests. Skipped 0 tests.
==================================================
Remote doesn't know how to detach
gdb_network_handler connection closed
signal caught, simavr terminating
pkill: killing pid 29234 failed: Operation not permitted
pkill: killing pid 30124 failed: Operation not permitted
pkill: killing pid 30338 failed: Operation not permitted
pkill: killing pid 30593 failed: Operation not permitted
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd source 
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ vim main.c
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd test 
-bash: cd: test: No such file or directory
~/Lab3_BitManipulation/source
sramk002@wch136-24 $ cd ..
~/Lab3_BitManipulation
sramk002@wch136-24 $ cd test 
~/Lab3_BitManipulation/test
sramk002@wch136-24 $ vim tests.py

#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [{'description': 'PINB: 0x00 PIND: 0x00 => PORTB: 0x00',
    'steps': [ {'inputs': [('PINB', 0x00), ('PIND', 0x00)], 'iterations': 1 } ],
    'expected': [('PORTB', 0x00)],
    },
    {'description': 'PINB: 0x00 PIND: 0xFF => PORTB: 0x02',
    'steps': [ {'inputs': [('PINB', 0x00), ('PIND', 0xFF)], 'iterations': 1 } ],
    'expected': [('PORTB', 0x02)],
    },
    {'description': 'PINB: 0x01 PIND: 0x01  => PORTB: 0x00',
    'steps': [ {'inputs': [('PINB', 0x01), ('PIND', 0x01)], 'iterations': 1 } ],
    'expected': [('PORTB', 0x00)],
    },
    {'description': 'PINB: 0x01 PIND: 0x05  => PORTB: 0x04',
    'steps': [ {'inputs': [('PINB', 0x01), ('PIND', 0x05)], 'iterations': 1 } ],
    'expected': [('PORTB', 0x04)],
    },
    {'description': 'PINB: 0x00 PIND: 0x80 => PORTB: 0x02',
    'steps': [ {'inputs': [('PINB', 0x00), ('PIND', 0x80)], 'iterations': 1 } ],
    'expected': [('PORTB', 0x02)],
    }
]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']
