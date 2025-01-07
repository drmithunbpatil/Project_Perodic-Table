from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
# Periodic table data
ELEMENTS = [
    {"atomic_number": 1, "symbol": "H", "name": "Hydrogen", "weight": 1.008},
    {"atomic_number": 2, "symbol": "He", "name": "Helium", "weight": 4.0026},
    {"atomic_number": 3, "symbol": "Li", "name": "Lithium", "weight": 6.94},
    {"atomic_number": 4, "symbol": "Be", "name": "Beryllium", "weight": 9.0122},
    {"atomic_number": 5, "symbol": "B", "name": "Boron", "weight": 10.81},
    {"atomic_number": 6, "symbol": "C", "name": "Carbon", "weight": 12.011},
    {"atomic_number": 7, "symbol": "N", "name": "Nitrogen", "weight": 14.007},
    {"atomic_number": 8, "symbol": "O", "name": "Oxygen", "weight": 15.999},
    {"atomic_number": 9, "symbol": "F", "name": "Fluorine", "weight": 18.998},
    {"atomic_number": 10, "symbol": "Ne", "name": "Neon", "weight": 20.180},
    {"atomic_number": 11, "symbol": "Na", "name": "Sodium", "weight": 22.990},
    {"atomic_number": 12, "symbol": "Mg", "name": "Magnesium", "weight": 24.305},
    {"atomic_number": 13, "symbol": "Al", "name": "Aluminium", "weight": 26.982},
    {"atomic_number": 14, "symbol": "Si", "name": "Silicon", "weight": 28.085},
    {"atomic_number": 15, "symbol": "P", "name": "Phosphorus", "weight": 30.974},
    {"atomic_number": 16, "symbol": "S", "name": "Sulfur", "weight": 32.06},
    {"atomic_number": 17, "symbol": "Cl", "name": "Chlorine", "weight": 35.45},
    {"atomic_number": 18, "symbol": "Ar", "name": "Argon", "weight": 39.948},
    {"atomic_number": 19, "symbol": "K", "name": "Potassium", "weight": 39.098},
    {"atomic_number": 20, "symbol": "Ca", "name": "Calcium", "weight": 40.078},
    {"atomic_number": 21, "symbol": "Sc", "name": "Scandium", "weight": 44.956},
    {"atomic_number": 22, "symbol": "Ti", "name": "Titanium", "weight": 47.867},
    {"atomic_number": 23, "symbol": "V", "name": "Vanadium", "weight": 50.942},
    {"atomic_number": 24, "symbol": "Cr", "name": "Chromium", "weight": 51.996},
    {"atomic_number": 25, "symbol": "Mn", "name": "Manganese", "weight": 54.938},
    {"atomic_number": 26, "symbol": "Fe", "name": "Iron", "weight": 55.845},
    {"atomic_number": 27, "symbol": "Co", "name": "Cobalt", "weight": 58.933},
    {"atomic_number": 28, "symbol": "Ni", "name": "Nickel", "weight": 58.693},
    {"atomic_number": 29, "symbol": "Cu", "name": "Copper", "weight": 63.546},
    {"atomic_number": 30, "symbol": "Zn", "name": "Zinc", "weight": 65.38},
    {"atomic_number": 31, "symbol": "Ga", "name": "Gallium", "weight": 69.723},
    {"atomic_number": 32, "symbol": "Ge", "name": "Germanium", "weight": 72.63},
    {"atomic_number": 33, "symbol": "As", "name": "Arsenic", "weight": 74.922},
    {"atomic_number": 34, "symbol": "Se", "name": "Selenium", "weight": 78.971},
    {"atomic_number": 35, "symbol": "Br", "name": "Bromine", "weight": 79.904},
    {"atomic_number": 36, "symbol": "Kr", "name": "Krypton", "weight": 83.798},
    {"atomic_number": 37, "symbol": "Rb", "name": "Rubidium", "weight": 85.468},
    {"atomic_number": 38, "symbol": "Sr", "name": "Strontium", "weight": 87.62},
    {"atomic_number": 39, "symbol": "Y", "name": "Yttrium", "weight": 88.906},
    {"atomic_number": 40, "symbol": "Zr", "name": "Zirconium", "weight": 91.224},
    {"atomic_number": 41, "symbol": "Nb", "name": "Niobium", "weight": 92.906},
    {"atomic_number": 42, "symbol": "Mo", "name": "Molybdenum", "weight": 95.95},
    {"atomic_number": 43, "symbol": "Tc", "name": "Technetium", "weight": 98},
    {"atomic_number": 44, "symbol": "Ru", "name": "Ruthenium", "weight": 101.07},
    {"atomic_number": 45, "symbol": "Rh", "name": "Rhodium", "weight": 102.91},
    {"atomic_number": 46, "symbol": "Pd", "name": "Palladium", "weight": 106.42},
    {"atomic_number": 47, "symbol": "Ag", "name": "Silver", "weight": 107.87},
    {"atomic_number": 48, "symbol": "Cd", "name": "Cadmium", "weight": 112.41},
    {"atomic_number": 49, "symbol": "In", "name": "Indium", "weight": 114.82},
    {"atomic_number": 50, "symbol": "Sn", "name": "Tin", "weight": 118.71},
    {"atomic_number": 51, "symbol": "Sb", "name": "Antimony", "weight": 121.76},
    {"atomic_number": 52, "symbol": "Te", "name": "Tellurium", "weight": 127.6},
    {"atomic_number": 53, "symbol": "I", "name": "Iodine", "weight": 126.9},
    {"atomic_number": 54, "symbol": "Xe", "name": "Xenon", "weight": 131.29},
    {"atomic_number": 55, "symbol": "Cs", "name": "Cesium", "weight": 132.91},
    {"atomic_number": 56, "symbol": "Ba", "name": "Barium", "weight": 137.33},
    {"atomic_number": 57, "symbol": "La", "name": "Lanthanum", "weight": 138.91},
    {"atomic_number": 58, "symbol": "Ce", "name": "Cerium", "weight": 140.12},
    {"atomic_number": 59, "symbol": "Pr", "name": "Praseodymium", "weight": 140.91},
    {"atomic_number": 60, "symbol": "Nd", "name": "Neodymium", "weight": 144.24},
    {"atomic_number": 61, "symbol": "Pm", "name": "Promethium", "weight": 145},
    {"atomic_number": 62, "symbol": "Sm", "name": "Samarium", "weight": 150.36},
    {"atomic_number": 63, "symbol": "Eu", "name": "Europium", "weight": 151.96},
    {"atomic_number": 64, "symbol": "Gd", "name": "Gadolinium", "weight": 157.25},
    {"atomic_number": 65, "symbol": "Tb", "name": "Terbium", "weight": 158.93},
    {"atomic_number": 66, "symbol": "Dy", "name": "Dysprosium", "weight": 162.5},
    {"atomic_number": 67, "symbol": "Ho", "name": "Holmium", "weight": 164.93},
    {"atomic_number": 68, "symbol": "Er", "name": "Erbium", "weight": 167.26},
    {"atomic_number": 69, "symbol": "Tm", "name": "Thulium", "weight": 168.93},
    {"atomic_number": 70, "symbol": "Yb", "name": "Ytterbium", "weight": 173.05},
    {"atomic_number": 71, "symbol": "Lu", "name": "Lutetium", "weight": 174.97},
    {"atomic_number": 72, "symbol": "Hf", "name": "Hafnium", "weight": 178.49},
    {"atomic_number": 73, "symbol": "Ta", "name": "Tantalum", "weight": 180.95},
    {"atomic_number": 74, "symbol": "W", "name": "Tungsten", "weight": 183.84},
    {"atomic_number": 75, "symbol": "Re", "name": "Rhenium", "weight": 186.21},
    {"atomic_number": 76, "symbol": "Os", "name": "Osmium", "weight": 190.23},
    {"atomic_number": 77, "symbol": "Ir", "name": "Iridium", "weight": 192.22},
    {"atomic_number": 78, "symbol": "Pt", "name": "Platinum", "weight": 195.08},
    {"atomic_number": 79, "symbol": "Au", "name": "Gold", "weight": 196.97},
    {"atomic_number": 80, "symbol": "Hg", "name": "Mercury", "weight": 200.59},
    {"atomic_number": 81, "symbol": "Tl", "name": "Thallium", "weight": 204.38},
    {"atomic_number": 82, "symbol": "Pb", "name": "Lead", "weight": 207.2},
    {"atomic_number": 83, "symbol": "Bi", "name": "Bismuth", "weight": 208.98},
    {"atomic_number": 84, "symbol": "Po", "name": "Polonium", "weight": 209},
    {"atomic_number": 85, "symbol": "At", "name": "Astatine", "weight": 210},
    {"atomic_number": 86, "symbol": "Rn", "name": "Radon", "weight": 222},
    {"atomic_number": 87, "symbol": "Fr", "name": "Francium", "weight": 223},
    {"atomic_number": 88, "symbol": "Ra", "name": "Radium", "weight": 226},
    {"atomic_number": 89, "symbol": "Ac", "name": "Actinium", "weight": 227},
    {"atomic_number": 90, "symbol": "Th", "name": "Thorium", "weight": 232.04},
    {"atomic_number": 91, "symbol": "Pa", "name": "Protactinium", "weight": 231.04},
    {"atomic_number": 92, "symbol": "U", "name": "Uranium", "weight": 238.03},
    {"atomic_number": 93, "symbol": "Np", "name": "Neptunium", "weight": 237},
    {"atomic_number": 94, "symbol": "Pu", "name": "Plutonium", "weight": 244},
    {"atomic_number": 95, "symbol": "Am", "name": "Americium", "weight": 243},
    {"atomic_number": 96, "symbol": "Cm", "name": "Curium", "weight": 247},
    {"atomic_number": 97, "symbol": "Bk", "name": "Berkelium", "weight": 247},
    {"atomic_number": 98, "symbol": "Cf", "name": "Californium", "weight": 251},
    {"atomic_number": 99, "symbol": "Es", "name": "Einsteinium", "weight": 252},
    {"atomic_number": 100, "symbol": "Fm", "name": "Fermium", "weight": 257},
    {"atomic_number": 101, "symbol": "Md", "name": "Mendelevium", "weight": 258},
    {"atomic_number": 102, "symbol": "No", "name": "Nobelium", "weight": 259},
    {"atomic_number": 103, "symbol": "Lr", "name": "Lawrencium", "weight": 266},
    {"atomic_number": 104, "symbol": "Rf", "name": "Rutherfordium", "weight": 267},
    {"atomic_number": 105, "symbol": "Db", "name": "Dubnium", "weight": 270},
    {"atomic_number": 106, "symbol": "Sg", "name": "Seaborgium", "weight": 271},
    {"atomic_number": 107, "symbol": "Bh", "name": "Bohrium", "weight": 270},
    {"atomic_number": 108, "symbol": "Hs", "name": "Hassium", "weight": 277},
    {"atomic_number": 109, "symbol": "Mt", "name": "Meitnerium", "weight": 278},
    {"atomic_number": 110, "symbol": "Ds", "name": "Darmstadtium", "weight": 281},
    {"atomic_number": 111, "symbol": "Rg", "name": "Roentgenium", "weight": 282},
    {"atomic_number": 112, "symbol": "Cn", "name": "Copernicium", "weight": 285},
    {"atomic_number": 113, "symbol": "Nh", "name": "Nihonium", "weight": 286},
    {"atomic_number": 114, "symbol": "Fl", "name": "Flerovium", "weight": 289},
    {"atomic_number": 115, "symbol": "Mc", "name": "Moscovium", "weight": 290},
    {"atomic_number": 116, "symbol": "Lv", "name": "Livermorium", "weight": 293},
    {"atomic_number": 117, "symbol": "Ts", "name": "Tennessine", "weight": 294},
    {"atomic_number": 118, "symbol": "Og", "name": "Oganesson", "weight": 294}
]



# Define periodic table categories and their colors
CATEGORY_COLORS = {
    "alkali_metal": [1, 3, 11, 19, 37, 55, 87],
    "alkaline_earth_metal": [4, 12, 20, 38, 56, 88],
    "transition_metal": list(range(21, 31)) + list(range(39, 49)) + list(range(72, 81)) + [104, 105, 106],
    "lanthanide": list(range(57, 72)),
    "actinide": list(range(89, 104)),
    "metalloid": [5, 14, 32, 33, 51, 52, 84],
    "halogen": [9, 17, 35, 53, 85, 117],
    "noble_gas": [2, 10, 18, 36, 54, 86, 118],
    "other_nonmetal": [1, 6, 7, 8, 15, 16, 34],
}

CATEGORY_COLOR_MAPPING = {
    "alkali_metal": "#FF6666",
    "alkaline_earth_metal": "#FFB266",
    "transition_metal": "#FFD966",
    "lanthanide": "#99CCFF",
    "actinide": "#B3B3FF",
    "metalloid": "#80FF80",
    "halogen": "#FF80FF",
    "noble_gas": "#66FFFF",
    "other_nonmetal": "#FFFF99",
}

class PeriodicTable(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 10  # Define rows for the periodic table layout
        self.cols = 18  # Maximum number of groups
        self.spacing = 2
        self.padding = 5
        self.create_table()

    def get_color(self, atomic_number):
        for category, elements in CATEGORY_COLORS.items():
            if atomic_number in elements:
                return CATEGORY_COLOR_MAPPING[category]
        return "#FFFFFF"  # Default color (white)

    def create_table(self):
        # Create blank spots for proper periodic table alignment
        BLANK_SPOTS = [
            (1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1), (5, 0), (5, 1),
            (6, 0), (6, 1), (7, 0), (7, 1), (8, 0), (8, 1),
        ]
        
        for row in range(1, 10):
            for col in range(1, 19):
                if (row, col) in BLANK_SPOTS:
                    self.add_widget(Label())  # Add empty space

        # Add elements with buttons
        for element in ELEMENTS:
            button = Button(
                text=f"{element['symbol']}\n{element['atomic_number']}",
                size_hint=(None, None),
                size=(80, 80),
                background_color=self.get_color(element['atomic_number'])
            )
            button.bind(on_press=lambda instance, el=element: self.show_element_details(el))
            self.add_widget(button)

    def show_element_details(self, element):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Name: {element['name']}"))
        content.add_widget(Label(text=f"Symbol: {element['symbol']}"))
        content.add_widget(Label(text=f"Atomic Number: {element['atomic_number']}"))
        content.add_widget(Label(text=f"Atomic Weight: {element['weight']}"))
        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50))
        content.add_widget(close_button)

        popup = Popup(title=f"Details: {element['symbol']}", content=content, size_hint=(0.8, 0.6))
        close_button.bind(on_press=popup.dismiss)
        popup.open()


class PeriodicTableApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        root.add_widget(Label(text="Developed by Dr. Mithun B. Patil    N K Orchid College of Engineering Solapur", size_hint=(1, 0.1), font_size='20sp'))
        root.add_widget(PeriodicTable(size_hint=(1, 0.9)))
        return root

if __name__ == "__main__":
    PeriodicTableApp().run()
