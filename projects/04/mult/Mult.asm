// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.




// init R2 with value 0
    @R2
    M=0

// IF R0 OR R1 EQUAL ZERO

    @R0
    D=M
    @END
    D; JEQ        //R0 == 0

    @R1
    D=M
    @END
    D; JEQ      //R1 == 0


// R0 AND R1 NOT EQUAL ZERO
// check which one is smaller number to be put as counter value
// in order to make the program faster and more efficient

//R1 - R0
    @R0
    D=D-M

//IF R0 < R1
    @R0_LESS 
    D; JGT

//IF R1 <= R0
    @R1
    D=M
    @counter
    M=D   //counter = R1 

    @R0
    D=M
    @number
    M=D   //number = R0 

    @LOOP
    0; JMP

(R0_LESS)
    @R0
    D=M
    @counter
    M=D   //counter = R0 

    @R1
    D=M
    @number
    M=D   //number = R1 
    @LOOP
    0; JMP

(LOOP)
    @number
    D=M
    @R2
    M=M+D       //multiplication is just repeated addition

    @counter
    M=M-1    // Decrement the counter
    D=M
    @END
    D; JEQ   // If the counter reaches 0, jump to END

    @LOOP
    0; JMP   // Jump to LOOP to continue the multiplication



(END)
    @END
    0; JMP






