# BeagleBone Blue Setup Guide for Robotic Arm Control

This guide covers everything you need to set up a BeagleBone Blue (BBB) board to control a robotic arm using OpenCV-based color and object detection.

---

## System Requirements

* **BeagleBone Blue** (with Debian image)
* **16GB MicroSD Card** (for storage expansion)
* **SD Card Reader** (to flash Debian image)
* **USB Cable (Micro-USB)** (for power and communication)
* **USB Camera** (for object detection input)
* **Breadboard & JST Wires** (for I2C and servo wiring)
* **5V Power Adapter** (for servos)
* **Laptop/PC** (for flashing and SSH)

---

## Step 1: Download & Flash Debian to SD Card

1. Visit the [BeagleBoard.org Distros page](https://www.beagleboard.org/distros).
2. Download the latest **Debian image** for BeagleBone Blue (e.g., "Debian 10.3 (Buster) IoT").
3. Flash the image using **balenaEtcher** or **Rufus**:

   * Select image → Select MicroSD card → Flash
4. Insert the SD card into your BeagleBone Blue.

---

## Step 2: Boot from SD [Card](http://192.168.7.2)

1. [Pre](http://192.168.7.2)ss and hold the **SD** button while powering the board.
2. Release after a few seconds to force boot from SD.
3. Watch for **LEDs blinking in a Larson scanner pattern** (left to right) – indicates booting.

---

## Step 3: Connect to BBB via SSH

1. Connect BBB to your computer using microUSB.
2. Access terminal using:

   ```bash
   ssh debian@192.168.7.2
   # Default credentials: debian / temppwd
   ```
3. To find IP address:

   ```bash
   ip a
   ```

---

## Step 4: Enable Wi-Fi Connection

```bash
sudo -s
cd /etc/network
ifconfig    # confirm wlan0 exists

sudo nano /etc/network/interfaces
```

Add this to the bottom:

```text
auto wlan0
iface wlan0 inet dhcp
    wpa-ssid "your_SSID"
    wpa-psk "your_password"
```

Then:

```bash
sudo pkill wpa_supplicant
sudo ifdown wlan0 && sudo ifup wlan0
```

---

## Step 5: Expand Storage Using SD Card

If 4GB eMMC is insufficient, shift full system to SD card:

```bash
sudo fdisk /dev/mmcblk0
# n → p → 1 → enter → enter → w
sudo mkfs.ext4 /dev/mmcblk0p1
sudo mkdir /mnt/sdcard
sudo mount /dev/mmcblk0p1 /mnt/sdcard
sudo rsync -avx / /mnt/sdcard
```

Edit boot config:

```bash
sudo nano /boot/uEnv.txt
```

Add or modify:

```text
cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh root=/dev/mmcblk0p1
```

Reboot:

```bash
sudo reboot
```

Check mounted filesystems:

```bash
df -h
```

---

## Step 6: Install Dependencies

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip python3-opencv libv4l-dev fswebcam
pip3 install numpy opencv-python
```

Optional robotics control:

```bash
sudo apt install librobotcontrol
# OR
sudo apt install roboticscape
```

---

## Step 7: Access Webcam

```bash
lsusb              # confirm camera detected
fswebcam image.jpg # test capture
```

---

## Step 8: GUI Access via VNC (Optional)

```bash
sudo apt install tightvncserver
vncserver :1        # set password when prompted
```

Then access from your PC using [RealVNC Viewer](https://www.realvnc.com):

```
192.168.7.2:5901
```

---

## Step 9: Servo Motor Control

Ensure sufficient 5V power supply is connected externally.

Test using:

```bash
sudo rc_test_servos -c 1 -p 0.0
```

Other usage:

```bash
rc_test_servos -c {channel} -p {position}
rc_test_servos -f {hz}
rc_test_servos -s {limit}
rc_test_servos -r {ch}
```

For full help:

```bash
rc_test_servos -h
```

---


👉 Now return to your main [`README.md`](./README.md) and start integrating vision and motion!

---

