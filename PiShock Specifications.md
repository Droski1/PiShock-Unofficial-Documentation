# ShockerId being 3377 

## RF Communication Protocol
                      (?)               IDK---\ Operations? Unknown
                       |                  |    \     |     /
   Shocker ID    | Operation |  Power  | ??? | ?? | OPE | Nul | # Name 
=================|===========|=========|=====|====|=====|=====|==========       
0000110100110001 | 000000110 | 0011001 | 010 | 11 | 010 | 000 | # BEEP
0000110100110001 | 000000010 | 0011001 | 010 | 11 | 000 | 000 | # 25%
0000110100110001 | 000000010 | 0000001 | 010 | 00 | 000 | 000 | # 1%
0000110100110001 | 000000100 | 0011001 | 010 | 11 | 001 | 000 | # Vibrate
0000110100110001 | 000000010 | 0011001 | 010 | 11 | 000 | 000 | # Mini 25
0000110100110001 | 000000110 | 0011001 | 010 | 11 | 010 | 000 | # Beep 15
0000110100110001 | 000000010 | 0011001 | 010 | 11 | 000 | 000 | # Mini 25 Variable 4-9


## Internal Json Formatting
{
    "Commands": [
        {
            "Id": 10,
            "Mac": "c0_49_ef_e6_1c_5c",
            "At": "2023-09-30T23:28:19.6047298Z",
            "Status": 1,
            "Type": 4,
            "Values": {
                "ShockerId": 3377,
                "Duration": 1,
                "Intensity": 25,
                "Method": 4,
                "Type": 1,
                "Milliseconds": false
            }
        }
    ],
    "ShockersId": [
        3377
    ],
    "ShockersType": [
        1
    ],
    "LastCommandId": 11,
    "Poll": 1,
    "RequestRefresh": false
}

## Hardware Info

ACEIRMC D1 Node MCU ESP32 WLan Wifi Bluetooth
    - Link: https://www.amazon.com/ACEIRMC-ESP-WROOM-32-Bluetooth-Development-Compatible/dp/B08PNWB81Z?th=1

RF Board 433MHz RF Wireless
    - Link: https://pmdway.com/products/long-range-433mhz-rf-wireless-transceiver-kit

Collar: Petrainer PET998DB E-Collar
    - Link: https://www.amazon.com/Petrainer-PET998DB1-Rechargeable-Waterproof-Electronic/dp/B00LVUP82S


## Extra
https://cyber.horse/blog/dissecting-petrainer-pt1.html\
https://github.com/CrashOverride85/collar/blob/master/extra/Type1.MD


## Testing
Going from Bytes to Flipper Code
