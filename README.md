# Ericsson_Tasks_Krol_Krzysztof

Uznałem, że profesjonalne będzie napisanie wszystkich komentarzy w projekcie w języku angielskim. Stąd również konsekwentnie angielski ten oto dokument readme dotyczący zadań.

In this repository I present my solutions to the tasks i was assigned to complete.

I have decided to take on every task in a different programming language in order to present my knowledge and skills regarding their usage.
Task 1 is written in C, Task 2 in C++ and the facultative Task 3 in Python. 

Task 3 also requires installing the keyboard module which can be done with the command (provided pip is already installed):
>pip install keyboard

I want to make a comment about my approach towards Task 1. I think my solution would be optimal or just more versitile if i opted to represent every object read as a struct and not just a buffer (string).

For example:<br/>
struct object{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;char id[4];<br/>
&nbsp;&nbsp;&nbsp;&nbsp;char msg[3];<br/>
&nbsp;&nbsp;&nbsp;&nbsp;char control;<br/>
};<br/>
and operate on those values after copying data from buffer to struct using memcpy function.

However taking into account the triviality of this specific task i chose to skip that operation for the sake of sheer simplicity.
