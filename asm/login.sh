#!/usr/bin/expect -f
spawn ssh asm@pwnable.kr -p2222
expect "password"
send "guest\n"
interact