import sys
import os
import logging

def print_log(msg) :

	logging.basicConfig(filename="rename.log",  
               format='%(asctime)s %(message)s',  
               filemode='w')  
	logger=logging.getLogger() 
	logger.setLevel(logging.DEBUG)   
	logger.debug(msg)



def rename_image_files(dir_name, name) :

	try :
		dir_list = os.listdir(dir_name)

	except Exception as e : 
		print_log(dir_name + "  Directory not found ")
		print(dir_name + "  Directory not found ")
		exit()

	file_no = 1;

	for file in dir_list :

		if (".jpg" in file or ".jpeg" in file) :
			old_name = dir_name + "/" + file
			new_name = dir_name +"/" + name + str(file_no) + ".jpg"
			file_no = file_no + 1

			try : 
				os.rename(old_name, new_name)

			except Exception :
				print("Error while remaning file " + old_name) 
				print_log("Error while remaning file " + old_name) 
				exit()

	print_log("All files are renamed")


def get_dir_name() :

	cwd = os.getcwd()
	cmd_args = sys.argv
	dir_name = ""
	if (len(cmd_args) < 1) :
		print("Directory name should be entered")
		print_log("Directory name should be entered")
		exit()

	elif(len(cmd_args) == 1) :
		dir_name = cwd

	else :
		dir_name = cmd_args[1]
		if("C:" in dir_name) :
			pass

		else :
			dir_name = cwd + "/" + dir_name

	return dir_name


def main() :
	
	dir_name =get_dir_name()
	print_log("Directory : " + dir_name)
	name = "newname-file-"
	rename_image_files(dir_name, name)

	
if __name__ == "__main__" :
	main()