# HID to ASCII key mappings for US keyboard
hid_map = {
    4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 
    14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 
    24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 
    34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 40: 'ENTER', 44: ' ', 45: '-', 46: '=',
    47: '[', 48: ']', 49: '\\', 51: ';', 52: "'", 53: '`', 54: ',', 55: '.', 56: '/',
    57: 'CAPSLOCK', 58: 'F1', 59: 'F2', 60: 'F3', 61: 'F4', 62: 'F5', 63: 'F6', 64: 'F7',
    65: 'F8', 66: 'F9', 67: 'F10', 68: 'F11', 69: 'F12'
}

# Shift key for upper case letters and special characters
shift_map = {
    4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 
    14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 
    24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 
    34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 45: '_', 46: '+', 47: '{', 48: '}', 
    49: '|', 51: ':', 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'
}

def translate_hid_data(hid_data):
    result = []
    shift = False
    
    for byte in hid_data:
        # Check for modifier keys
        if byte == 0x02:
            shift = True
        elif byte == 0x00:
            shift = False
        elif byte in hid_map:
            if shift:
                result.append(shift_map.get(byte, ''))
            else:
                result.append(hid_map.get(byte, ''))
    
    return ''.join(result)

# Adjusted function to read and process the specific HID data format from the file
def read_hid_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        translated_data = []
        
        for line in lines:
            # Split the line into bytes (each 8 bytes long, but we only need the third byte)
            hex_data = line.strip()
            if len(hex_data) >= 6:
                key_code = int(hex_data[4:6], 16)
                
                # Ignore empty key press (key code 0)
                if key_code != 0:
                    translated_data.append(key_code)
                    
        return translated_data

# Example usage
hid_data = read_hid_file('hid.txt')
translated_text = translate_hid_data(hid_data)
print(f'Translated Text: {translated_text}')

