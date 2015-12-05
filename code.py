import pyautogui
import os
import cv2
import time

"""
Works on OSX, any browser, any resolution. Use the "template_match" function of OpenCV to find the subpicture
Should work on windows. But I haven't tried
"""
customers = [
    "adventure.png",
    "buy.png",
    "hunter-1.png",
    "hunter-2.png",
    "knight-1.png",
    "illusionist-1.png",
    "musketeer-1.png",
    "mercenary-2.png",
    "barbarian-1.png",
    "barbarian-2.png",
    "barbarian-3.png",
    "evoker-1.png",
    "evoker-2.png",
    "engineer-1.png",
    "engineer-2.png",
    "engineer-3.png",
    "guard-1.png",
    "guard-2.png",
    "healer-1.png",
    "healer-2.png",
    "mercenary-1.png",
    "thief-1.png",
    "thief-2.png"
]

employees = [
    "waiting.png",
    "coffee.png",
    "shopkeeper_woman-1.png",
    "leather-worker-1.png",
    "leather-worker-2.png",
    "carpenter-1.png",
    "carpenter-2.png"
]

customerInteractions = [
    "buy-sell.png",
    "suggest.png",
    "wait.png"
]

employeeInteractions = [
    "zero.png",
    "lv3.png",
    "lv2.png"
]

suggestActions = [
    "lv3.png",
    "lv2.png",
    "lv1.png"
]

startActions = [
    "next.png",
    "open.png"
]

def makeEmployeeAction():
    for action in employeeInteractions:
        print "trying action : " + action

        coord = analysePicture(os.getcwd() + '/pictures/employee-interactions/' + action, os.getcwd() + '/temp/my_screenshot2.png', 0.8)

        if coord != (0, 0):
            pyautogui.click(coord)
            print "Action made!"
            return True
    return False

def makeSuggestAction():
    for action in suggestActions:
        print "trying action : " + action

        coord = analysePicture(os.getcwd() + '/pictures/suggest-actions/' + action, os.getcwd() + '/temp/my_screenshot2.png', 0.8)

        if coord != (0, 0):
            pyautogui.click(coord)
            print "Action made!"
            return True
    return False

def makeCustomerAction():
    for action in customerInteractions:
        print "trying action : " + action

        coord = analysePicture(os.getcwd() + '/pictures/customer-interactions/' + action, os.getcwd() + '/temp/my_screenshot2.png', 0.8)

        if coord != (0, 0):
            pyautogui.click(coord)
            print "Action made!"

            if action == "suggest.png":
                return "suggest"
            return True
    return False


def getCustomer():
    for customer in customers:
        print "trying with : " + customer

        coord = analysePicture(os.getcwd() + '/pictures/customers/' + customer, os.getcwd() + '/temp/my_screenshot2.png', 0.8)

        if coord != (0, 0):
            pyautogui.click(coord)
            print "Customer found!"
            return True
    return False

def getEmployee():
    for employee in employees:
        print "trying with : " + employee
        coord = analysePicture(os.getcwd() + '/pictures/employees/' + employee, os.getcwd() + '/temp/my_screenshot2.png', 0.8)

        if coord != (0, 0):
            pyautogui.click(coord)
            print "Employee found!"
            return True

    return False

def startAction():
    for action in startActions:
        print "trying action : " + action

        coord = analysePicture(os.getcwd() + '/pictures/actions/' + action, os.getcwd() + '/temp/my_screenshot2.png', 0.8)

        if coord != (0, 0):
            pyautogui.click(coord)
            print "Day started!"
            return True
    return False

def analysePicture(picture, template_img, similarity):
    img = cv2.imread(picture,0)
    template = cv2.imread(template_img,0)
    method = eval('cv2.TM_CCOEFF_NORMED')

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val < similarity:
        return (0,0)
    else:
        return max_loc

def play():
    im = pyautogui.screenshot()
    im.save(os.getcwd() + '/temp/my_screenshot2.png')

    if startAction() == False:
        if getCustomer() == False:
            if getEmployee():
                time.sleep(1.5)
                im = pyautogui.screenshot()
                im.save(os.getcwd() + '/temp/my_screenshot2.png')
                makeEmployeeAction()
        else:
            time.sleep(1.5)
            im = pyautogui.screenshot()
            im.save(os.getcwd() + '/temp/my_screenshot2.png')
            if makeCustomerAction() == "suggest":
                time.sleep(1.5)
                im = pyautogui.screenshot()
                im.save(os.getcwd() + '/temp/my_screenshot2.png')
                makeSuggestAction()
                time.sleep(2.5)

def main():
    while True :
        play()


if __name__ == '__main__':
    main()