# E-ink temperature + humidity PCB (active, 2026-10-11)

A group project with his brother **Seth**. Their first PCB: a battery-powered board that reads
temperature and humidity and shows them as text on an e-ink screen. PCBWay makes **and assembles** it.
KiCad 10.0.7, project `temperature_and_humidty` (on his machine, **not in a repo yet**).

## Status (2026-10-11 17:04 CDT)

- **Schematic done. ERC passes: 0 errors, 0 warnings.**
- **Footprints:** all passives (0805), the LED and the four chips are assigned. **Still open:** J1
  (battery), J2 (USB-C), J3 (display), SW1 and SW2. Each one waits on picking a real part to buy.
- **Not started:** schematic tidy-up into blocks, PCB layout, ordering.

## The design

| Block | Parts | Key values |
| --- | --- | --- |
| Battery | J1, 2-pin; 1-cell LiPo, **100 mAh**, protected | +BATT net |
| USB-C | J2 `USB_C_Receptacle_USB2.0_16P` | CC1/CC2 each 5.1k to GND; D+ → IO19, D− → IO18; SBU no-connect |
| Charger | U3 **MCP73831-2-OT** (4.20 V) | R5 **10k → 100 mA** (1C); 4.7u in/out; charge LED on STAT via 1k from VBUS |
| Regulator | U1 **AP2112K-3.3** | 1u in/out; EN tied to VIN |
| MCU | U2 **ESP32-C3-WROOM-02** | 10u + 100n decoupling; EN = 10k up + 1u + reset button; IO9 = 10k up + BOOT button; IO2, IO8 = 10k pull-ups (strapping) |
| Sensor | U4 **SHT4x** (order SHT40-AD1B, address 0x44) | SDA IO4, SCL IO5, 10k pull-ups, 100n |
| Display | J3 8-pin header for a 2.13" e-ink **module** | DIN IO7, CLK IO6, CS IO10 (hardware SPI default pins), DC IO20, RST IO21, BUSY IO3 |
| Battery gauge | 1M/1M divider + 100n | VBAT_SENSE → IO0 (ADC1) |

No Wi-Fi: the board wakes, reads, updates the screen, and goes back to deep sleep. Rough budget
was ~0.15 mA average, so ~4 weeks on 100 mAh. **That's an estimate, never measured.** Most of
the sleep current is the AP2112's ~55 µA quiescent current.

## Decisions and why

- **LiPo over AA** (his): "fits well into learning robotics stuff." The USB port also programs the C3.
- **ESP32-C3 over S3** (his): simpler. 15 GPIOs covers it.
- **WROOM-02 module**: antenna, crystal and flash inside, pre-certified. The bare chip would mean RF design.
- **E-ink, not a backlit LCD**: a backlight draws 10–30 mA all the time, so 100 mAh would last
  hours. They only care about text.
- **PCBWay assembles**: the SHT40 is a 1.5 mm DFN, which can't be hand-soldered. Passives are 0805
  so they can still be reworked by hand.
- **Battery gauge added** after review: his "can't we do it in software?" Answer: no. The 3.3 V rail
  stays flat until the battery is nearly dead.

## Open items, in order

1. **Pick the display module.** DFR0676 (DFRobot) turned out to be a **complete ESP32 + e-ink
   board** (LilyGO T5 V2.3), not a module, so it can't be J3. Plan: **buy it as the firmware
   prototype** (with an SHT40 breakout on SDA 21 / SCL 22), and find a display-only module for the
   PCB (e.g. "Waveshare 2.13 inch e-Paper **Module**"). Check its **pin order** (J3 labels must
   match it) and **pin count** (some newer driver boards have a 9th PWR pin).
2. **Footprints for J1–J3, SW1–SW2**, from parts they'll actually order. J1: JST-PH horizontal SMD
   (`JST_PH_S2B-PH-SM4-TB`) suggested. **Check LiPo polarity:** many sellers reverse red/black.
   J2: a common 16-pin USB-C that PCBWay can source.
3. **Tidy the schematic** into blocks: inputs left, MCU centre, sensor/display right. Add notes on
   non-obvious values, the title block and rev A, and re-annotate.
4. **PCB editor:** F8 Update PCB from Schematic. Check that ESP32 **GND pad 19** (EPAD) lands on
   GND. Sensor at the board edge, away from the charger, regulator and MCU heat. Module antenna
   hanging over the board edge with no copper under it. Input/output capacitors tight to their pins.
5. **Optional, decided against for now:** USB ESD protection (e.g. USBLC6-2), reverse-battery protection.

## Datasheets used

AP2112 (Diodes Inc.), ESP32-C3-WROOM-02 (Espressif: peripheral schematic §9, pin table §3,
strapping Tables 4-1/4-3), MCP73831 (Microchip DS20001984G, DC characteristics I_REG table),
SHT4x (Sensirion, typical application circuit).
