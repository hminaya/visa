ln_new =['Algo', 'Mas', 'f11', '1', '123']
valid_visa_types = [
        ' cr1', ' dv1', 'f11', ' f21', ' f22', ' f24', ' fx1', ' fx2',
       ' ir1', ' ir2', ' ir5', ' sb1', ' se1', ' se2', ' cr2', ' dv2',
       ' dv3', ' e22', ' e23', ' e31', ' e34', ' e35', ' f12', ' f31',
       ' f32', ' f33', ' f41', ' f42', ' f43', ' fx3', ' sq2', ' f23',
       ' f25', ' ib2', ' ib3', ' iw1', ' e21', ' se3', ' e32', ' i51',
       ' i52', ' i53', ' t51', ' t52', ' ir4', ' e14', ' sq1', ' sq3',
       ' ib1', ' ew3', ' ew4', ' ew5', ' ih3', ' ih4', ' e11', ' ir3',
       ' e15', ' sd1', ' iw2', ' bx1', ' su3', ' c51', ' c52',
       ' c53', ' e13', ' t53', ' am1', ' am2', ' si1', ' si2', ' si3',
       ' sr1', ' sr2', ' sr3', ' sd2', ' sd3', ' bc1'
]

quantity = ''
visa_class = ''
post = ''

for w in ln_new:

    #print(w)
    if w in valid_visa_types:
        
        loc_class = ln_new.index(w)
        loc_end = len(ln_new)

        visa_class = w

        # Everything to the right is the Quantity
        for x in range(loc_class+1, loc_end):
            quantity = f"{quantity}" + f"{ln_new[x]}"

        # Everything to the left is the Post
        for x in range(0, loc_class):
            post = f"{post} " + f"{ln_new[x]}"

ln_new = f"{post}, {visa_class}, {quantity}\n"

print(ln_new)