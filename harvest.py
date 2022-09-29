############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        # self.attributes
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

## check back in with this for for loop?

        # set new info = instance
        self.pairings.append(pairing)
        # MelonType.pairing = pairing
    

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # instantiating a melon
    # call the add_pairing method to add necessary pairings to the instancse's pairings attribute

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("strawberries and mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow = MelonType("yw", "Yellow", 2013, "yellow", False, True)
    yellow.add_pairing("ice cream")
    all_melon_types.append(yellow)


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # takes a list of melon_types objects
    # identical to what melon_types returns
    # loop through list
    for object in melon_types:
        print(f"{object} pairs with")

    # for every value in melon_types 
    # print f"self.name self.pairing"
    # print each melon_type pairings
    # returns None

    # prints 
    # Muskmelon pairs with
    # - mint


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest



