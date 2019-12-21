* FLIP FLOP SCHEMATIC LEVEL

.subckt flip-flop c cn d q rn
xm22 q net92 vdd vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+ pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm21 net79 c net77 vdd pe w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)'
xm20 net77 net92 vdd vdd pe w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)'
xm15 net92 rn vdd vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+  pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm14 net92 net79 vdd vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+  pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm13 net79 cn net54 vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+  pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm11 net84 cn net85 vdd pe w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)'
xm10 net85 net54 vdd vdd pe w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)'
xm6 net85 rn vdd vdd pe w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+ pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)'
xm4 net54 net84 vdd vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+  pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm3 net84 c net13 vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+  pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm0 net13 d vdd vdd pe w=660.0n l=180.0n as=3.168e-13 ad=3.168e-13 ps=2.28e-06
+ pd=2.28e-06 nrs=0.409091 nrd=0.409091 m='(1*1)' par1='(1*1)'
xm23 q net92 gnd gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+ pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm19 net81 net92 gnd gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm18 net79 cn net81 gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm17 net67 net79 gnd gnd ne w=440.0n l=180.0n as=2.112e-13 ad=2.112e-13 ps=1.84e-06
+  pd=1.84e-06 nrs=0.613636 nrd=0.613636 m='(1*1)' par1='(1*1)' xf_subext=0
xm16 net92 rn net67 gnd ne w=440.0n l=180.0n as=2.112e-13 ad=2.112e-13 ps=1.84e-06
+  pd=1.84e-06 nrs=0.613636 nrd=0.613636 m='(1*1)' par1='(1*1)' xf_subext=0
xm12 net54 c net79 gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm9 net37 net54 gnd gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm8 net33 rn net37 gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm7 net84 c net33 gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+ pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm5 net54 net84 gnd gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm2 net13 cn net84 gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+  pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
xm1 net13 d gnd gnd ne w=220.0n l=180.0n as=1.056e-13 ad=1.056e-13 ps=1.4e-06
+ pd=1.4e-06 nrs=1.22727 nrd=1.22727 m='(1*1)' par1='(1*1)' xf_subext=0
.ends
