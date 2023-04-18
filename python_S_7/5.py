class TV:
    def __init__(self, Power, Channel, Volume):
        self.Power = Power
        self.Channel = Channel
        self.Volume = Volume
    def info(self):
        print("Power :", self.Power)
        print("Channel :", self.Channel)
        print("Volume :", self.Volume)
    def on_off(self):
        if self.Power == "On":
            print("Turn off")
        elif self.Power == "Off":
            print("Turn on")
    def set_channel(self, n):
        self.Channel = n
        print("Channel :", self.Channel)
    def set_volume(self, n):
        self.Volume = n
        print("Volume :", self.Volume)
control = TV("On", 1, 16)
control.info()
control.on_off()
control.set_channel(172)
control.set_volume(14)