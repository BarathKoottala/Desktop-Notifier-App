import time 
import os 
from news import get_top_stories

# news_paper_icon_path = "//Users//barath//Projects//python_playground//desktop_notification_app/news_paper.jpg"

news_items = get_top_stories()

# notify2.init("Uplifting News Notifier")


# notify = notify2.Notification(None, icon=news_paper_icon_path)

# notify.set_urgency(notify2.URGENCY_NORMAL) 

# notify.set_timeout(10000) 

for item in news_items: 
	
    displayNotification(message=item['link'], title=item['title'])
    # notify.update(item['title'], item['link']) 

    time.sleep(30)

def displayNotification(message,title=None,subtitle=None,soundname=None):
	"""
		Display an OSX notification with message title an subtitle
		sounds are located in /System/Library/Sounds or ~/Library/Sounds
	"""
	titlePart = ''
	if(not title is None):
		titlePart = 'with title "{0}"'.format(title)
	subtitlePart = ''
	if(not subtitle is None):
		subtitlePart = 'subtitle "{0}"'.format(subtitle)
	soundnamePart = ''
	if(not soundname is None):
		soundnamePart = 'sound name "{0}"'.format(soundname)

	appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message,titlePart,subtitlePart,soundnamePart)
	os.system("osascript -e '{0}'".format(appleScriptNotification))

if __name__ == '__main__':
	#displayNotification("message","title","subtitle","Pop")
	#displayNotification("message","title","subtitle")
	displayNotification("message","title")
	#displayNotification("message")