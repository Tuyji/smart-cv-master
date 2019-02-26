import datetime

class Course(object):
	def __init__(self):
		self.courser_id=0
		self.name=''
		self.number=0

class SpeakLanguage(object):
	def __init__(self):
		self.speak_language_id=0
		self.name=''
		self.level=''

class Skill(object):
	def __init__(self):
		self.skill_id=0
		self.name=''
		self.level=''
		self.year=''
	
class Education(object):
	def __init__(self):
		self.education_id=0
		self.start_date=None
		self.end_date=None
		self.year=None
		self.school_name=''
		self.field_of_study=''
		self.degree=''
		self.activities=''
		self.notes=''

class Position(object):
	def __init__(self):
		self.company=Company()		
		self.end_date=None
		self.start_date=datetime.datetime.now()
		self.isCurrent=False
		self.summary=''
		self.title=''

class Company(object):
	def __init__(self):
		self.company_id=0
		self.industry=''
		self.name=''
		self.size=''
		self.company_type=''

