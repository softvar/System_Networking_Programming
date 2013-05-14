import appuifw
import contacts
import calendar

L = [u'Add Contacts', u'Delete Contacts', u'Find Contact', u'Edit Contact', u'Create Group', u'Delete Group', u'Add Member to Group', u'Date and Time', u'Add Calender events', u'Exit']

index = appuifw.selection_list(choices=L , search_field=1)

if index==0:

	db = contacts.open()
	c = db.add_contact()
	fnam = appuifw.query(u"first_name:", "text")
	lnam= appuifw.query(u"last_name:", "text")
	no = appuifw.query(u"mobile_number:", "text")
	
	
	c.add_field('first_name', fnam)
	c.add_field('last_name', lnam)
	c.add_field('mobile_number', no)
	print "new contact\n" +fnam + "  "+lnam+"  "+ no +"\n"
	c.commit()

elif index==1:
	db = contacts.open()
	data = appuifw.query(u"Type contact to delete:", "text")
	l = db.find(data)
 
	if len(l) > 0:
		c = l[0]
		id = c.id
 
		print "deleted"
		print db[id]
		del db[id]
	else:
		print "No such contact found"
	
elif index==2:
	db = contacts.open()
	data = appuifw.query(u"Type contact to Find:", "text")
	l = db.find(data)
 
	if len(l) > 0:
		c = l[0]
		#Get its ID
		id = c.id
 
		print db[id]
	else:
		print "No such contact found"
	
elif index==3:
	db = contacts.open()
	data = appuifw.query(u"Type contact to Find n Edit:", "text")
	#Search for a contact whose name is data
	c = db.find(data)
	d=c[0]
 
	 
	#Retrieve the "last_name" field if it exists, change its 	value to some other name and its label to "Surname"
	if d.find("first_name"):
		print d
		data = appuifw.query(u"Type new Fname:", "text")
		d.find("first_name")[0].value = data
 
	#Undo the changes
	#c.commit()
elif index==4:
	db = contacts.open()
 
	#Instantiate a Groups object
	groups = db.Groups(db)
 
	#Add a new group
	group = groups.add_group(u"Friends")
	print "group named friends added"
elif index==5:
	db = contacts.open()
 
	#Get a list of IDs of the available groups
	ids = list(iter(db.groups))
 
	#Remove the group whose ID is first in the list
	print "deleted" 
	print db.groups[ids[0]]
	del db.groups[ids[0]]
elif index==6:
	db = contacts.open()
 
	#Get a list of IDs of the available groups
	group_ids = list(iter(db.groups))
 
	#Open the first group in the list
	group = db.groups[group_ids[0]]
 
	#Get a list of all the contact IDs
	id = contacts.open().keys()
 
	#Add the first contact in the list
	group.append(id[0])
	print db[id[0]]
	print "added to grp"
	
elif index==8:
	db = calendar.open()

	#Create an appointment entry
	appointment = db.add_appointment()

	#Add the regular information
	appointment.content = appuifw.query(u"Enter subject", 	"text")
	appointment.location = appuifw.query(u"Enter location", 	"text")

	#Ask the user for the start and end time
	t1 = appuifw.query(u"Enter start hour", "time")
	d1 = appuifw.query(u"Enter start date", "date")
	t2 = appuifw.query(u"Enter end hour", "time")
	d2 = appuifw.query(u"Enter end date", "date")

	start_time = t1 + d1
	end_time = t2 + d2

	#Set the start and end time
	appointment.set_time(start_time, end_time)

	#Save the entry	
	appointment.commit()

			
 