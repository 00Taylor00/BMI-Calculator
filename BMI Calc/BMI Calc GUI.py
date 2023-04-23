import PySimpleGUI as sg


# BMI calculator body
def bmi(weight_kgs, height_ms):
    if height_ms < 1.0 or height_ms > 2.5 or weight_kgs < 20 or weight_kgs > 200:
        return None
    return weight_kgs / height_ms ** 2


# Conversion function for weight lbs to kilograms
def lbs_to_kg(lbs):
    weight_kgs = lbs * 0.45359
    return weight_kgs


# Conversion function for imperial to metric height
def footinches_to_m(feet, inch):
    height_ms = (feet * 30.34 + inch * 2.54) / 100
    return height_ms


# Set PySimpleGUI theme and options
sg.theme('LightBlue')
sg.set_options(font=('Helvetica', 14))

# Define opening window layout
layout_opening_window = [
    [sg.Text('Welcome to the BMI calculator', font=('Helvetica', 20, 'underline'))],
    [sg.Text('Are you over 18 years old?', font=('Helvetica', 16))],
    [sg.Input(key='age', size=(5, 1), font=('Helvetica', 16))],
    [sg.Button('Submit', font=('Helvetica', 16))],
    [sg.Button('Kilogram/Metres', key='Kg/M', button_color=('white', 'blue'), font=('Helvetica', 16), enable_events=True, pad=((200, 5), 10)),
     sg.Button('Feet/Inches/Pounds', key='Ft/In/Lbs', button_color=('white', 'blue'), font=('Helvetica', 16), enable_events=True, pad=((5, 200), 10))]
]

# Define layout for Kg/M input
layout_kgm = [
    [sg.Text('Enter your weight (in kg)', font=('Helvetica', 16))],
    [sg.Input(key='weight_kgs', font=('Helvetica', 16))],
    [sg.Text('Enter your height (in m)', font=('Helvetica', 16))],
    [sg.Input(key='height_ms', font=('Helvetica', 16))],
    [sg.Text('', key='result_output', font=('Helvetica', 14), text_color='black', size=(70, 1))],
    [sg.Button('Calculate BMI', font=('Helvetica', 16))],
]

# Define layout for Ft/In/Lbs input
layout_fil = [
    [sg.Text('Enter your weight', font=('Helvetica', 16))],
    [sg.Input(key='weight_lbs', size=(10, 1), font=('Helvetica', 16)), sg.Text('lbs', font=('Helvetica', 16))],
    [sg.Text('Enter your height', font=('Helvetica', 16))],
    [sg.Input(key='feet', size=(10, 1), font=('Helvetica', 16)), sg.Text('ft', font=('Helvetica', 16)),
     sg.Input(key='inches', size=(10, 1), font=('Helvetica', 16)), sg.Text('in', font=('Helvetica', 16))],
    [sg.Text('', key='result_output', font=('Helvetica', 14), text_color='black', size=(70, 1))],
    [sg.Button('Calculate BMI', font=('Helvetica', 16))],
]

# Create window using opening window layout
window = sg.Window('BMI Calculator', layout_opening_window)

kgm_button = window['Kg/M']
fil_button = window['Ft/In/Lbs']

# Main event loop
while True:
    event, values = window.read()

    # Close window if 'Exit' button or window X is clicked
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    # Toggle Kg/M and Ft/In/Lbs buttons
    if event == 'Kg/M':
        kgm_button.update(button_color=('white', 'green'))
        fil_button.update(button_color=('white', 'red'))

    elif event == 'Ft/In/Lbs':
        fil_button.update(button_color=('white', 'green'))
        kgm_button.update(button_color=('white', 'red'))

    # Handle 'Submit' button

    elif event == 'Submit':
        valid_age = values['age']

        if valid_age.lower() in ["yes", "y"] and kgm_button.ButtonColor == ('white', 'green') and fil_button.ButtonColor == ('white', 'red'):
            window.close()
            window = sg.Window('BMI Calculator', layout_kgm)

        elif valid_age.lower() in ["yes", "y"] and kgm_button.ButtonColor == ('white', 'red') and fil_button.ButtonColor == ('white', 'green'):
            window.close()
            window = sg.Window('BMI Calculator', layout_fil)

        elif valid_age.lower() in ["no", "n"]:
            sg.popup('Come back when you are a little bit older! The BMI is only valid if your older than 18 years of age')

    # Handle 'Calculate BMI' button
    elif event == 'Calculate BMI':
        # Check which layout is being used
        if 'weight_lbs' in values:  # Using Ft/In/Lbs layout
            weight_lbs = float(values['weight_lbs'])
            feet = float(values['feet'])
            inch = float(values['inches'])
            height_ms = footinches_to_m(feet, inch)
            weight_kgs = lbs_to_kg(weight_lbs)
        else:  # Using Kg/M layout
            weight_kgs = float(values['weight_kgs'])
            height_ms = float(values['height_ms'])

        # Calculate BMI and update output
        calculated_bmi = bmi(weight_kgs, height_ms)
        if calculated_bmi is None:
            window['result_output'].update('Invalid weight or height value. Please try again.')
        else:
            if calculated_bmi <= 18.5:
                window['result_output'].update(f'You are defined as underweight with a BMI of {calculated_bmi:.2f}')
            elif calculated_bmi > 18.5 and calculated_bmi < 24.9:
                window['result_output'].update(f'You are defined as having a healthy weight with a BMI of {calculated_bmi:.2f}')
            elif calculated_bmi >= 25 and calculated_bmi < 29.9:
                window['result_output'].update(f'You are defined as overweight with a BMI of {calculated_bmi:.2f}')
            elif calculated_bmi >= 30 and calculated_bmi < 39.9:
                window['result_output'].update(f'You are defined as obese with a BMI of {calculated_bmi:.2f}')
            else:
                window['result_output'].update(f'You are defined as severely obese with a BMI of {calculated_bmi:.2f}')

    # Handle invalid events
    else:
        sg.popup('Invalid response. Please try again.')

# Close the window when the event loop is exited
window.close()
