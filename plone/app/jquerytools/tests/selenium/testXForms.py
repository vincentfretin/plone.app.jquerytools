import sys
import time

from base import SeleniumTestCase
from plone.app.testing import TEST_USER_NAME, TEST_USER_PASSWORD, TEST_USER_ROLES

class FormTestCase(SeleniumTestCase):
        
    def test_afancy_form(self):
        """ test basic form functions on a complex form """

        sel = self.selenium

        count = 0
        while True:
            count += 1
            try:
                self.open("@@p.a.jqt.testPage/")
            except:
                if str(sys.exc_value).count('XHR ERROR') :
                    print "Nasty selenium XHR bug!"
                else:
                    raise
            time.sleep(2)
            if (count == 5) or sel.is_element_present("id=taform"):
                break

        self.waitForElement("#taform")
        time.sleep(1)

        sel.click("taform")
        time.sleep(2)
        self.failUnless(sel.is_text_present("Test Form"))
        self.failUnless(sel.is_text_present("exact:ajax_load:"))

        sel.type("Password", "xxx")
        sel.click("//input[@name='Check' and @value='3']")
        sel.click("//input[@name='Radio' and @value='3']")
        sel.click("submitButton")
        time.sleep(3)

        self.failUnless(sel.is_text_present("exact:Multiple:one"))
        self.failUnless(sel.is_text_present("exact:Name:MyName1"))
        self.failUnless(sel.is_text_present("exact:Single2:A"))
        self.failUnless(sel.is_text_present("exact:Single:one"))
        self.failUnless(sel.is_text_present("exact:Radio:3"))
        self.failUnless(sel.is_text_present("exact:Text:This is Form1"))
        self.failUnless(sel.is_text_present("exact:submitButton:Submit1"))
        self.failUnless(sel.is_text_present("exact:Hidden:hiddenValue"))
        self.failUnless(sel.is_text_present("exact:Password:xxx"))
        self.failUnless(sel.is_text_present("exact:Check:3"))
        sel.click("//input[@name='submitButton' and @value='Submit2']")
        time.sleep(3)
        self.failUnless(sel.is_text_present("exact:submitButton:Submit2"))
        sel.click("//button[@name='submitButton']")
        time.sleep(3)
        self.failUnless(sel.is_text_present("exact:submitButton:Submit5"))
