// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.



    @SCREEN     //screen base address
    D=A

    @8191 
    D=D+A     //calculate screen end address

    @screen_end //save screen end address in variable
    M=D

    @DETECT_KEY
    0; JMP


// listen to the keyboard

(DETECT_KEY)

    @KBD
    D=M

    @WHITE_SCREEN
    D; JEQ        // no key pressed

    @BLACK_SCREEN   //key pressed
    0; JMP



(BLACK_SCREEN)

    @SCREEN     //screen base address
    D=A

    @address    //load screen base address in variable named address
    M=D

    (FILL_BLACK)

        @screen_end     //check if all screen is black
        D = M - D

        @DETECT_KEY     // return to listening to keyboard
        D; JLT

        @address
        D=M
        A=D
        M=-1            // fill register with ones

        @address  
        M=M+1           //increment to next memory address
        D=M

        @FILL_BLACK     //loop to put ones in all memory map
        0; JMP

(WHITE_SCREEN)

    @SCREEN     //screen base address
    D=A

    @address    //load screen base address in variable named address
    M=D

    (FILL_WHITE)

        @screen_end
        D = M - D         //check if all screen is white

        @DETECT_KEY     // return to listening to keyboard
        D; JLT

        @address
        D=M
        A=D
        M=0               // fill register with zeros

        @address
        M=M+1             //increment to next memory address
        D=M

        @FILL_WHITE     //loop to put zeros in all memory map
        0; JMP
