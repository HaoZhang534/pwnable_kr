#!/usr/bin/expect -f
spawn ssh unlink@pwnable.kr -p2222
expect "password"
send "guest\n"
interact