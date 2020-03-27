	.data 

array: .word 4, 21, 29, 27, 25, 19, 46, 2, 14, 34 
	# 4 = 0x0004
	# 21 = Ox0015
	# 29 = 0x001d
	# 27 = 0x001b
	# 50 = 0x0032
	# 19 = 0x0013
	# 46 = 0x002e
	# 2 = Ox0002
	# 14 = 0x000e
	# 34 = 0x0022
new_line: .asciiz ",\n"

	.text
	.globl main
main: 
	li $t0, 0 
	
	# $t0 is the index of the array
start_loop: # print the unsorted array
	seq $t1, $t0, 40
	# if $t0 = 40, set $t1 to 1, otherwise $t1 = 0
	bnez $t1, end_loop
	# if $t1 != 0, branch to end_loop

	li $v0, 1
	# $v0 is holding 1
	lw $a0, array($t0)
	# set $a0 to the contents of the effective memeory word address
	syscall
	
	# print a new line
	li $v0, 4  
	# syscall 4 = print string
    	la $a0, new_line    
    	# loads the address of new_line
    	syscall
	
	# increasing the index by 4 'cause 1 word = 4 bytes.
	# 40 comes from 10 numbers to be sorted * 4 bytes = 40
	add $t0, $t0, 4
	# add 1 to $t0 
	b start_loop
	# branch to start_loop

end_loop: # exiting the loop of printing unordered integers
	
	la $a0, array
	li $s3, 0
	li $a1, 0
	li $s4, 0
	# loading the address of the array into $a0
check_array:

	seq $s3, $a1, 40
	# set $s3 = 1 if $a1 = 40. Otherwise, leave $s3 = 0
	bnez $s3, start_over
	# if $s3 != 0, jump to orderedLoop_start 
	
	lw $s0, 0($a0)
	# load word at position 0 into $s0
	lw $s1, 4($a0)
	# load word at position 4 into $s1
	
	sgt $s4, $s0, $s1
	# if $s0 > $s1, set $s4 = 1. Otherwise, $s4 = 0
	bnez $s4, swap
	# branch to swap if $s4 != 0
	
	add $a0, $a0, 4
	# add 4 to the address of the array to get to the next position
	add $a1, $a1, 4
	# add 4 to the inner index
	add $k0, $k0, 4
	# add 4 to the outer loop index
	b check_array
	# branch back to the array checking
	
swap:
	sw $s0, 4($a0)
	# store word $s0 at address of $s0
	sw $s1, 0($a0)
	# store word $s1 at address of $s1
	
	add $a0, $a0, 4
	# add 4 to the address of the array to get to the next position
	add $a1, $a1, 4
	# add 4 to the inner loop index
	add $k0, $k0, 4
	# add 4 to the outer loop index
	b check_array
	# branch back to the array checking
	
start_over: # checking if we have to start the loop again
	seq $k1, $k0, 400
	# if $k0 = 400, set $k1 = 1. Otherwise, $k1 = 0
	beqz $k1, end_loop
	# if $k1 = 0, jump back in the loop
	
	### reseting everything in the loop ###
	li $t0, 0
	# $t0 is holding 0
	#li $t1, 0
	# $t1 is holding 0
	#li $v0, 0
	# $v0 is holding 0
orderedLoop_start: # print the sorted array 
	seq $t1, $t0, 40
	# if $t0 = 40, set $t1 to 1, otherwise $t1 = 0
	bnez $t1, orderedLoop_end
	# if $t1 != 0, branch to end_loop

	li $v0, 1
	# $v0 is holding 1
	lw $a0, array($t0)
	# set $a0 to the contents of the effective memeory word address
	syscall
	
	# print a new line
	li $v0, 4  
	# syscall 4 = print string
    	la $a0, new_line    
    	# loads the address of new_line
    	syscall
	
	# increasing the index by 4 'cause 1 word = 4 bytes.
	# 40 comes from 10 numbers to be sorted * 4 bytes = 40
	add $t0, $t0, 4
	# add 1 to $t0 
	b orderedLoop_start
	# branch to start_loop
	
orderedLoop_end:   # exit the program

	li $v0, 10
	syscall
	
