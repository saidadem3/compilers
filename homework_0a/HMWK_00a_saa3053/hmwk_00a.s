# Adem, Said A.
# saa3053
# 2019-09-04

# Here're the command to assemble, link, and run this file:
#
#   as -o hw.o hmwk_00a.s
#   gcc -static -o test hw.o
#   ./test

.global main

.text
main:
  movq    $msg, %rdi    # Arg 1: string.
  call    puts          # puts( const char *str )

  movl    $0, %edi      # Arg 1: exit code
  call    exit          # exit( int status )

.data

# Need asciz to get NUL byte on end.
# puts adds a \n so don't need one here.
msg:
  .asciz  "Hello, world, from puts!"
