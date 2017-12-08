set r11 43
set r12 55

set r21 44
set r22 52

set r31 46
set r32 50

set r41 47
set r42 74

set r51 55
set r52 65

set r61 57
set r62 60

set r71 58
set r72 67

set r81 60
set r82 64

set r91 60
set r92 64

set r01 64
set r02 74


play folded.vmd
#display rendermode GLSL

set var "resid $r11 $r12 $r21 $r22 $r31 $r32 $r41 $r42 $r51 $r52 $r61 $r62 $r71 $r72 $r81 $r82 $r91 $r92 $r01 $r02 and name CA"
mol selection $var
mol representation cpk
mol addrep top
mol modcolor 8 0 ColorID 0
mol modmaterial 8 0 Glossy
draw color 16

set sel1 [atomselect 0 "resid $r91 and name CA"]
set var1 [$sel1 get {x y z}]
set test1 [lindex $var1 0]
set sel2 [atomselect 0 "resid $r92 and name CA"]
set var2 [$sel2 get {x y z}]
set test2 [lindex $var2 0]
draw line $test1 $test2 style dashed width 5


set sel1 [atomselect 0 "resid $r01 and name CA"]
set var1 [$sel1 get {x y z}]
set test1 [lindex $var1 0]
set sel2 [atomselect 0 "resid $r02 and name CA"]
set var2 [$sel2 get {x y z}]
set test2 [lindex $var2 0]
draw line $test1 $test2 style dashed width 5
