import datetime
import liclass

def get_fname(json_data):
	return str(json_data['firstName'])

def get_lname(json_data):
	return str(json_data['lastName'])

def get_email(json_data):
	str_email=''
	if json_data.get('emailAddress') != None:
		str_email=json_data['emailAddress']
	return str_email

def get_phone(json_data):
	str_phone=''
	if json_data.get('phoneNumbers') != None:
		total=json_data['phoneNumbers']['_total']
		for i in range(0,total):
			str_phone=str(json_data['phoneNumbers']['values'][i]['phoneNumber'])
			if json_data['phoneNumbers']['values'][i]['phoneType']=='mobile':
				return str_phone
	
	return str_phone

def get_headline(json_data):
	if json_data.get('headline') != None:
		return json_data['headline']

def get_industry(json_data):
	if json_data.get('industry') != None:
		return json_data['industry']

def get_summary(json_data):
	if json_data.get('summary') != None:
		return json_data['summary']

def get_location(json_data):
	if json_data.get('location') !=None:
		if json_data['location'].get('name') != None:
			return json_data['location']['name']


def get_course(json_data,n):
	course=liclass.Course()
        course.course_id=json_data['courses']['values'][n]['id']
        course.name=json_data['courses']['values'][n]['name']
        course.number=json_data['courses']['values'][n]['number']
	return course

def get_language(json_data,n):
	speak_language=liclass.SpeakLanguage()
	speak_language.speak_language_id=json_data['languages']['values'][n]['id']
	if json_data['languages']['values'][n]['language'].get('name') != None:
		speak_language.name=json_data['languages']['values'][n]['language']['name']
	
	if json_data['languages']['values'][n].get('proficiency') !=None:
		speak_language.level= json_data['languages']['values'][n]['proficiency']['name']
	
	return speak_language

def get_skill(json_data,n):
	skill=liclass.Skill()
	skill.name=json_data['skills']['values'][n]['skill']['name']
	if json_data['skills']['values'][n].get('proficiency') !=None:
		skill.level= json_data['skills']['values'][n]['proficiency']['name']
	

	return skill 

def get_education(json_data,n):
	education=liclass.Education()
	education.education_id=json_data['educations']['values'][n]['id']
	education.start_date=json_data['educations']['values'][n]['startDate']['year']
	education.school_name=str(json_data['educations']['values'][n]['schoolName'].encode('utf-8'))

	if json_data['educations']['values'][n].get('degree') != None:
		education.degree=json_data['educations']['values'][n]['degree']
	
	if json_data['educations']['values'][n].get('activities') != None:
		education.activitie=json_data['educations']['values'][n]['activities']
	
	if json_data['educations']['values'][n].get('notes') != None:
		education.note=json_data['educations']['values'][n]['notes']

	if json_data['educations']['values'][n].get('endDate') != None:
		if json_data['educations']['values'][n]['endDate'].get('year') != None:
			education.end_date=json_data['educations']['values'][n]['endDate']['year']
	
	return education

def get_poisition(json_data,isPast,n):
	root_keyword_d = 'threePastPositions'
	if isPast== False:
		root_keyword_d = 'threeCurrentPositions'

	position=liclass.Position()
	position.start_date = datetime.datetime(int(str(json_data[root_keyword_d]['values'][n]['startDate']['year'])), 
			int(str(json_data[root_keyword_d]['values'][n]['startDate']['month'])),1)

	position.isCurrent=True

	if json_data[root_keyword_d]['values'][n]['isCurrent']==False:
		position.isCurrent=False
		position.end_date = datetime.datetime(int(str(json_data[root_keyword_d]['values'][n]['endDate']['year'])), 
			int(str(json_data[root_keyword_d]['values'][n]['endDate']['month'])),1)
	
	if json_data[root_keyword_d]['values'][n].get('title')!=None:
		position.title= str(json_data[root_keyword_d]['values'][n]['title'])
	
	
	if json_data[root_keyword_d]['values'][n].get('summary')!=None:
		position.summary= str(json_data[root_keyword_d]['values'][n]['summary'])
	
	if json_data[root_keyword_d]['values'][n].get('company')!=None:
		if json_data[root_keyword_d]['values'][n]['company'].get('id')!=None:
			position.company.company_id=str(json_data[root_keyword_d]['values'][n]['company']['id'])

		if json_data[root_keyword_d]['values'][n]['company'].get('industry')!=None:
			position.company.industry=str(json_data[root_keyword_d]['values'][n]['company']['industry'])

		if json_data[root_keyword_d]['values'][n]['company'].get('name')!=None:
			position.company.name=str(json_data[root_keyword_d]['values'][n]['company']['name'].encode('utf-8'))

		if json_data[root_keyword_d]['values'][n]['company'].get('size')!=None:
			position.company.size=str(json_data[root_keyword_d]['values'][n]['company']['size'])

		if json_data[root_keyword_d]['values'][n]['company'].get('type')!=None:
			position.company.type=str(json_data[root_keyword_d]['values'][n]['company']['type'])

	return position

