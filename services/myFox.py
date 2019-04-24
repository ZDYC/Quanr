import logging
import os
import pickle
import psutil
from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import myFirefox


class myFox():

    def __init__(self):
        self.file = r'/home/yu/Desktop/Quanr/params.data'
        self.gecko = r'/usr/bin/geckodriver'
        self.url = 'http://127.0.0.1:4444'
        self.capabilities = DesiredCapabilities.FIREFOX

    def createfirefox(self):
        os.system('sh geckodiver.sh')
        driver = webdriver.remote.webdriver.WebDriver(command_executor=self.url,
                                                      desired_capabilities=self.capabilities,
                                                      )
        params = {}
        params["session_id"] = driver.session_id
        params["server_url"] = driver.command_executor._url
        with open(self.file, 'wb') as f:
            pickle.dump(params, f)
        return driver

    def work(self):
        p_name = [psutil.Process(i).name() for i in psutil.pids()]
        if 'geckodriver' not in p_name:
            driver = self.createfirefox()
        else:
            try:
                with open(self.file, 'rb') as f:
                    params = pickle.load(f)
                driver = myFirefox.myWebDriver(service_url=params['server_url'], session_id=params['session_id'])
                driver.refresh()
            except Exception as e:
                logging.error('error', e)
                print(e)
                [p.kill() for p in psutil.process_iter() if p.name()=='geckodriver']
                driver = self.createfirefox()
        return driver