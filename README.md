# homeServerEDisplay
This is used to control the 3.52" e-ink display from pihut. Display: https://thepihut.com/products/3-52-e-paper-hat-360x240

## Remember
1) Change the `raspi-config` to allow SPI.
```
sudo raspi-config
Choose Interfacing Options -> SPI -> Yes Enable SPI interface
```
2) Run the install script. This will need `sudo` as it needs to move a file into a protected zone.

3) Move the `pic` directory into your working directory as these are your fonts. located in `e-Paper/RaspberryPi_JetsonNano/python/pic/`
