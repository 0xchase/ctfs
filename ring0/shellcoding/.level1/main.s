global _start

section .text

_start:
  
    xor rdx, rdx
    mov  qword rbx, 'cat f.t'
    shr rbx, 0x8
    push rbx
    mov rdi, rsp
    push rdi
    mov rsi, rsp
    mov al, 0x3b
    syscall

section .rodata
  msg: db "Hello, world!", 10
  msglen: equ $ - msg
