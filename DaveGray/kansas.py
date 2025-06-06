from random import choice
capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"

def randomfunfact():
    funfact = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas city.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Kansas is known for its wheat production.",
        "Most Kansans are annoyed by wizard of OZ references from people outside of Kansas.",
    ]
    index = choice('01234')
    print(funfact[int(index)])
if __name__ == "__main__":
    randomfunfact()
    