```python
class Time:
    """The class takes input in minutes and seconds and
    convert the result into hours, minutes and seconds"""

    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec

    def convert(self):
        if self.sec >= 60:
            self.min = self.min + (self.sec // 60)
            second = self.sec - (self.sec // 60) * 60
        else:
            second = self.sec
        hour = self.min // 60
        minute = self.min - (hour * 60)

        return print(hour, "hour:", minute, "minute:", second, "seconds")


o = Time(0, 70000)
o.convert()
```
