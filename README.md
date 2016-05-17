# QuickVU

## Team Members

1. Benjamin Acevedo
2. Tarik Calderon
3. Michael Mercado
4. Andros Rosa

## Introduction

QuickVU is a programming language designed to facilitate user interface development for web projects by merging the most common UI web technologies into one product. The current UI development method for the web requires knowledge of various web technologies such as HTML, CSS, JavaScript. Hence, developers end up working with different languages each with different syntax, procedures and learning curves. Consequently, our motivation for creating QuickVU comes from the idea that the process of developing web UI’s can be simplified by unifying the most used web technologies and standards into one programming language. QuickVU provides a tool for developers where the code they write is converted into a fully functional static website containing all the required HTML, Javascript and CSS code in combination with standard web development libraries and dependencies.

## Setting up QuickVU

1. Download as ZIP or clone to desired location
2. Open terminal session and navigate to the QuickVU directory
3. Install dependencies:
  * PyQuery:
    - sudo pip install pyquery
  * BeautifulSoup:
    - sudo pip install beautifulsoup4
4. Run QuickVU:
  * python quickvu.py

## Sample usage

1. *QuickVu* `> <vucreate htmlpage>`
2. *QuickVu* `> <vumenu 1>`
3. *QuickVu* `> <vuelement heading1>`
4. *QuickVu* `> <vuelement paragraph>`
5. *QuickVu* `> <vuelement heading2>`
6. *QuickVu* `> <vuelement table>`
7. *QuickVu* `> <vuelement image>`
8. *QuickVu* `> <vuform textarea>`
9. *QuickVu* `> <vuform dropdown>`
10.	*QuickVu* `> <vuform password>`
11.	*QuickVu* `> <vuform submit>`
12.	*QuickVu* `> <vufinish>`

## Language Reference Manual

Command | Parameter | Description
------- | --------- | ----------
`<vucreate page_title>` | Any name | The title of the web page
`<vumenu x>` | 1, 2, 3 | 1. White navigation template
2. Black navigation template
3. Black navigation and responsive template
`<vuelement headingX>` | heading1, heading2, heading3, heading4, heading5, heading6 | Creates a dummy heading
`<vuelement paragraph>` | paragraph | Adds a dummy paragraph
`<vuelement table>` | table | Creates a dummy table
`<vuelement image>` | image | Displays a dummy image
`<vuelement list>` | list | Creates a dummy list
`<vuelement button>` | button | Creates a default button
`<vuform textarea>` | textarea | Creates a form with a text area
`<vuform dropdown>` | dropdown | Creates a dropdown on the form
`<vuform radio>` | radio | Creates a radio element for the form
`<vuform checkbox>` | checkbox | Creates a simple checkbox element
`<vuform text>` | text | Creates a simple are to input text
`<vuform password>` | password | Creates area for password input
`<vuform number>` | number | Creates area to input numbers
`<vuform submit>` | submit | Creates a submit button
`<vufinish>` | N/A | Finishes the web page and opens it. Also adds default footer for web page.
