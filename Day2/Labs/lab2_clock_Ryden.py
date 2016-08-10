class Clock(object):
	def __init__(self, hour, minutes):
		self.minutes = minutes
		self.hour = hour
		
	@classmethod
	def at(cls, hour, minutes=0):
		return cls(hour, minutes)
		
	def __str__(self):
		while self.hour > 12:
			self.hour -= 12
		if self.hour == 0:
			self.hour = 12
		if self.minutes < 10:
			return '''%d:0%d''' % (self.hour, self.minutes)
		else:
			return '''%d:%d''' % (self.hour, self.minutes)
	
	def __repr__(self):
		return self.__str__()
	
	def __add__(self, minutes):
		new_minutes = self.minutes + int(minutes)
		result = Clock(self.hour, new_minutes)
		while result.minutes >= 60:
			result.minutes -= 60
			result.hour += 1
		while result.minutes < 0:
			result.minutes += 60
			result.hour -= 1
		while result.hour > 12:
			result.hour -= 12
		while result.hour < 0:
			result.hour += 12
		if result.hour == 0:
			result.hour == 12
		return result
		
	def __sub__(self, minutes):
		new_minutes = -1 * minutes
		return self.__add__(new_minutes)
		
    def __eq__(self, other):
	    if type(other) == str:
            if other == self.__str__():
                return True
            return False
        if other == self:
            return True
        return False
		
    def __ne__(self, other):
        return not self.__eq__(other)
		
# 	def __eq__(self,other):
# 	    if type(other) != str:
# 	        other = other.__str__()
# 	    new_other = other.split(':')
# 	    if self.minutes < 10:
# 	        mins = '''0%d''' % (self.minutes)
# 	    else:
# 	        mins = self.minutes
# 	    old_hour = str(self.hour)
# 	    old_min = str(mins)
# 	    if old_hour == new_other[0] and old_min == new_other[1]:
# 	        return True
# 	    else:
# 	        return False

