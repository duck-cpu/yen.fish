# getting the initial values from the user.
RX = input("Enter your glasses prescription (SPH CYL AXIS): ")

# wrapping entire program in a 'try' block to ensure values are valid.
try:
    # divide the input into 3 variables.
    sph, cyl, axis = RX.split()
    sph = float(sph)
    cyl = float(cyl)
    axis = int(axis)

    # makes sure the axis is not below 0 or above 180.
    if axis < 0 or axis > 180:
        print("Error: Axis value must be between 0 and 180.")
    else:
        # if the axis is less than or equal to 89, add 90, and if it's more than 89, subtract 90.
        if axis <= 89:
            axis += 90
        else:
            axis -= 90
        
        # adds the sphere to the cylinder
        sph += cyl 
        
        # flips cyl sign
        cyl = -cyl

        # assigns variable the new transposed prescription.
        newRX = (f"{sph:+.2f} {cyl:+.2f} X{axis:03d}")
        print("Your new prescription is:", newRX)
        
except ValueError:
    print("Error: Please enter valid values for the RX.")