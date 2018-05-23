#!/usr/bin/expect -f
spawn ssh memcpy@pwnable.kr -p2222
expect "password"
send "guest\n"
interact