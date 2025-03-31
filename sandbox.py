
import time
from unitTesting import modules
from unitTesting import logIn

if __name__ == "__main__":
    
    
    l = logIn.login()
    l.setup()
    l.login()
    
    mt = modules.moduleTabs(l.driver)
    mt.admin()
    # mt.setup()
    # mt.login()
    # mt.admin()
    mt.pim()
    mt.leave()
    mt.time()
    mt.recruitment()
    mt.myInfo()
    mt.performance()
    mt.dashboard()
    mt.directory() 
    mt.claim()
    mt.buzz()
    
