# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class Pasts_Killed_Goal_Amount(Range):
    """Select how many pasts must be killed to complete the game. (ensure you have enough characters with pasts to complete the game)"""
    display_name = "Number of characters to kill the past with before victory"
    range_start = 1
    range_end = 8
    default = 4

class enable_secret_characters(Toggle):
    """Enables the Bullet and the Robot, adds 2 pasts"""
    display_name = "Enable secret characters"
    Default = False

class enable_farewell_to_arms_characters(Toggle):
    """Enables the Paradox and the Gunslinger, adds 1 past"""
    display_name = "Enable farewell to arms characters"
    Default = False

class enable_cultist(Toggle):
    """Enables the Cultist, does not add a past"""
    display_name = "Enable farewell the cultist"
    Default = False

class enable_cut_content(Toggle):
    """Enables cut gungeoneers (The Ninja, Lamey, and the Cosmonaut), adds 1 past"""
    display_name = "Enable cut content"
    Default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["Pasts_Killed_Goal_Amount"] = Pasts_Killed_Goal_Amount
    options["enable_secret_characters"] = enable_secret_characters
    options["enable_farewell_to_arms_characters"] = enable_farewell_to_arms_characters
    options["enable_cultist"] = enable_cultist
    options["enable_cut_content"] = enable_cut_content
    return options



# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
