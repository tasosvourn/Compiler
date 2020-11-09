j Lmain
L0:
sw $ra, ($sp)
L1:
lw $t1,-12($sp)
lw $t2,-16($sp)
add $t1, $t1, $t2
sw $t1,-24($sp)
L2:
lw $t1,-24($sp)
sw $t1,-20($sp)
L3:
lw $t1,-12($sp)
lw $t2,-20($sp)
mul $t1, $t1, $t2
sw $t1,-28($sp)
L4:
lw $t1,-28($sp)
li $t2,12
add $t1, $t1, $t2
sw $t1,-32($sp)
L5:
lw $t1,-32($sp)
sw $t1,-16($sp)
L6:
li $v0, 1
lw $t0,-16($sp)
move $a0, $t0
syscall
L7:
lw $t1,-12($sp)
li $t2,10
add $t1, $t1, $t2
sw $t1,-36($sp)
L8:
lw $t1,-36($sp)
lw $t0, -8($sp)
sw $t1, ($t0)
L9:
lw $ra, ($sp)
jr $ra
L10:
sw $ra, ($sp)
L11:
li $v0, 1
lw $t0,-12($sp)
move $a0, $t0
syscall
L12:
lw $t1,-12($sp)
li $t2,20
bge $t1, $t2, L14
L13:
j L23
L14:
li $v0, 1
lw $t0,-12($sp)
move $a0, $t0
syscall
L15:
lw $t1,-12($sp)
li $t2,0
blt $t1, $t2, L17
L16:
j L19
L17:
j L22
L18:
j L19
L19:
lw $t1,-12($sp)
li $t2,20
sub $t1, $t1, $t2
sw $t1,-16($sp)
L20:
lw $t1,-16($sp)
sw $t1,-12($sp)
L21:
j L14
L22:
j L24
L23:
li $v0, 1
li $t0,1234
move $a0, $t0
syscall
L24:
lw $ra, ($sp)
jr $ra
Lmain:
add $sp, $sp, 40
move $s0, $sp
L25:
L26:
li $v0, 5
syscall
move $t0, $v0
sw $t0,-12($s0)
L27:
li $v0, 5
syscall
move $t0, $v0
sw $t0,-16($s0)
L28:
add $fp, $sp, 40
lw $t0,-12($s0)
sw $t0, -12($fp)
L29:
lw $t0,-16($s0)
sw $t0, -16($fp)
L30:
add $t0, $sp, -24
sw $t0, -8($fp)
L31:
sw $sp, -4($fp)
add $sp, $sp, 40
jal L0
add $sp, $sp, -40
L32:
lw $t1,-24($s0)
sw $t1,-20($s0)
L33:
li $v0, 1
lw $t0,-16($s0)
move $a0, $t0
syscall
L34:
li $v0, 1
lw $t0,-20($s0)
move $a0, $t0
syscall
L35:
li $t1,21
sw $t1,-20($s0)
L36:
add $fp, $sp, 20
lw $t0,-20($s0)
sw $t0, -12($fp)
L37:
sw $sp, -4($fp)
add $sp, $sp, 20
jal L10
add $sp, $sp, -20
L38:
li $t1,100
sw $t1,-20($s0)
L39:
lw $t1,-20($s0)
li $t2,1000
blt $t1, $t2, L41
L40:
j L44
L41:
lw $t1,-20($s0)
li $t2,100
add $t1, $t1, $t2
sw $t1,-28($s0)
L42:
lw $t1,-28($s0)
sw $t1,-20($s0)
L43:
j L39
L44:
li $v0, 1
lw $t0,-20($s0)
move $a0, $t0
syscall
L45:
li $t1,10
sw $t1,-20($s0)
L46:
lw $t1,-20($s0)
li $t2,1
bne $t1, $t2, L49
L47:
li $v0, 1
li $t0,1
move $a0, $t0
syscall
L48:
j L66
L49:
lw $t1,-20($s0)
li $t2,2
bne $t1, $t2, L52
L50:
li $v0, 1
li $t0,2
move $a0, $t0
syscall
L51:
j L66
L52:
lw $t1,-20($s0)
li $t2,10
bne $t1, $t2, L66
L53:
li $t1,0
sw $t1,-32($s0)
L54:
lw $t1,-20($s0)
li $t2,10
bge $t1, $t2, L56
L55:
j L58
L56:
li $t1,1
lw $t2,-32($s0)
add $t1, $t1, $t2
sw $t1,-32($s0)
L57:
li $v0, 1
lw $t0,-20($s0)
move $a0, $t0
syscall
L58:
lw $t1,-20($s0)
li $t2,5
bge $t1, $t2, L60
L59:
j L64
L60:
li $t1,1
lw $t2,-32($s0)
add $t1, $t1, $t2
sw $t1,-32($s0)
L61:
li $v0, 1
lw $t0,-20($s0)
move $a0, $t0
syscall
L62:
lw $t1,-20($s0)
li $t2,1
sub $t1, $t1, $t2
sw $t1,-36($s0)
L63:
lw $t1,-36($s0)
sw $t1,-20($s0)
L64:
li $t1,0
lw $t2,-32($s0)
bne $t1, $t2, L53
L65:
j L66
L66:

L67:
