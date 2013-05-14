import appuifw
import messaging
import inbox
import time
L = [u'Send an SMS',u'Open Inbox',u'Sort inbox messages using date and time',u'Sort inbox messages using names',u'Send autoreply to messages']
index = appuifw.selection_list(choices=L , search_field=0)
if index==0:
	msg = appuifw.query(u"Enter message:", "text")
	num = appuifw.query(u"Enter number:", "text")
	if appuifw.query(u"Send message?","query") == True:
		messaging.sms_send(num, msg)
		appuifw.note(u"Message sent", "info")
	else:
		appuifw.note(u"Message cannot be sent", "info")
elif index==1:
	box = inbox.Inbox(inbox.EDraft)
	messages = box.sms_messages()
	print "You have %d SMS messages." % len(messages)
elif index==2:
	obj={}
	box = inbox.Inbox(inbox.EDraft)
	messages = box.sms_messages()
	for x in messages:
		obj[x]=time(x)
	for w in sorted(obj, key=obj.get):
		print w, obj[w]
elif index==3:
	obj={}
	box = inbox.Inbox(inbox.EDraft)
	messages = box.sms_messages()
	for x in messages:
		obj[x]=address(x)
	for w in sorted(obj, key=obj.get):
		print w, obj[w]
