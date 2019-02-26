import jsonparser
import liclass

class Profile(object):
	def __init__(self,json_data):
		self.data=json_data
		self.set_fname()
		self.set_lname()
		self.set_email()
		self.set_phone()
		self.set_headline()
		self.set_summary()
		self.set_location()
		self.set_industry()
		self.set_courses()
		self.set_languages()
		self.set_educations()
		self.set_skills()
		self.set_interests()
		self.set_educations()
		self.set_past_positions()
		self.set_current_positions()

	
	def set_fname(self):
		self.f_name=jsonparser.get_fname(self.data)

	def set_lname(self):
		 self.l_name=jsonparser.get_lname(self.data)

	def set_email(self):
		self.email=jsonparser.get_email(self.data)

	def set_phone(self):
		self.phone=jsonparser.get_phone(self.data)

	def set_headline(self):
		self.headline=jsonparser.get_headline(self.data)
	
	def set_summary(self):
		self.summary=jsonparser.get_summary(self.data)
	
	def set_location(self):
		self.location=jsonparser.get_location(self.data)
	
	def set_industry(self):
		self.industry=jsonparser.get_industry(self.data)
	

	def set_courses(self):
		self.courseList=[]
		if self.data.get('courses') !=None:
			for i in range(0,self.data['courses']['_total']):
				course=jsonparser.get_course(self.data,i)
				self.courseList.append(course)
	def set_languages(self):
		self.languageList=[]
		if self.data.get('languages') != None:
			for i in range(0,self.data['languages']['_total']):
				language=jsonparser.get_language(self.data,i)
				self.languageList.append(language)
	def set_skills(self):
		self.skillList=[]
		if self.data.get('skills')!=None:
			for i in range(0,self.data['skills']['_total']):
				skill=jsonparser.get_skill(self.data,i)
				self.skillList.append(skill)
	
	def set_interests(self):
		self.interests=''
		if self.data.get('interests')!=None:
			self.interests=	self.data['interests']
	
	def set_educations(self):
		self.educationList=[]
		if self.data.get('educations') != None:
			for i in range(0,self.data['educations']['_total']):
					edu=jsonparser.get_education(self.data,i)
					self.educationList.append(edu)
	def set_current_positions(self):
		self.currentPositionList=[]
		if self.data.get('threeCurrentPositions') != None:
			for i in range(0,self.data['threeCurrentPositions']['_total']):
				position=jsonparser.get_poisition(self.data,False,i)
				self.currentPositionList.append(position)
	
	def set_past_positions(self):
		self.pastPositionList=[]
		if self.data.get('threePastPositions') != None:
			for i in range(0, self.data['threePastPositions']['_total']):
				position=jsonparser.get_poisition(self.data,True,i)
				self.pastPositionList.append(position)


