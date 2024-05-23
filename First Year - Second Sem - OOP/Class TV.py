#Lab Assignment No 5: Problem No. 1
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: May 5, 2024

class TV:
    def __init__(self, channel=1, volumeLevel=3, on=False):
        # Initialize TV with default channel, volume level, and off state
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on

    def turnOn(self):
        # Turn on the TV
        print('TV is on')

    def getChannel(self):
        # Get the current channel of the TV
        return self.channel

    def setChannel(self, channel):
        # Set the channel of the TV within the valid range of 1 to 120
        if channel >= 1 and channel <= 120:
            self.channel = channel

    def getVolume(self):
        # Get the current volume level of the TV
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        # Set the volume level of the TV within the valid range of 1 to 7
        if volumeLevel >= 1 and volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        # Increase the channel by 1, if within the valid range
        if self.channel >= 1 and self.channel <= 119:
            self.channel += 1

    def channelDown(self):
        # Decrease the channel by 1, if within the valid range
        if self.channel >= 2 and self.channel <= 120:
            self.channel -= 1

    def volumeUp(self):
        # Increase the volume level by 1, if within the valid range
        if self.volumeLevel >= 1 and self.volumeLevel <= 6:
            self.volumeLevel += 1

    def volumeDown(self):
        # Decrease the volume level by 1, if within the valid range
        if self.volumeLevel >= 2 and self.volumeLevel <= 7:
            self.volumeLevel -= 1

    def turnOff(self):
        # Turn off the TV
        print('TV is off')