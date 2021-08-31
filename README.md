# pymmurabi
The classic game Hammurabi ported to Python

This is an attempt to recreate the classic game Hammuraby in Python.  
I will be using the original source code as aquired from this web site.  

https://programmingpraxis.com/2010/07/27/hamurabi-bas/

## Description from the site
"Back in the 1970s, David Ahl wrote a new game program each month for Creative Computing magazine. Those were the days of all-caps teletypes (if you were rich you could get a new-fangled “glass teletype”) and punched paper tapes (it was fun to play with the confetti they made). MS-BASIC permitted twenty-six single-letter variable names; later they also allowed a single letter followed by a single digit. There were no user-defined functions and no recursion. GOTO was common, resulting in a phenomenon called “spaghetti code.” There was good news, however: it was acceptable programming practice to GOTO the middle of a FOR loop and run the code there, as long as you jumped back out of the loop before the corresponding NEXT — try to do that in your favorite functional language!

One of Ahl’s most memorable games was Hamurabi, in which the player took the role of the administrator of the ancient city of Sumeria, managing the grain and land resources of the city and trying to keep the residents from starvation. It is typical of the genre, with simple numeric input and scrolling text output. Here is a description and sample game, and the original BASIC source code is reproduced on the next page. By my count, there are fourteen lines that are unreachable except by an IF…THEN, GOSUB or GOTO, forty-three lines that redirect control flow away from the line below, and four instances (line 555 to 215, bypassing line 210, 453 and 479 to 440, bypassing 430, 441 to 511, bypassing 510, and 880 and 885 to 565, bypassing 560) of jumping into the middle of a block of code; that’s a fine bowl of spaghetti, considering the entire program is only 120 lines. Variable P represents the current population, S is the number of bushels in stores, and A is the number of acres of farmland owned by the city, but other variables are used inconsistently — for instance D sometimes represents the number of deaths in the current year, but other times it represents the current input value, and other times Q is used to represent the current input value.

Your task is to reimplement HAMURABI.BAS in a more modern computer language. Don’t peek at the solution unless you want to deprive yourself of the sheer joy of working out the spaghetti code and figuring out what the variables really stand for. When you are finished, you are welcome to read or run a suggested solution, or to post your own solution or discuss the exercise in the comments below."

## Basic source code

```
10 PRINT TAB(32);"HAMURABI"
20 PRINT TAB(15);"CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY"
30 PRINT:PRINT:PRINT
80 PRINT "TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA"
90 PRINT "SUCCESSFULLY FOR A TEN-YEAR TERM OF OFFICE.":PRINT
95 D1=0:P1=0
100 Z=0:P=95:S=2800:H=3000:E=H-S
110 Y=3:A=H/Y:I=5:Q=1
210 D=0
215 PRINT:PRINT:PRINT "HAMURABI:  I BEG TO REPORT TO YOU,":Z=Z+1
217 PRINT "IN YEAR"Z","D"PEOPLE STARVED,"I"CAME TO THE CITY."
218 P=P+I
227 IF Q>0 THEN 230
228 P=INT(P/2)
229 PRINT "A HORRIBLE PLAGUE STRUCK!  HALF THE PEOPLE DIED."
230 PRINT "POPULATION IS NOW"P
232 PRINT "THE CITY NOW OWNS"A"ACRES."
235 PRINT "YOU HARVESTED"Y"BUSHELS PER ACRE."
250 PRINT "RATS ATE"E"BUSHELS."
260 PRINT "YOU NOW HAVE"S"BUSHELS IN STORE.":PRINT
270 IF Z=11 THEN 860
310 C=INT(10*RND(1)):Y=C+17
312 PRINT "LAND IS TRADING AT"Y"BUSHELS PER ACRE."
320 PRINT "HOW MANY ACRES DO YOU WISH TO BUY";
321 INPUT Q:IF Q<0 THEN 850
322 IF Y*Q<=S THEN 330
323 GOSUB 710
324 GOTO 320
330 IF Q=0 THEN 340
331 A=A+Q:S=S-Y*Q:C=0
334 GOTO 400
340 PRINT "HOW MANY ACRES DO YOU WISH TO SELL";
341 INPUT Q:IF Q<0 THEN 850
342 IF Q<A THEN 350
343 GOSUB 720
344 GOTO 340
350 A=A-Q:S=S+Y*Q:C=0
400 PRINT
410 PRINT "HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE";
411 INPUT Q
412 IF Q<0 THEN 850
418 REM *** TRYING TO USE MORE GRAIN THAN IN THE SILOS?
420 IF Q<=S THEN 430
421 GOSUB 710
422 GOTO 410
430 S=S-Q:C=1:PRINT
440 PRINT "HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED";
441 INPUT D:IF D=0 THEN 511
442 IF D<0 THEN 850
444 REM *** TRYING TO PLANT MORE ACRES THAN YOU OWN?
445 IF D<=A THEN 450
446 GOSUB 720
447 GOTO 440
449 REM *** ENOUGH GRAIN FOR SEED?
450 IF INT(D/2)<S THEN 455
452 GOSUB 710
453 GOTO 440
454 REM *** ENOUGH PEOPLE TO TEND THE CROPS?
455 IF D<10*P THEN 510
460 PRINT "BUT YOU HAVE ONLY"P"PEOPLE TO TEND THE FIELDS. NOW THEN,"
470 GOTO 440
510 S=S-INT(D/2)
511 GOSUB 800
512 REM *** A BOUNTYFULL HARVEST!!
515 Y=C:H=D*Y:E=0
521 GOSUB 800
522 IF INT(C/2)<>C/2 THEN 530
523 REM *** THE RATS ARE RUNNING WILD!!
525 E=INT(S/C)
530 S=S-E+H
531 GOSUB 800
532 REM *** LET'S HAVE SOME BABIES
533 I=INT(C*(20*A+S)/P/100+1)
539 REM *** HOW MANY PEOPLE HAD FULL TUMMIES?
540 C=INT(Q/20)
541 REM *** HORRORS, A 15% CHANCE OF PLAGUE
542 Q=INT(10*(2*RND(1)-.3))
550 IF P<C THEN 210
551 REM *** STARVE ENOUGH FOR IMPEACHMENT?
552 D=P-C:IF D>.45*P THEN 560
553 P1=((Z-1)*P1+D*100/P)/Z
555 P=C:D1=D1+D:GOTO 215
560 PRINT:PRINT "YOU STARVED"D"PEOPLE IN ONE YEAR!!!"
565 PRINT "DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY"
566 PRINT "BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE"
567 PRINT "ALSO BEEN DECLARED 'NATIONAL FINK' !!":GOTO 990
710 PRINT "HAMURABI:  THINK AGAIN. YOU HAVE ONLY"
711 PRINT S"BUSHELS OF GRAIN. NOW THEN,"
712 RETURN
720 PRINT "HAMURABI:  THINK AGAIN. YOU OWN ONLY"A"ACRES. NOW THEN,"
730 RETURN
800 C=INT(RND(1)*5)+1
801 RETURN
850 PRINT:PRINT "HAMURABI:  I CANNOT DO WHAT YOU WISH."
855 PRINT "GET YOURSELF ANOTHER STEWARD!!!!!"
857 GOTO 990
860 PRINT "IN YOUR 10-YEAR TERM OF OFFICE,"P1"PERCENT OF THE"
862 PRINT "POPULATION STARVED PER YEAR ON AVERAGE, I.E., A TOTAL OF"
865 PRINT D1"PEOPLE DIED!!":L=A/P
870 PRINT "YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH"
875 PRINT L"ACRES PER PERSON.":PRINT
880 IF P1>33 THEN 565
885 IF L<7 THEN 565
890 IF P1>10 THEN 940
892 IF L<9 THEN 940
895 IF P1>3 THEN 960
896 IF L<10 THEN 960
900 PRINT "A FANTASTIC PERFORMANCE!!!  CHARLEMANGE, DISRAELI, AND"
905 PRINT "JEFFERSON COMBINED COULD NOT HAVE DONE BETTER!":GOTO 990
940 PRINT "YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV."
945 PRINT "THE PEOPLE (REMAINING) FIND YOU AN UNPLEASANT RULER, AND,"
950 PRINT "FRANKLY, HATE YOUR GUTS!":GOTO 990
960 PRINT "YOUR PERFORMANCE COULD HAVE BEEN SOMEWHAT BETTER, BUT"
965 PRINT "REALLY WASN'T TOO BAD AT ALL. ";
966 PRINT INT(P*.8*RND(1));"PEOPLE WOULD"
970 PRINT "DEARLY LIKE TO SEE YOU ASSASSINATED BUT WE ALL HAVE OUR"
975 PRINT "TRIVIAL PROBLEMS."
990 PRINT:FOR N=1 TO 10:PRINT CHR;:NEXT N
995 PRINT "SO LONG FOR NOW.":PRINT
999 END
```
