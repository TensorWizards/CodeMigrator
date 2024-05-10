IDENTIFICATION DIVISION.
PROGRAM-ID. PrimeChecker.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Num PIC 9(5).
01 IsPrime PIC X(3) VALUE 'YES'.

PROCEDURE DIVISION.
    DISPLAY 'Enter a number to check if it is prime: '.
    ACCEPT Num.

    IF Num <= 1
        DISPLAY Num ' is not a prime number'
    ELSE
        PERFORM CHECK-PRIME
    END-IF.

    STOP RUN.

CHECK-PRIME.
    DIVIDE Num BY 2 GIVING Num REMAINDER Remainder.

    PERFORM VARYING Divisor FROM 2 BY 1 UNTIL Divisor > Num / 2
        IF Remainder = 0
            MOVE 'NO' TO IsPrime
            EXIT PERFORM
        END-IF
    END-PERFORM.

    IF IsPrime = 'YES'
        DISPLAY Num ' is a prime number'
    ELSE
        DISPLAY Num ' is not a prime number'
    END-IF.
