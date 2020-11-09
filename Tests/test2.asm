j Lmain
L0:
sw $ra, ($sp)
L1:
lw $t1,-12($sp)
lw $t0, -8($sp)
sw $t1, ($t0)
L2:
lw $ra, ($sp)
jr $ra
L3:
sw $ra, ($sp)
L4:
lw $t1,-12($sp)
lw $t0, -8($sp)
sw $t1, ($t0)
L5:
lw $ra, ($sp)
jr $ra
L6:
sw $ra, ($sp)
L7:
add $fp, $sp, 28
add $t0, $sp, -12
sw $t0, -8($fp)L8:
sw $sp, -4($fp)sw $sp, -4($fp)add $sfp, $sp, 28
jal L3
add $sfp, $sp, -28
L9:
lw $t1,-12($sp)
sw $t1,-16($s0)
L10:
lw $t0, -4($sp)
add $t0, $t0, -12
lw $t1,($t0)
lw $t0, -8($sp)
sw $t1, ($t0)
L11:
lw $ra, ($sp)
jr $ra
L12:
sw $ra, ($sp)
L13:
lw $t1,-12($s0)
lw $t2,-16($s0)
bne $t1, $t2, L18
L14:
j L15
L15:
lw $t1,-12($s0)
li $t2,1
add $t1, $t1, $t2
sw $t1,-16($sp)
L16:
lw $t1,-16($sp)
sw $t1,-12($s0)
L17:
j L13
L18:
lw $ra, ($sp)
jr $ra
Lmain:
add $sp, $sp, 96
move $s0, $sp
L19:
L20:
lw $t1,-20($s0)
lw $t2,-40($s0)
beq $t1, $t2, L22
L21:
j L29
L22:
lw $t1,-44($s0)
li $t2,0
blt $t1, $t2, L24
L23:
j L29
L24:
lw $t1,-36($s0)
li $t2,4
div $t1, $t1, $t2
sw $t1,-52($s0)
L25:
lw $t1,-28($s0)
lw $t2,-52($s0)
add $t1, $t1, $t2
sw $t1,-56($s0)
L26:
lw $t1,-56($s0)
li $t2,9
sub $t1, $t1, $t2
sw $t1,-60($s0)
L27:
lw $t1,-60($s0)
sw $t1,-20($s0)
L28:
j L30
L29:
li $t1,0
sw $t1,-20($s0)
L30:
lw $t1,-12($s0)
lw $t2,-16($s0)
bne $t1, $t2, L35
L31:
j L32
L32:
lw $t1,-12($s0)
li $t2,1
add $t1, $t1, $t2
sw $t1,-64($s0)
L33:
lw $t1,-64($s0)
sw $t1,-12($s0)
L34:
j L30
L35:
li $t1,0
sw $t1,-20($s0)
L36:
j L43
L37:
li $t1,90
li $t2,34
add $t1, $t1, $t2
sw $t1,-68($s0)
L38:
lw $t1,-68($s0)
sw $t1,-24($s0)
L39:
j L41
L40:
j L37
L41:
li $t1,9
sw $t1,-28($s0)
L42:
j L35
L43:
lw $t1,-28($s0)
li $t2,1
bne $t1, $t2, L46
L44:
li $t1,1
sw $t1,-20($s0)
L45:
j L52
L46:
lw $t1,-28($s0)
li $t2,2
bne $t1, $t2, L49
L47:
li $t1,2
sw $t1,-20($s0)
L48:
j L52
L49:
lw $t1,-28($s0)
li $t2,3
bne $t1, $t2, L52
L50:
li $t1,3
sw $t1,-20($s0)
L51:
j L52
L52:
li $t1,0
sw $t1,-72($s0)
L53:
lw $t1,-20($s0)
lw $t2,-40($s0)
blt $t1, $t2, L55
L54:
j L57
L55:
li $t1,1
lw $t2,-72($s0)
add $t1, $t1, $t2
sw $t1,-72($s0)
L56:
li $t1,0
sw $t1,-32($s0)
L57:
lw $t1,-28($s0)
lw $t2,-40($s0)
bgt $t1, $t2, L59
L58:
j L62
L59:
li $t1,1
lw $t2,-72($s0)
add $t1, $t1, $t2
sw $t1,-72($s0)
L60:
li $t1,9
lw $t2,-48($s0)
add $t1, $t1, $t2
sw $t1,-76($s0)
L61:
lw $t1,-76($s0)
sw $t1,-36($s0)
L62:
li $t1,0
lw $t2,-72($s0)
bne $t1, $t2, L52
L63:
lw $t1,-20($s0)
li $t2,1
add $t1, $t1, $t2
sw $t1,-80($s0)
L64:
add $fp, $sp, 20
lw $t0,-80($s0)
sw $t0, -268($fp)L65:
L66:
sw $sp, -4($fp)sw $sp, -4($fp)add $sfp, $sp, 20
jal L12
add $sfp, $sp, -20
L67:
add $fp, $sp, 28
lw $t0,-20($s0)
sw $t0, -280($fp)L68:
add $t0, $sp, -84
sw $t0, -8($fp)L69:
sw $sp, -4($fp)sw $sp, -4($fp)add $sfp, $sp, 28
jal L0
add $sfp, $sp, -28
L70:
lw $t1,-12($s0)
lw $t2,-84($s0)
add $t1, $t1, $t2
sw $t1,-88($s0)
L71:
lw $t1,-88($s0)
sw $t1,-12($s0)
L72:
add $fp, $sp, 28
L73:
lw $t0,-20($s0)
sw $t0, -304($fp)L74:
add $t0, $sp, -92
sw $t0, -8($fp)L75:
sw $sp, -4($fp)sw $sp, -4($fp)add $sfp, $sp, 28
jal L0
add $sfp, $sp, -28
L76:
add $fp, $sp, 20
lw $t0,-92($s0)
sw $t0, -316($fp)L77:
sw $sp, -4($fp)sw $sp, -4($fp)add $sfp, $sp, 20
jal L12
add $sfp, $sp, -20
L78:
li $v0, 5
syscall
move $t0, $v0
sw $t0,-12($s0)
L79:

L80:
