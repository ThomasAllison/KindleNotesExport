from bs4 import BeautifulSoup

INDENTATION = "    "

with open('ExampleNotes.html', 'r') as file:
    html_doc = file

    soup = BeautifulSoup(html_doc, 'html.parser')

    desired_divs = soup.findAll('div', attrs={'class': ['sectionHeading', 'noteHeading', 'noteText']})

    skip_next = False
    for current_div, next_div in zip(desired_divs, desired_divs[1:]):
        indentation_multiplier = 0

        current_div_class = current_div['class'][0]
        current_div_text = current_div.text.strip()

        if current_div_class == "sectionHeading":
            print("-", current_div_text)
        elif skip_next:
            skip_next = False
        else:
            next_div_class = next_div['class'][0]
            next_div_text = next_div.text.strip()

            # print(current_div_text, "|", next_div_text)

            if current_div_text.startswith('Highlight'):
                indentation_multiplier = 1
            elif current_div_text.startswith('Note'):
                indentation_multiplier = 2

            print(indentation_multiplier*INDENTATION, "-", next_div_text)
            skip_next = True


    # for previous_div, current_div in zip(desired_divs, desired_divs[1:]):
    #     indentation_multiplier = 0
    #
    #     previous_div_class = previous_div['class'][0]
    #     previous_div_text = previous_div.text.strip()
    #
    #     current_div_class = current_div['class'][0]
    #     current_div_text = current_div.text.strip()
    #
    #     # if div_text.startswith('Highlight'):
    #     #     indentation_multiplier = 1
    #     # elif div_text.startswith('Note'):
    #     #     indentation_multiplier = 2
    #
    #     print(previous_div_text, "|" ,current_div_text)