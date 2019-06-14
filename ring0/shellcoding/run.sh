nasm -f elf64 -o main.o main.s
ld -o main.x main.o
./main.x

rm main.o
rm main.x
