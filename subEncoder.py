DEBUGMODE = 1

def IntInput(text, range = (0, 9999), default = 0):
    if(DEBUGMODE):
        return default
    while True:
        try:
            Input = input(text + f'({range[0]} - {range[1]}): ')
            Input = int(Input)
            if range[0] <= Input < range[1]:
                return Input
            else:
                print("Out of Range! Try again!")
        except:
            print("Incorrect Input! Try again!")
        
        

# Define constants and initial values
BitString = "0000"
ShockerID = IntInput("ShockerID", (0, 4096), 3377)
Operation = IntInput("Mode", (1, 3), 0 ) # More Testing needed!
Power = IntInput("Power", (0,100), 25)
Null1 = 0
Null2 = 0
Null3 = 0

# Convert ShockerID to binary string with leading zeros
ShockerID = ''.join(format(byte, '08b') for byte in ShockerID.to_bytes(2, byteorder='big'))
Operation = ''.join(format(byte, '08b') for byte in Operation.to_bytes(2, byteorder='big'))
Power     = ''.join(format(byte, '08b') for byte in Power    .to_bytes(2, byteorder='big'))

print("AAA" + ShockerID)
# Define the bit array to be encoded
BytesToEncode = [int(bit) for bit in f"0000" + str(110100110001) + "000000110" + "0011001" + "010" + "11" + "010" + "000"]

# Define silence values
Silence = -300

# Initialize variables for Raw Data generation
RawDatas = ''
Spaces = 1
SpaceLimit = '512'
RawDataCount = 0

# Generate Raw Data based on bit array
for byte in BytesToEncode:
    if byte == 1:
        RawDatas += f'{1200} {Silence} '  # 1
    else:
        RawDatas += f'{400} {Silence} '   # 0

# Add final silence and create Raw File output
RawDatas += f'{0} {-500000}'
RawFileOut = f'''
Filetype: {"Flipper SubGhz RAW File"}
Version: {1}
Frequency: {434075000}
Preset: {"FuriHalSubGhzPresetOok270Async"}
Protocol: {"RAW"}
RAW_Data: {RawDatas}
'''

# Print the Raw File output
print(RawFileOut)
