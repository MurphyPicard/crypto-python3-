I made these 3 programs tonight, using Python, because for the last few weeks
I've been doing nothing but learning Ruby on Rails and I kind of missed Python.

All programs are functioning correctly, yay!

initials.py is quick and easy
-   just put in a regular name like michael jordan
-   it'll tell you that the initials are MJ

caesar.py is a little more interesting
-   type a number in the command line when you run the program initially
-   then type a message when prompted
-   this program will return a new encrypted message with each letter rotated by
    the number specified

vigenere.py is a little more complex, but reused some of the code from caesar
-   when prompted, type a message, like 'Hello, young kid!', or whatever
-   when prompted, type a keyword, like 'bad', or whatever
-   the program will return an encrypted message, according to the following:
-   keyword letters:
-   a = 0, b = 1, c = 2, d = 3, ... Z or z = 25 are used to rotate the letters in the message

-   example:
-   message - Hello, young kid!
-   keyword - badba__dbadb_adb    ('bad' revolves)
-   becomes - Ieomo, bpuqh kle!    (cool, huh?)

Making these was very enjoyable
