import pyautogui, time

# Set x,y and RGB for Name field and Submit button
nameFiled = (430, 410)
submitButton = (433, 942)
submitButtonColor = (74, 139, 245)
submitAnotherLink = (610, 508)
pyautogui.PAUSE = 1 # pause 1 s after each function call

# Input data
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent'},
            ]

for person in formData:
    # If Ctrl+C, stop the scrpit
    print('------ 5 seconds pause to let user press Ctrl-C')
    time.sleep(5)

    # Wait until the form webpage has loaded
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)
    print('Entering info: %s ' % (person['name']))
    pyautogui.click(nameFiled[0], nameFiled[1])

# Fill out the Name Field
    pyautogui.typewrite(person['name'] + '\t')

# Fill out the Greatest Fear field
    pyautogui.typewrite(person['fear'] + '\t')

# Fill out the Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

# Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

# Fill out the Additional Comments field
    pyautogui.typewrite(person['comments'] + '\t')

# Click Submit
    pyautogui.press('enter')

# Wait until form webpage has loaded
    # print('Clicked Submit button')
    time.sleep(5)

# Click the "Submit another response link"
    pyautogui.click(610, 308)


