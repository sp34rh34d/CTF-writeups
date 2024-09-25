## Name: Secret Note
#### Category: Forensics
#### Difficulty: Medium
#### Description: I was told to never write down my passwords on a sticky note, so instead I wrote them down on my computer!

## Procedure
checking the first 20 packets, we can see some USB device traffic
```
tshark -r capture.pcapng  | head -n 20
    1   0.000000         host → 3.1.0        USB 36 GET DESCRIPTOR Request DEVICE
    2   0.000000        3.1.0 → host         USB 46 GET DESCRIPTOR Response DEVICE
    3   0.000000         host → 3.1.0        USB 36 GET DESCRIPTOR Request CONFIGURATION
    4   0.000000        3.1.0 → host         USB 87 GET DESCRIPTOR Response CONFIGURATION
    5   0.000000         host → 3.1.0        USB 36 SET CONFIGURATION Request
    6   0.000000        3.1.0 → host         USB 28 SET CONFIGURATION Response
    7   0.000000         host → 3.2.0        USB 36 GET DESCRIPTOR Request DEVICE
    8   0.000000        3.2.0 → host         USB 46 GET DESCRIPTOR Response DEVICE
    9   0.000000         host → 3.2.0        USB 36 GET DESCRIPTOR Request CONFIGURATION
   10   0.000000        3.2.0 → host         USB 53 GET DESCRIPTOR Response CONFIGURATION
   11   0.000000         host → 3.2.0        USB 36 SET CONFIGURATION Request
   12   0.000000        3.2.0 → host         USB 28 SET CONFIGURATION Response
   13   0.000000         host → 3.3.0        USB 36 GET DESCRIPTOR Request DEVICE
   14   0.000000        3.3.0 → host         USB 46 GET DESCRIPTOR Response DEVICE
   15   0.000000         host → 3.3.0        USB 36 GET DESCRIPTOR Request CONFIGURATION
   16   0.000000        3.3.0 → host         USB 53 GET DESCRIPTOR Response CONFIGURATION
   17   0.000000         host → 3.3.0        USB 36 SET CONFIGURATION Request
   18   0.000000        3.3.0 → host         USB 28 SET CONFIGURATION Response
   19   0.084582        3.1.1 → host         USB 35 URB_INTERRUPT in
   20   0.084639         host → 3.1.1        USB 27 URB_INTERRUPT in

```

First we need to identify USB or Bluetooth Traffic, If the capture is of USB devices, use the filter ```usb || usb.capdata```

```
tshark -r capture.pcapng  -Y "usb || usb.capdata" | head -n 20
    1   0.000000         host → 3.1.0        USB 36 GET DESCRIPTOR Request DEVICE
    2   0.000000        3.1.0 → host         USB 46 GET DESCRIPTOR Response DEVICE
    3   0.000000         host → 3.1.0        USB 36 GET DESCRIPTOR Request CONFIGURATION
    4   0.000000        3.1.0 → host         USB 87 GET DESCRIPTOR Response CONFIGURATION
    5   0.000000         host → 3.1.0        USB 36 SET CONFIGURATION Request
    6   0.000000        3.1.0 → host         USB 28 SET CONFIGURATION Response
    7   0.000000         host → 3.2.0        USB 36 GET DESCRIPTOR Request DEVICE
    8   0.000000        3.2.0 → host         USB 46 GET DESCRIPTOR Response DEVICE
    9   0.000000         host → 3.2.0        USB 36 GET DESCRIPTOR Request CONFIGURATION
   10   0.000000        3.2.0 → host         USB 53 GET DESCRIPTOR Response CONFIGURATION
   11   0.000000         host → 3.2.0        USB 36 SET CONFIGURATION Request
   12   0.000000        3.2.0 → host         USB 28 SET CONFIGURATION Response
   13   0.000000         host → 3.3.0        USB 36 GET DESCRIPTOR Request DEVICE
   14   0.000000        3.3.0 → host         USB 46 GET DESCRIPTOR Response DEVICE
   15   0.000000         host → 3.3.0        USB 36 GET DESCRIPTOR Request CONFIGURATION
   16   0.000000        3.3.0 → host         USB 53 GET DESCRIPTOR Response CONFIGURATION
   17   0.000000         host → 3.3.0        USB 36 SET CONFIGURATION Request
   18   0.000000        3.3.0 → host         USB 28 SET CONFIGURATION Response
   19   0.084582        3.1.1 → host         USB 35 URB_INTERRUPT in
   20   0.084639         host → 3.1.1        USB 27 URB_INTERRUPT in

```

For Bluetooth HID (Human Interface Devices like keyboards or mouse), you can use ```bthid || bthci_evt```

```tshark -r capture.pcapng  -Y "bthid || bthci_evt" ```

### Filter by HID Class
HID (Human Interface Device) traffic is often used by both keyboards and mouse. You can filter HID-related packets with ```usb.device_class == 0x03```, this will display packets for devices that fall under the HID class, which includes both keyboards and mouse.

### Analyze the Packet Content:
1) Keyboard HID reports typically contain key codes. You can recognize a keyboard by looking at the HID report descriptor and seeing if it contains standard key codes.
2) Mouse traffic includes X and Y movement data (for cursor movement) and may also include information about button clicks (left, right, middle).

For example:
<br>
USB Keyboard Packets: Often contain 8-byte data fields. Bytes 3-8 typically represent key codes.
<br>
USB Mouse Packets: Usually contain data representing movement (X, Y) and button clicks.

HID devices have some data that describe their functionality. You can ```right-click a packet and choose Follow → USB stream``` or view the descriptor information.
1) Keyboards: Usually have descriptors that define input as key presses.
2) Mouse: Typically have descriptors that define X/Y axis movements and button presses.

### Filter Specific Report Descriptors:
For a keyboard, use this filter ```usb.capdata && usb.endpoint_address.direction == "in"``` to focus on specific USB HID packets that might reveal keystrokes.
<br>
For a mouse, you can look for data about relative movement or button presses.

### Example
Keyboard Packets:
<br>
HID packets for keyboards often contain key scan codes in bytes 3-8 of the payload ```00 00 04 00 00 00 00 00```, the ```04``` corresponds to the keycode for the letter ```A``` on a US keyboard layout.

Mouse Packets:
<br>
HID reports for mice typically contain relative movement data (for X/Y coordinates) and button presses ```00 02 00 00 00 00```, the ```02``` indicates movement along the X-axis.

More information [HID Wiki](https://wiki.osdev.org/USB_Human_Interface_Devices)

After this investigation we start extracting HID data from pcapng file with command ```tshark -r capture.pcapng -Y "usb.src==3.1.1" -T fields -e usbhid.data > hid.txt```
output
```
at hid.txt | head -n 30
0000263957510000
0000263957510000
000026397b510000
000000397b510000
00000039c3510000
00000039e8510000
0000ec38e8510000
0000ec380c520000
0000ec3854520000
0000d93854520000
0000d93879520000
0000d9389d520000
0000c5389d520000
0000c538e5520000
0000c5380a530000
0000b2380a530000
0000b23852530000
0000b23876530000
00008b3876530000
```

To reconstruct the X, Y coordinates from the HID data, we'll first parse the hexadecimal data. In the standard HID format for mouse data, the bytes represent the following information:
1) Byte 1: Button states (not used for movement).
2) Byte 2: X movement (signed 8-bit integer).
3) Byte 3: Y movement (signed 8-bit integer).
4) Bytes 4-6: Wheel movement or reserved fields (not used for basic X, Y movement).


take the value ```0000263957510000```
1) Byte 1: 00 – Button state (ignore for now).
2) Byte 2: 26 – X movement (hex 0x26 = 38 in decimal, so movement is +38 in X direction).
3) Byte 3: 39 – Y movement (hex 0x39 = 57 in decimal, so movement is +57 in Y direction).
4) Remaining Bytes: Reserved or unused for this purpose.



