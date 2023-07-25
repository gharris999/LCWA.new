'''
Created on May 8, 2023

@author: klein

test connection to dropbox
'''



import dropbox
import datetime
import time
from pathlib import Path 
from os.path import expanduser

class TestDropBox(object):

    def __init__(self,local_dir = None , dropbox_dir = None , dropbox_file = None, tokenfile = None, loop_time = None):
        self.LoopTime        = loop_time
        self.TokenFile      = tokenfile
        self.DropBoxFile    = dropbox_file
        self.DropBoxDir     = dropbox_dir
        self.LocalDir       = local_dir

    def ConnectDropboxOld(self):
        """
        here we establish connection to the dropbox account
        """
        f=open(self.TokenFile,"r")

    
        temp =f.readlines() #key for encryption
        temp_buf = []
  
        for k in range(len(temp)):
            temp1 = temp[k].strip('\n')
            start   = temp1.find('\'') # find beginning quote
            end     = temp1.rfind('\'') # find trailing  quote
            temp_buf.append(temp1[start+1:end])
        
        


        
    
             #connect to dropbox 
        #self.dbx=dropbox.Dropbox(self.data.strip('\n'))
        APP_KEY = temp_buf[0]
        APP_SECRET = temp_buf[1]
        REFRESH_TOKEN = temp_buf[2]

        self.dbx = dropbox.Dropbox(
            app_key = APP_KEY,
            app_secret = APP_SECRET,
            oauth2_refresh_token = REFRESH_TOKEN
        )
        

        self.myaccount = self.dbx.users_get_current_account()
        print('***************************dropbox*******************\n\n\n')
        print( self.myaccount.name.surname , self.myaccount.name.given_name)
        print (self.myaccount.email)
        print('\n\n ***************************dropbox*******************\n')

        return

    def ConnectDropbox(self):
        """
        here we establish connection to the dropbox account
        """
        f=open(self.TokenFile,"r")

        # now we branch out depending on which keyfile we are using:
        if  'LCWA_d.txt' in self.TokenFile:
            print("old system")
            f=open(self.TokenFile,"r")
            self.data =f.readline() #key for encryption
        

         
         
         
         #connect to dropbox 
            self.dbx=dropbox.Dropbox(self.data.strip('\n'))

 
        elif 'LCWA_a.txt'  in self.TokenFile:
            print('new system')

            temp =f.readlines() #key for encryption
            temp_buf = []
  
            for k in range(len(temp)):
                temp1 = temp[k].strip('\n')
                start   = temp1.find('\'') # find beginning quote
                end     = temp1.rfind('\'') # find trailing  quote
                temp_buf.append(temp1[start+1:end])
        
        


        
    
             #connect to dropbox 
            #self.dbx=dropbox.Dropbox(self.data.strip('\n'))
            APP_KEY = temp_buf[0]
            APP_SECRET = temp_buf[1]
            REFRESH_TOKEN = temp_buf[2]

            



            self.dbx = dropbox.Dropbox(
                app_key = APP_KEY,
                app_secret = APP_SECRET,
                oauth2_refresh_token = REFRESH_TOKEN
                )
        
        else:
            print("wrong keyfile")


        

        self.myaccount = self.dbx.users_get_current_account()
        print('***************************dropbox*******************\n\n\n')
        print( self.myaccount.name.surname , self.myaccount.name.given_name)
        print (self.myaccount.email)
        print('\n\n ***************************dropbox*******************\n')

        return self.dbx


    def DropFileExists(self,path):
        try:
            self.dbx.files_get_metadata(path)
            return True
        except:
            return False  
              

        

    def GetDropBoxfile(self , temp):

        if self.DropFileExists(temp):
            print ("getting file " ,temp, '   and storing it at : ',self.LocalDir+self.DropBoxFile)
                
            self.dbx.files_download_to_file(self.LocalDir+self.DropBoxFile,temp)
            return True
        
        else:
            return False
     
         
         

    def MainLoop(self):
        ''' this a timed loop, which every looptime gets the file at dropbox
        looptime is seconds
        '''
        while(True):
            e = datetime.datetime.now()
            if self.GetDropBoxfile(self.DropBoxDir+self.DropBoxFile):
                print(" Succesful Transfer at : %s/%s/%s  %s:%s:%s" % (e.day, e.month, e.year,e.hour, e.minute, e.second))
            else:
                print(" Failed Transfer at : %s/%s/%s  %s:%s:%s" % (e.day, e.month, e.year,e.hour, e.minute, e.second))

            time.sleep(self.LoopTime)  

        return 

 

if __name__ == '__main__':
    import os.path
    loop_time       = 600 # every loop_time we will read a file and copy it locally, the time is in seconds
    homedir         = os.path.expanduser('~')
    #tokenfile       = homedir+'/git/LCWA/src/LCWA_d.txt' # the name and path of the dropbox creds
    tokenfile       = homedir+'/git/LCWA/src/LCWA_a.txt' # the name and path of the dropbox creds
    #dropbox_dir     = '/LCWA/ALL_LCWA/' # dir on dropbox
    dropbox_dir     = '/LCWA/LC99_/'
    #dropbox_file    = 'LCWA_TOTAL_2023-05-07speedfile.pdf' # name of file
    dropbox_file    = 'LC99_2023-05-07speedfile.pdf'
    local_dir       = homedir+'/scratch/'


    TDB = TestDropBox(local_dir = local_dir ,dropbox_dir = dropbox_dir , dropbox_file = dropbox_file,  tokenfile = tokenfile ,loop_time = loop_time)
    TDB.ConnectDropbox()
    TDB.MainLoop()