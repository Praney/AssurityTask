# AssurityTask

**Abstract**

The goal of this project was to make automation script that will test the functional as well as Contract of an API.

**Background**

API which need to be tested is -:
1. https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false

**Test Cases:**

All the below test cases are according to the acceptance criteria mentioned in the task.

Following are the test cases that are implemented in the automation script:

1. **Functional Automation Testing** 
* Verifies if Name is Carbon Credit or not
* Verifies if Can Relist is true or not
* Verfies if Promotions which has Gallery contains text '2x larger image' or not

2. **Contract Automation Testing**
* Verifies the contract of the api

**Environment**
* Language- Python
* Framework - Pytest
* Model - API automation
* Report - pytest-html

**Pre requisites:** Test System should have python 2.7+ on it

**Steps to run automation script -**
1. Go to Automation Project https://github.com/Praney/AssurityTask
2. Clone it
3. cd projectname/
4. pip install -r requirements.txt
3. Install all the tools mentioned in requirements.txt
4. Run file startTest.sh (sh startTest.sh)
5. HTML Report is generated in the same project after running startTest.sh.

**HTML Report**

HTML report contains all the test cases with their status .You can check the sample report in the same repo.  
