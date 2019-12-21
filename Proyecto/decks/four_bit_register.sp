* ------------------------------
* 4 bit register SCHEMATIC LEVEL
* ------------------------------

* Flip-flop schematic netlist
.include flip-flop.sp 

.subckt four_bit_register clk en resetn d1 d2 d3 d4 q1 q2 q3 q4
	X0 clk en en_clk and * And gate, which enables the clock signal
	X1 en_clk clkn inv * Inverted clock signal
	X2 en_clk clkn d1 q1 resetn
	X3 en_clk clkn d2 q2 resetn
	X4 en_clk clkn d3 q3 resetn
	X5 en_clk clkn d4 q4 resetn
.ends
