#coding=utf-8

from util.read_init import ReadIni

class GetByLocal(object):
	def __init__(self,driver):
		self.driver = driver

	def get_element(self,key):
		read_ini = ReadIni()
		local = read_ini.get_value(key)
		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]

			activity = self.driver.current_activity


			print("activity====================================================",activity,"================================")
			try:
				if by == 'id':
					print("++++++++++++++++++++++++++++++++",local_by,local_by=="org.cnodejs.android.md:id/edt_access_token")
					# if local_by=="org.cnodejs.android.md:id/edt_access_token":
					# 	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
					# 	self.driver.find_element_by_id("org.cnodejs.android.md:id/edt_access_token").click()
					# 	return self.driver.find_element_by_id("org.cnodejs.android.md:id/edt_access_token").send_keys('abcddd')
					# else:
					return self.driver.find_element_by_id(local_by)

				elif by == 'className':
					return self.driver.find_element_by_class_name(local_by)
				elif by == 'android_uiautormator':
					return self.driver.find_element_by_android_uiautomator(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				return None
		else:
			return None


