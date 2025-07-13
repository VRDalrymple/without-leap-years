import leapyearcalc
from pyscript import document

def displaydate():
    output_div = document.querySelector("#output")
    output_div.innerText = leapyearcalc.calculate()
